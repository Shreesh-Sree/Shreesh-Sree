#!/usr/bin/env python3
"""Builds the animated ASCII terminal SVGs for the profile README.

Stdlib only. Run locally with `python scripts/build.py` or let the
GitHub Action run it on a schedule. Live numbers come from the GitHub
REST + GraphQL APIs (GITHUB_TOKEN). If a fetch fails, the last good
values in data/cache.json are reused so the README never breaks.

Flags:
  --data PATH   use a JSON fixture instead of hitting the API
  --offline     skip the API and render from cache (or placeholders)
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
CFG = json.loads((ROOT / "data" / "profile.json").read_text(encoding="utf-8"))
CACHE = ROOT / "data" / "cache.json"
ASSETS = ROOT / "assets"
README = ROOT / "README.md"
TZ = dt.timezone(dt.timedelta(minutes=CFG.get("tz_offset_minutes", 0)))
USER = CFG["user"]

# --------------------------------------------------------------------------
# geometry + themes
# --------------------------------------------------------------------------
FS, CW, LH = 14, 8.4, 20          # font size, char width, line height (px)
PADX, PADY, BAR = 22, 14, 34       # side padding, top/bottom padding, title bar
FONT = ("ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,"
        "'Liberation Mono','DejaVu Sans Mono',monospace")

THEMES = {
    "dark": dict(
        bg="#0d1117", border="#30363d", bar="#161b22", fg="#c9d1d9", dim="#6e7681",
        mute="#8b949e", green="#3fb950", cyan="#39c5cf", blue="#58a6ff",
        yellow="#d29922", magenta="#bc8cff", red="#ff7b72", orange="#ffa657",
        heat=["#2d333b", "#0e4429", "#006d32", "#26a641", "#39d353"], scan="#c9d1d9",
    ),
    "light": dict(
        bg="#ffffff", border="#d0d7de", bar="#f6f8fa", fg="#1f2328", dim="#8c959f",
        mute="#656d76", green="#1a7f37", cyan="#1b7c83", blue="#0969da",
        yellow="#9a6700", magenta="#8250df", red="#cf222e", orange="#bc4c00",
        heat=["#d0d7de", "#9be9a8", "#40c463", "#30a14e", "#216e39"], scan="#1f2328",
    ),
}
PH = "…"  # placeholder when a live value is unavailable


def fmt(n) -> str:
    return PH if n is None else f"{n:,}"


# --------------------------------------------------------------------------
# terminal SVG renderer
# --------------------------------------------------------------------------
class Term:
    """A grid of monospace cells. Every coloured run is its own <text> with a
    forced textLength, so box-drawing glyphs stay on the grid whatever font
    the viewer's browser falls back to."""

    def __init__(self, cols: int, title: str = "", chrome: bool = True):
        self.cols, self.title, self.chrome = cols, title, chrome
        self.rows: list[tuple[list, dict]] = []
        self.defs: list[str] = []
        self.over: list = []       # callables (theme) -> svg, drawn after text
        self._id = 0

    # -- building ----------------------------------------------------------
    def uid(self, p="c") -> str:
        self._id += 1
        return f"{p}{self._id}"

    def line(self, spans=None, at=None, typed=None, dur=0.25, clip=None):
        """spans: str | list[(text, colour_key[, extra_svg])]; at: reveal time;
        typed: seconds per char to type the line instead of fading it in."""
        if spans is None:
            spans = []
        if isinstance(spans, str):
            spans = [(spans, "fg")]
        self.rows.append((spans, dict(at=at, typed=typed, dur=dur, clip=clip)))
        return len(self.rows) - 1

    def blank(self):
        return self.line([])

    # -- coordinates ---------------------------------------------------------
    def top(self) -> float:
        return (BAR if self.chrome else 0) + PADY

    def x(self, col: float) -> float:
        return PADX + col * CW

    def y(self, row: int) -> float:       # baseline
        return self.top() + row * LH + FS

    def ytop(self, row: int) -> float:
        return self.top() + row * LH + 3

    @property
    def width(self) -> float:
        return PADX * 2 + self.cols * CW

    @property
    def height(self) -> float:
        return self.top() + len(self.rows) * LH + PADY + 4

    # -- rendering ------------------------------------------------------------
    @staticmethod
    def text(x, y, s, fill, extra="", attrs=""):
        """Emit one <text> per run of non-space characters (single spaces kept
        inside a run). Browsers collapse whitespace in SVG-as-image, so any
        run of 2+ spaces becomes a gap in x instead of characters."""
        out = []
        for m in re.finditer(r"\S+(?: \S+)*", s):
            seg = m.group(0)
            sx = x + m.start() * CW
            out.append(f'<text x="{sx:.1f}" y="{y:.1f}" fill="{fill}" textLength="{len(seg) * CW:.1f}" '
                       f'lengthAdjust="spacingAndGlyphs"{attrs}>{escape(seg)}{extra}</text>')
        return "".join(out)

    def render_row(self, r, spans, th) -> str:
        out, col = [], 0
        for sp in spans:
            txt, ck = sp[0], sp[1]
            extra = sp[2] if len(sp) > 2 else ""
            if callable(extra):
                extra = extra(th)
            fill = th.get(ck, ck)
            out.append(self.text(self.x(col), self.y(r), txt, fill, extra))
            col += len(txt)
        return "".join(out)

    def svg(self, th: dict) -> str:
        W, H = self.width, self.height
        body = []
        for r, (spans, o) in enumerate(self.rows):
            inner = self.render_row(r, spans, th)
            if not inner:
                continue
            if o["typed"] and o["at"] is not None:
                n = sum(len(s[0]) for s in spans)
                cid = self.uid("t")
                steps = [i * CW + (4 if i == n else 0) for i in range(n + 1)]
                vals = ";".join(f"{v:.1f}" for v in steps)
                keys = ";".join(f"{i / n:.4f}" for i in range(n + 1)) if n else "0"
                self.defs.append(
                    f'<clipPath id="{cid}"><rect x="{PADX - 2}" y="{self.ytop(r) - 2}" width="0" height="{LH}">'
                    f'<animate attributeName="width" values="{vals}" keyTimes="{keys}" calcMode="discrete" '
                    f'begin="{o["at"]}s" dur="{max(n * o["typed"], 0.01):.2f}s" fill="freeze"/></rect></clipPath>')
                body.append(f'<g clip-path="url(#{cid})">{inner}</g>')
            elif o["at"] is not None:
                body.append(f'<g opacity="0">{inner}<animate attributeName="opacity" from="0" to="1" '
                            f'begin="{o["at"]}s" dur="{o["dur"]}s" fill="freeze"/></g>')
            elif o["clip"]:
                body.append(f'<g clip-path="url(#{o["clip"]})">{inner}</g>')
            else:
                body.append(inner)
        over = "".join(f(th) for f in self.over)
        chrome = ""
        if self.chrome:
            chrome = (
                f'<rect x="0.5" y="0.5" width="{W - 1}" height="{BAR}" rx="10" fill="{th["bar"]}"/>'
                f'<rect x="0.5" y="{BAR - 10}" width="{W - 1}" height="10" fill="{th["bar"]}"/>'
                f'<line x1="0" y1="{BAR + .5}" x2="{W}" y2="{BAR + .5}" stroke="{th["border"]}"/>'
                + "".join(f'<circle cx="{20 + i * 20}" cy="{BAR / 2}" r="6" fill="{c}"/>'
                          for i, c in enumerate(["#ff5f57", "#febc2e", "#28c840"]))
                + f'<text x="{W / 2:.1f}" y="{BAR / 2 + 4.5:.1f}" fill="{th["mute"]}" font-size="12.5" '
                  f'text-anchor="middle">{escape(self.title)}</text>')
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:.0f}" height="{H:.0f}" '
            f'viewBox="0 0 {W:.0f} {H:.0f}" font-family="{FONT}" font-size="{FS}" role="img" '
            f'aria-label="{escape(self.title)}">'
            f'<defs>{"".join(self.defs)}</defs>'
            f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="10" fill="{th["bg"]}" '
            f'stroke="{th["border"] if self.chrome else th["bg"]}"/>{chrome}<g xml:space="preserve">{"".join(body)}</g>{over}</svg>')


def blink(th=None, dur=1.0) -> str:
    return (f'<animate attributeName="opacity" values="1;0" keyTimes="0;0.5" calcMode="discrete" '
            f'dur="{dur}s" repeatCount="indefinite"/>')


def shimmer(colors, dur=6.0, begin=0.0) -> str:
    vals = ";".join(colors + colors[-2::-1])
    return (f'<animate attributeName="fill" values="{vals}" dur="{dur}s" begin="{begin:.2f}s" '
            f'repeatCount="indefinite"/>')


def dots(key: str, val: str, width: int):
    n = max(2, width - len(key) - len(val) - 2)
    return [(key + " ", "blue"), ("." * n, "dim"), (" " + val, "cyan")]


def save(name: str, term_factory):
    ASSETS.mkdir(exist_ok=True)
    for theme, th in THEMES.items():
        t = term_factory()
        (ASSETS / f"{name}-{theme}.svg").write_text(t.svg(th), encoding="utf-8")


# --------------------------------------------------------------------------
# live data
# --------------------------------------------------------------------------
API = "https://api.github.com"


def gh(path: str, token: str | None, body: dict | None = None):
    url = path if path.startswith("http") else API + path
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method="POST" if data else "GET")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", f"{USER}-profile-readme")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def safe(label, fn, default=None):
    try:
        return fn()
    except Exception as e:  # noqa: BLE001 - any API hiccup falls back to cache
        print(f"[warn] {label}: {e}", file=sys.stderr)
        return default


def fetch_live(token: str | None) -> dict:
    now = dt.datetime.now(dt.timezone.utc)
    out: dict = {}

    # owned repos -> stars, languages
    def repos():
        allr, page = [], 1
        while page <= 10:
            batch = gh(f"/users/{USER}/repos?per_page=100&type=owner&page={page}", token)
            allr += batch
            if len(batch) < 100:
                break
            page += 1
        return allr

    rs = safe("repos", repos)
    if rs is not None:
        own = [r for r in rs if not r.get("fork")]
        out["repos"] = len(own)
        out["stars"] = sum(r.get("stargazers_count", 0) for r in own)
        langs: dict[str, int] = {}
        # featured repos that live in an org (e.g. the Go services) count toward languages too
        extra = []
        for p in CFG["projects"]:
            if p["repo"].split("/")[0].lower() != USER.lower():
                meta = safe(f"repo {p['repo']}", lambda p=p: gh(f"/repos/{p['repo']}", token))
                if meta and not meta.get("fork"):
                    extra.append(meta)
        for r in own + extra:
            if r.get("archived") or r.get("size", 0) == 0:
                continue
            got = safe(f"langs {r['name']}", lambda r=r: gh(r["languages_url"], token), {}) or {}
            for k, v in got.items():
                if k not in CFG.get("ignore_languages", []):
                    langs[k] = langs.get(k, 0) + v
        tot = sum(langs.values()) or 1
        out["languages"] = [[k, v / tot] for k, v in sorted(langs.items(), key=lambda kv: -kv[1])[:6]]

    # graphql: calendar, followers, commits, merged prs
    if token:
        jan1 = dt.datetime(now.year, 1, 1, tzinfo=dt.timezone.utc)
        q = """query($login:String!,$from:DateTime!,$to:DateTime!,$jan1:DateTime!){
          user(login:$login){
            createdAt followers{totalCount}
            pullRequests(states:MERGED){totalCount}
            repositoriesContributedTo(contributionTypes:[COMMIT,PULL_REQUEST],includeUserRepositories:false){totalCount}
            year: contributionsCollection(from:$from,to:$to){
              contributionCalendar{ totalContributions weeks{ contributionDays{ date contributionCount weekday } } }
            }
            ytd: contributionsCollection(from:$jan1,to:$to){ totalCommitContributions restrictedContributionsCount }
          }}"""
        v = dict(login=USER, to=now.isoformat(), jan1=jan1.isoformat(),
                 **{"from": (now - dt.timedelta(days=364)).isoformat()})
        res = safe("graphql", lambda: gh("/graphql", token, {"query": q, "variables": v}))
        u = (res or {}).get("data", {}).get("user") if res else None
        if u:
            out["created_at"] = u["createdAt"]
            out["followers"] = u["followers"]["totalCount"]
            out["prs_merged"] = u["pullRequests"]["totalCount"]
            out["contributed_to"] = u["repositoriesContributedTo"]["totalCount"]
            out["commits_ytd"] = u["ytd"]["totalCommitContributions"]
            cal = u["year"]["contributionCalendar"]
            out["calendar"] = [[d["date"], d["contributionCount"]]
                               for w in cal["weeks"] for d in w["contributionDays"]]
            out["contrib_total"] = cal["totalContributions"]
        elif res and res.get("errors"):
            print(f"[warn] graphql: {res['errors']}", file=sys.stderr)
    else:
        u = safe("user", lambda: gh(f"/users/{USER}", token))
        if u:
            out["created_at"] = u["created_at"]
            out["followers"] = u["followers"]

    # upstream pull requests
    up = CFG["upstream"]
    excl = "+".join(f"-user:{o}" for o in up["exclude_owners"])
    sr = safe("search prs", lambda: gh(
        f"/search/issues?q=is:pr+author:{USER}+{excl}&sort=created&order=desc&per_page=40", token))
    prs: dict[str, dict] = {}
    if sr:
        out["upstream_total"] = sr.get("total_count")
        for it in sr.get("items", []):
            repo = it["repository_url"].split("/repos/")[1]
            key = f"{repo}#{it['number']}"
            merged = (it.get("pull_request") or {}).get("merged_at")
            prs[key] = dict(key=key, title=it["title"], url=it["html_url"],
                            state="merged" if merged else it["state"], created=it["created_at"])
    for key in up["pinned"]:
        if key in prs:
            continue
        repo, num = key.split("#")
        p = safe(f"pr {key}", lambda repo=repo, num=num: gh(f"/repos/{repo}/pulls/{num}", token))
        if p:
            prs[key] = dict(key=key, title=p["title"], url=p["html_url"], created=p["created_at"],
                            state="merged" if p.get("merged_at") else p["state"])
    if prs:
        pinned = [prs[k] for k in up["pinned"] if k in prs]
        rest = [p for k, p in prs.items() if k not in up["pinned"]]
        out["prs"] = (pinned + rest)[: up["max_rows"]]

    # featured repos
    feat = {}
    for p in CFG["projects"]:
        r = safe(f"repo {p['repo']}", lambda p=p: gh(f"/repos/{p['repo']}", token))
        if r:
            feat[p["repo"]] = dict(stars=r.get("stargazers_count", 0), forks=r.get("forks_count", 0),
                                   lang=r.get("language"), pushed=r.get("pushed_at"),
                                   license=(r.get("license") or {}).get("spdx_id"))
    if feat:
        out["featured"] = feat
    return out


def load_data(args) -> dict:
    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    if args.data:
        live = json.loads(Path(args.data).read_text())
    elif args.offline:
        live = {}
    else:
        live = fetch_live(os.getenv("GITHUB_TOKEN"))
    merged = {**cache, **{k: v for k, v in live.items() if v is not None}}
    if live and not args.data:
        CACHE.write_text(json.dumps(merged, indent=1, sort_keys=True) + "\n")
    merged["synced_at"] = dt.datetime.now(TZ).strftime("%Y-%m-%d %H:%M") if live else merged.get("synced_at", PH)
    return merged


# --------------------------------------------------------------------------
# helpers on data
# --------------------------------------------------------------------------
def ago(iso: str | None) -> str:
    if not iso:
        return PH
    t = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    s = (dt.datetime.now(dt.timezone.utc) - t).total_seconds()
    for unit, sec in (("y", 31536000), ("mo", 2592000), ("d", 86400), ("h", 3600), ("m", 60)):
        if s >= sec:
            return f"{int(s // sec)}{unit} ago"
    return "just now"


def uptime(iso: str | None) -> str:
    if not iso:
        return PH
    a = dt.datetime.fromisoformat(iso.replace("Z", "+00:00")).date()
    b = dt.date.today()
    y = b.year - a.year - ((b.month, b.day) < (a.month, a.day))
    m = (b.month - a.month - (b.day < a.day)) % 12
    anchor = dt.date(a.year + y + (a.month + m - 1) // 12, (a.month + m - 1) % 12 + 1, 1)
    d = (b - anchor.replace(day=min(a.day, 28))).days
    return f"{y}y {m}mo {max(d, 0)}d"


def streaks(cal):
    if not cal:
        return None, None, None
    counts = [c for _, c in cal]
    longest = run = 0
    for c in counts:
        run = run + 1 if c else 0
        longest = max(longest, run)
    cur, i = 0, len(counts) - 1
    if counts and counts[-1] == 0:
        i -= 1                     # today not done yet; streak still alive
    while i >= 0 and counts[i]:
        cur += 1
        i -= 1
    best = max(cal, key=lambda dc: dc[1])
    return cur, longest, best


# --------------------------------------------------------------------------
# panels
# --------------------------------------------------------------------------
P = f"{CFG['alias']}@{CFG['host']}"


def prompt(cmd: str):
    return [(P, "green"), (":", "fg"), ("~", "blue"), ("$ ", "fg"), (cmd, "fg")]


BANNER = [
    '            ███████╗██╗  ██╗██████╗ ███████╗███████╗███████╗██╗  ██╗',
    '            ██╔════╝██║  ██║██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║',
    '            ███████╗███████║██████╔╝█████╗  █████╗  ███████╗███████║',
    '            ╚════██║██╔══██║██╔══██╗██╔══╝  ██╔══╝  ╚════██║██╔══██║',
    '            ███████║██║  ██║██║  ██║███████╗███████╗███████║██║  ██║',
    '            ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝',
]
CHIP_TEXT = [
    '███████╗██╗  ██╗',
    '██╔════╝██║  ██║',
    '███████╗███████║',
    '╚════██║██╔══██║',
    '███████║██║  ██║',
    '╚══════╝╚═╝  ╚═╝',
]


def header(d):
    def build():
        t = Term(80, f"{P}: ~ · zsh")
        t.line(prompt("./boot --profile"), at=0.2, typed=0.045)
        clock = 1.15
        for lvl, msg in CFG["boot"]:
            c = "green" if lvl == "OK" else "yellow"
            t.line([("[", "dim"), (f"{lvl:^6}", c), ("] ", "dim"), (msg, "fg")], at=clock)
            clock += 0.22
        live = (f"synced github: {fmt(d.get('repos'))} repos · {fmt(d.get('stars'))} stars · "
                f"{fmt(d.get('contrib_total'))} contributions this year")
        t.line([("[", "dim"), ("  OK  ", "green"), ("] ", "dim"), (live, "cyan")], at=clock)
        clock += 0.4
        t.blank()
        grad = lambda th: [th["cyan"], th["blue"], th["magenta"]]  # noqa: E731
        for i, row in enumerate(BANNER):
            b = clock + i * 0.09
            t.line([(row, "cyan", lambda th, i=i: shimmer(grad(th), 5.0, 2 + i * 0.25))], at=b, dur=0.15)
        clock += len(BANNER) * 0.09 + 0.3
        t.blank()
        t.line([("  " + CFG["tagline"], "mute")], at=clock, typed=0.012)
        clock += len(CFG["tagline"]) * 0.012 + 0.3
        t.blank()
        t.line(prompt("echo $ROLE"), at=clock, typed=0.05)
        clock += 0.7
        role_row = t.line([])
        t.blank()
        _roles(t, role_row, clock)
        return t
    save("header", build)


def _roles(t: Term, row: int, start: float, per_char=0.05, hold=1.6, erase=0.02):
    """Type each role, hold, erase, next. Loops forever. One cursor follows."""
    roles = CFG["roles"]
    x0 = t.x(2)
    # build a global timeline
    frames: list[tuple[float, int, int]] = []   # (time, role index, visible chars)
    tt = 0.0
    for i, r in enumerate(roles):
        for k in range(len(r) + 1):
            frames.append((tt, i, k)); tt += per_char
        tt += hold
        for k in range(len(r) - 1, -1, -1):
            frames.append((tt, i, k)); tt += erase
        tt += 0.25
    total = tt

    def kt(ts):
        return ";".join(f"{x / total:.5f}" for x in ts)

    clips = []
    for i, r in enumerate(roles):
        cid = t.uid("r")
        ts, ws = [0.0], [0.0]
        for (f, j, k) in frames:
            if j == i:
                ts.append(f); ws.append(k * CW)
        if ts[1] == 0.0:
            ts, ws = ts[1:], ws[1:]
        t.defs.append(
            f'<clipPath id="{cid}"><rect x="{x0 - 1:.1f}" y="{t.ytop(row) - 2}" width="0" height="{LH}">'
            f'<animate attributeName="width" values="{";".join(f"{w:.1f}" for w in ws)}" keyTimes="{kt(ts)}" '
            f'calcMode="discrete" dur="{total:.2f}s" begin="{start}s" repeatCount="indefinite"/></rect></clipPath>')
        clips.append((cid, r))
    cur_t = [f for f, _, _ in frames]
    cur_x = [x0 + k * CW for _, _, k in frames]

    def over(th):
        s = [f'<text x="{t.x(0):.1f}" y="{t.y(row):.1f}" fill="{th["magenta"]}">&gt;</text>']
        for cid, r in clips:
            s.append(f'<g clip-path="url(#{cid})">{Term.text(x0, t.y(row), r, th["yellow"])}</g>')
        s.append(
            f'<rect x="{x0:.1f}" y="{t.ytop(row):.1f}" width="{CW:.1f}" height="{LH - 4}" fill="{th["fg"]}" opacity="0">'
            f'<set attributeName="opacity" to="1" begin="{start}s"/>'
            f'<animate attributeName="x" values="{";".join(f"{v:.1f}" for v in cur_x)}" keyTimes="{kt(cur_t)}" '
            f'calcMode="discrete" dur="{total:.2f}s" begin="{start}s" repeatCount="indefinite"/></rect>'
            f'<rect x="{x0:.1f}" y="{t.ytop(row):.1f}" width="{CW:.1f}" height="{LH - 4}" fill="{th["bg"]}" opacity="0">'
            f'<animate attributeName="opacity" values="0;0.55" keyTimes="0;0.5" calcMode="discrete" dur="0.9s" '
            f'begin="{start}s" repeatCount="indefinite"/>'
            f'<animate attributeName="x" values="{";".join(f"{v:.1f}" for v in cur_x)}" keyTimes="{kt(cur_t)}" '
            f'calcMode="discrete" dur="{total:.2f}s" begin="{start}s" repeatCount="indefinite"/></rect>')
        return "".join(s)
    t.over.append(over)


def chip_rows():
    inner = 22
    w = inner + 2
    pins = [i for i in range(2, w - 2, 2)]
    pin_line = "".join("│" if i in pins else " " for i in range(w))
    top = "┌" + "".join("┴" if i in pins else "─" for i in range(1, w - 1)) + "┐"
    bot = "└" + "".join("┬" if i in pins else "─" for i in range(1, w - 1)) + "┘"
    label = "sh-1 · rev 2026"
    content = [""] + [c.center(inner) for c in CHIP_TEXT] + ["", label.center(inner), ""]
    rows = [("  " + pin_line, "pins_top"), ("  " + top, "edge")]
    for i, c in enumerate(content):
        side = "──┤" if i % 2 else "  │"
        rside = "├──" if i % 2 else "│  "
        rows.append((side, c.ljust(inner), rside, i))
    rows += [("  " + bot, "edge"), ("  " + pin_line, "pins_bot")]
    return rows, pins


def neofetch(d):
    def build():
        t = Term(88, f"{P}: ~ · neofetch")
        t.line(prompt("neofetch --live"), at=0.2, typed=0.05)
        t.blank()
        L = 32                          # info column start
        info: list[list] = [
            [(P, "green")],
            [("─" * len(P), "dim")],
        ]
        for k, v in CFG["neofetch"]:
            info.append([(f"{k:<8}", "blue"), (v, "fg")])
        info.append([])
        info.append([("── github ", "dim"), ("live", "green"), (" " + "─" * 37, "dim")])
        W = 54
        cur, longest, best = streaks(d.get("calendar"))
        info += [
            dots("uptime", uptime(d.get("created_at")), W),
            dots("repos", f"{fmt(d.get('repos'))} · contributed to {fmt(d.get('contributed_to'))}", W),
            dots("stars", f"{fmt(d.get('stars'))} · followers {fmt(d.get('followers'))}", W),
            dots(f"commits {dt.date.today().year}", fmt(d.get("commits_ytd")), W),
            dots("prs merged", fmt(d.get("prs_merged")), W),
            dots("streak", f"{fmt(cur)}d now · {fmt(longest)}d best", W),
        ]
        info.append([])
        langs = d.get("languages") or []
        lang_rows = []
        for name, frac in langs[:5]:
            lang_rows.append(len(info))
            info.append([(f"{name[:12]:<12}", "fg"), ("░" * 30, "dim"), (f" {frac * 100:5.1f}%", "mute")])
        if not langs:
            info.append([("languages", "fg"), (f" {PH}", "mute")])
        info.append([])
        info.append([("sync ", "dim"), (f"{d.get('synced_at', PH)} IST", "mute"), (" · auto-updates every 6h", "dim")])

        chip, pins = chip_rows()
        n = max(len(chip), len(info))
        base = len(t.rows)
        clock = 1.0
        for i in range(n):
            spans: list = []
            if i < len(chip):
                c = chip[i]
                if len(c) == 2:
                    txt, kind = c
                    if kind.startswith("pins"):
                        for j, ch in enumerate(txt[2:]):
                            if ch == "│":
                                k = pins.index(j)
                                delay = k * 0.12 + (0 if kind == "pins_top" else 0.6)
                                spans.append((ch, "dim", lambda th, delay=delay: (
                                    f'<animate attributeName="fill" values="{th["dim"]};{th["green"]};{th["dim"]}" '
                                    f'keyTimes="0;0.08;0.3" dur="2.4s" begin="{2 + delay:.2f}s" repeatCount="indefinite"/>')))
                            else:
                                spans.append((ch, "dim"))
                        spans.insert(0, ("  ", "dim"))
                    else:
                        spans.append((txt, "mute"))
                else:
                    lpad, mid, rpad, idx = c
                    spans.append((lpad, "mute"))
                    spans.append((mid, "magenta" if idx in range(1, 7) else "dim",
                                  (lambda th, idx=idx: shimmer([th["cyan"], th["blue"], th["magenta"]], 5, idx * 0.2))
                                  if idx in range(1, 7) else ""))
                    spans.append((rpad, "mute"))
            used = sum(len(s[0]) for s in spans)
            if i < len(info) and info[i]:
                spans.append((" " * (L - used), "fg"))
                spans += info[i]
            t.line(spans, at=clock, dur=0.2)
            clock += 0.07
        # animated language bars (fill grows over the ░ track)
        for k, ri in enumerate(lang_rows):
            name, frac = langs[k]
            row = base + ri
            full = max(1, round(frac * 30))
            cid = t.uid("lb")
            begin = 1.0 + ri * 0.07 + 0.4
            x = t.x(L + 12)
            t.defs.append(
                f'<clipPath id="{cid}"><rect x="{x:.1f}" y="{t.ytop(row) - 2}" width="0" height="{LH}">'
                f'<animate attributeName="width" from="0" to="{full * CW:.1f}" begin="{begin:.2f}s" dur="0.9s" '
                f'fill="freeze" calcMode="spline" keySplines="0.2 0.7 0.3 1" keyTimes="0;1"/></rect></clipPath>')
            t.over.append(lambda th, cid=cid, row=row, x=x, full=full, k=k: (
                f'<g clip-path="url(#{cid})">'
                + Term.text(x, t.y(row), "█" * full, [th["cyan"], th["blue"], th["magenta"], th["green"], th["orange"]][k])
                + "</g>"))
        t.blank()
        sw = ["red", "orange", "yellow", "green", "cyan", "blue", "magenta", "fg"]
        t.line([(" " * L, "fg")] + sum([[("███", c), (" ", "fg")] for c in sw], []), at=clock + 0.1)
        return t
    save("neofetch", build)


def activity(d):
    cal = d.get("calendar") or []

    def build():
        t = Term(112, f"{P}: ~ · contributions")
        t.line(prompt("git log --since='1 year ago' --format=heatmap"), at=0.2, typed=0.035)
        t.blank()
        days = [(dt.date.fromisoformat(a), c) for a, c in cal]
        if days:
            pad = (days[0][0].weekday() + 1) % 7          # grid columns start on Sunday
            days = [(None, -1)] * pad + days
        weeks = [days[i:i + 7] for i in range(0, len(days), 7)][-53:]
        mx = max([c for _, c in days if c > 0] or [1])

        def level(c):
            if c < 0:
                return -1
            if c == 0:
                return 0
            q = c / mx
            return 1 if q <= .25 else 2 if q <= .5 else 3 if q <= .75 else 4
        chars = ["·", "░", "▒", "▓", "█"]
        mrow = [" "] * (5 + max(len(weeks), 1) * 2)
        last = None
        for wi, w in enumerate(weeks):
            dd = next((x for x, _ in w if x), None)
            if dd and dd.month != last and dd.day <= 7:
                p = 5 + wi * 2
                if p + 3 <= len(mrow):
                    mrow[p:p + 3] = list(dd.strftime("%b").lower())
                last = dd.month
        t.line([("".join(mrow), "mute")], at=0.9)
        cid = t.uid("sw")
        grid_top = len(t.rows)
        names = ["", "mon", "", "wed", "", "fri", ""]
        labels, cells = [], []
        for dow in range(7):
            r = t.line([])                       # reserve the row; cells drawn individually below
            labels.append((r, [(names[dow], "mute")]))
            for wi, w in enumerate(weeks):
                lv = level(w[dow][1]) if dow < len(w) else -1
                if lv >= 0:
                    cells.append((r, wi, lv))
        # one glyph per cell, centred on its own column: no stretching, rows stay on the grid
        t.over.append(lambda th: f'<g clip-path="url(#{cid})">' + "".join(
            f'<text x="{t.x(5 + wi * 2) + CW / 2:.1f}" y="{t.y(r):.1f}" fill="{th[f"h{lv}"]}" '
            f'text-anchor="middle">{chars[lv]}</text>' for r, wi, lv in cells) + "</g>")
        if not weeks:
            t.line([(f"     no data yet {PH} the action fills this in on its first run", "mute")])
        t.blank()
        cur, longest, best = streaks(cal)
        bestd = f"{best[1]} on {best[0]}" if best else PH
        t.line([("total ", "mute"), (fmt(d.get("contrib_total")), "cyan"), ("  ·  current streak ", "mute"),
                (f"{fmt(cur)}d", "green"), ("  ·  longest ", "mute"), (f"{fmt(longest)}d", "yellow"),
                ("  ·  best day ", "mute"), (bestd, "magenta")], at=2.4)
        t.line([("less ", "mute"), ("· ", "h0"), ("░ ", "h1"), ("▒ ", "h2"), ("▓ ", "h3"), ("█ ", "h4"),
                ("more", "mute")], at=2.6)
        gx, gw = t.x(5), max(len(weeks), 1) * 2 * CW
        gy, gh_ = t.ytop(grid_top) - 2, 7 * LH + 2
        t.defs.append(f'<clipPath id="{cid}"><rect x="{gx - 1:.1f}" y="{gy:.1f}" width="0" height="{gh_}">'
                      f'<animate attributeName="width" from="0" to="{gw + 2:.1f}" begin="0.9s" dur="1.4s" '
                      f'fill="freeze"/></rect></clipPath>')
        t.over.append(lambda th: '<g opacity="0">' + "".join(t.render_row(r, sp, th) for r, sp in labels)
                      + '<animate attributeName="opacity" from="0" to="1" begin="0.9s" dur="0.3s" fill="freeze"/></g>')
        t.over.append(lambda th: (
            f'<rect x="{gx:.1f}" y="{gy:.1f}" width="{2 * CW:.1f}" height="{gh_}" fill="{th["scan"]}" opacity="0">'
            f'<set attributeName="opacity" to="0.10" begin="2.4s"/>'
            f'<animate attributeName="x" from="{gx:.1f}" to="{gx + gw - 2 * CW:.1f}" begin="2.4s" dur="5s" '
            f'repeatCount="indefinite"/></rect>'))
        return t

    for theme, th in THEMES.items():
        th2 = dict(th, **{f"h{i}": c for i, c in enumerate(th["heat"])})
        ASSETS.mkdir(exist_ok=True)
        (ASSETS / f"activity-{theme}.svg").write_text(build().svg(th2), encoding="utf-8")


def project_card(p, d, rows_total):
    meta = (d.get("featured") or {}).get(p["repo"]) or {}

    def build():
        W = 48
        t = Term(W, chrome=False)
        stars = f" ★ {fmt(meta.get('stars'))} "
        pre = [("┌", "dim"), ("─[", "dim"), (p["id"], "yellow"), ("]─ ", "dim"), (p["name"], "cyan"), (" ", "dim")]
        used = sum(len(x[0]) for x in pre)
        t.line(pre + [("─" * (W - used - len(stars) - 2), "dim"), (stars, "yellow"), ("─┐", "dim")],
               at=0.1, typed=0.012)
        body: list[list] = [
            [(p["subtitle"], "fg")],
            [(p["stack"], "mute")],
            [],
        ]
        for pt in p["points"]:
            body.append([("› ", "green"), (pt, "fg")])
        bars = p.get("bars") or []
        if bars:
            body.append([])
        bar_rows = []
        for lab, frac, val in bars:
            bar_rows.append((len(body), frac, lab))
            body.append([(f"{lab:<9}", "mute"), ("░" * 26, "dim"), (f" {val}", "yellow" if frac >= 1 else "mute")])
        while len(body) < rows_total:
            body.append([])
        active = False
        if meta.get("pushed"):
            age = dt.datetime.now(dt.timezone.utc) - dt.datetime.fromisoformat(meta["pushed"].replace("Z", "+00:00"))
            active = age.days < 7
        lic = meta.get("license") or ""
        status = [("● ", "green" if active else "dim", (lambda th: blink(th, 1.4)) if active else ""),
                  (f"{meta.get('lang') or PH}", "fg"), ("  pushed ", "mute"), (ago(meta.get("pushed")), "cyan")]
        if lic and lic != "NOASSERTION":
            status += [("  ", "fg"), (lic, "mute")]
        body.append(status)
        for i, b in enumerate(body):
            used = sum(len(s[0]) for s in b)
            t.line([("│ ", "dim")] + b + [(" " * (W - 3 - used), "fg"), ("│", "dim")], at=0.3 + i * 0.05, dur=0.15)
        t.line([("└" + "─" * (W - 2) + "┘", "dim")], at=0.3 + len(body) * 0.05)
        for ri, frac, lab in bar_rows:
            row = 1 + ri
            cid = t.uid("pb")
            x = t.x(2 + 9)
            full = max(1, round(26 * frac))
            t.defs.append(f'<clipPath id="{cid}"><rect x="{x:.1f}" y="{t.ytop(row) - 2}" width="0" height="{LH}">'
                          f'<animate attributeName="width" from="0" to="{full * CW:.1f}" begin="1.2s" '
                          f'dur="{0.6 + 1.6 * frac:.2f}s" fill="freeze"/></rect></clipPath>')
            t.over.append(lambda th, cid=cid, row=row, x=x, full=full, frac=frac: (
                f'<g clip-path="url(#{cid})">'
                + Term.text(x, t.y(row), "█" * full, th["yellow"] if frac >= 1 else th["mute"]) + "</g>"))
        # crt scanline
        t.over.append(lambda th: (
            f'<rect x="1" y="0" width="{t.width - 2:.0f}" height="3" fill="{th["scan"]}" opacity="0.07">'
            f'<animate attributeName="y" from="0" to="{t.height:.0f}" dur="4.5s" repeatCount="indefinite"/></rect>'))
        return t
    save(f"project-{p['id']}", build)


def projects(d):
    rows = max(3 + len(p["points"]) + (len(p.get("bars") or []) + 1 if p.get("bars") else 0)
               for p in CFG["projects"])
    for p in CFG["projects"]:
        project_card(p, d, rows)


def career(_d):
    def build():
        t = Term(80, f"{P}: ~ · git")
        t.line(prompt("git log --graph --career"), at=0.2, typed=0.05)
        t.blank()
        clock = 1.2
        n = len(CFG["career"])
        for i, c in enumerate(CFG["career"]):
            ref = [(" (", "yellow"), (c["ref"], "cyan" if "HEAD" in c["ref"] else "yellow"), (")", "yellow")] \
                if c["ref"] else []
            head = [("* ", "red"), (c["hash"], "yellow")] + ref + [(" " + c["title"], "fg")]
            used = sum(len(s[0]) for s in head)
            head.append((" " * max(1, 80 - used - len(c["when"])), "fg"))
            head.append((c["when"], "mute"))
            t.line(head, at=clock); clock += 0.12
            bar = "│ " if i < n - 1 else "  "
            t.line([(bar, "red"), ("  " + c["sub"], "mute")], at=clock); clock += 0.08
            for j, pt in enumerate(c["points"]):
                br = "└─ " if j == len(c["points"]) - 1 else "├─ "
                t.line([(bar, "red"), ("  " + br, "dim"), (pt, "fg")], at=clock); clock += 0.08
            if i < n - 1:
                t.line([("│", "red")], at=clock); clock += 0.05
        return t
    save("career", build)


def prs(d):
    items = d.get("prs") or []

    def build():
        t = Term(88, f"{P}: ~ · gh")
        t.line(prompt("gh search prs --author=@me --upstream"), at=0.2, typed=0.04)
        t.blank()
        t.line([("STATE      REPO                              PR       TITLE", "mute")], at=1.9)
        t.line([("─" * 88, "dim")], at=1.9)
        clock = 2.1
        if not items:
            t.line([(f"  waiting for first sync {PH}", "mute")], at=clock)
        spinner_rows = []
        for it in items:
            repo, num = it["key"].split("#")
            st = it["state"]
            colour = {"merged": "magenta", "open": "green"}.get(st, "red")
            icon = {"merged": "[+]", "open": "[ ]", "closed": "[x]"}.get(st, "[?]")
            title = it["title"]
            room = 88 - 11 - 34 - 9
            if len(title) > room:
                title = title[: room - 1] + "…"
            r = t.line([(icon, colour), (f" {st:<7}", colour), (f"{repo[:32]:<34}", "fg"),
                        (f"#{num:<8}", "yellow"), (title, "mute")], at=clock)
            if st == "open":
                spinner_rows.append(r)
            clock += 0.12
        t.blank()
        tot = d.get("upstream_total")
        t.line([("showing ", "dim"), (str(len(items)), "cyan"), (" of ", "dim"), (fmt(tot), "cyan"),
                (" upstream PRs · ", "dim"), ("[+] merged  [|] open  [x] closed", "mute")], at=clock + 0.2)

        def spin(th):
            out = []
            for r in spinner_rows:
                x, y = t.x(1), t.y(r)
                out.append(f'<rect x="{x - 1:.1f}" y="{t.ytop(r):.1f}" width="{CW + 2:.1f}" height="{LH - 4}" fill="{th["bg"]}"/>')
                for k, ch in enumerate("|/-\\"):
                    out.append(f'<text x="{x:.1f}" y="{y:.1f}" fill="{th["green"]}" opacity="0">{escape(ch)}'
                               f'<animate attributeName="opacity" values="{";".join("1" if j == k else "0" for j in range(4))}" '
                               f'keyTimes="0;0.25;0.5;0.75" calcMode="discrete" dur="0.8s" begin="{clock:.2f}s" '
                               f'repeatCount="indefinite"/></text>')
            return "".join(out)
        t.over.append(spin)
        return t
    save("prs", build)


def stack(_d):
    def build():
        t = Term(80, f"{P}: ~ · tree")
        t.line(prompt("tree ~/stack"), at=0.2, typed=0.05)
        t.blank()
        t.line([("~/stack", "blue")], at=1.0)
        clock = 1.1
        items = CFG["stack"]
        tools = 0
        for i, (k, v) in enumerate(items):
            br = "└── " if i == len(items) - 1 else "├── "
            t.line([(br, "dim"), (f"{k:<10}", "green"), (v, "fg")], at=clock)
            tools += len([x for x in v.split("·") if x.strip()])
            clock += 0.07
        t.blank()
        t.line([(f"{len(items)} directories, {tools} tools", "mute")], at=clock); clock += 0.4
        t.blank()
        t.line(prompt("tail /var/log/honors.log"), at=clock, typed=0.04); clock += 1.1
        t.blank()
        wmax = max(len(w) for _, w, _ in CFG["honors"])
        for y, what, note in CFG["honors"]:
            dots_n = max(2, min(wmax + 4 - len(what), 80 - 8 - len(what) - len(note)))
            t.line([("[", "dim"), (y, "yellow"), ("] ", "dim"), (what + " ", "fg"), ("." * dots_n, "dim"),
                    (" " + note, "cyan")], at=clock)
            clock += 0.1
        return t
    save("stack", build)


def footer(d):
    def build():
        t = Term(88, f"{P}: ~")
        t.line(prompt("uptime"), at=0.2, typed=0.06)
        t.line([(" up ", "mute"), (uptime(d.get("created_at")), "cyan"), (" on github · last sync ", "mute"),
                (f"{d.get('synced_at', PH)} IST", "green"), (" · rebuilds every 6h", "mute")], at=0.8)
        t.line(prompt("exit"), at=1.5, typed=0.08)
        t.line([("logout · connection closed. ship something today.", "mute")], at=2.1)
        r = t.line(prompt(""), at=2.6)
        t.over.append(lambda th: (
            f'<rect x="{t.x(len(P) + 4):.1f}" y="{t.ytop(r):.1f}" width="{CW:.1f}" height="{LH - 4}" '
            f'fill="{th["fg"]}" opacity="0"><set attributeName="opacity" to="1" begin="2.6s"/>'
            f'<animate attributeName="opacity" values="1;0" keyTimes="0;0.5" calcMode="discrete" dur="1s" '
            f'begin="2.6s" repeatCount="indefinite"/></rect>'))
        return t
    save("footer", build)


# --------------------------------------------------------------------------
# README sections between markers
# --------------------------------------------------------------------------
def replace_block(text: str, name: str, content: str) -> str:
    pat = re.compile(rf"(<!--{name}:START-->)(.*?)(<!--{name}:END-->)", re.S)
    return pat.sub(lambda m: f"{m.group(1)}\n{content}\n{m.group(3)}", text)


def update_readme(d):
    if not README.exists():
        return
    txt = README.read_text(encoding="utf-8")
    items = d.get("prs") or []
    links = " &nbsp;·&nbsp; ".join(f'<a href="{it["url"]}"><code>{escape(it["key"])}</code></a>' for it in items)
    txt = replace_block(txt, "UPSTREAM", f'<p align="center"><sub>{links or "syncing…"}</sub></p>')
    txt = replace_block(txt, "SYNC", f'<sub>last sync {d.get("synced_at", PH)} IST</sub>')
    README.write_text(txt, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data")
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    d = load_data(args)
    for fn in (header, neofetch, activity, projects, career, prs, stack, footer):
        fn(d)
    if not args.data:
        update_readme(d)
    print(f"built {len(list(ASSETS.glob('*.svg')))} svgs · synced_at={d.get('synced_at')}")


if __name__ == "__main__":
    main()
