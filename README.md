<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a2942,100:58a6ff&height=140&section=header&text=Sreesanth%20R&fontSize=40&fontColor=ffffff&fontAlignY=45&desc=Backend%20%26%20Systems%20Engineer&descAlignY=68&descSize=16&descColor=8b949e&animation=fadeIn" width="100%" />

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&duration=3000&pause=800&color=58A6FF&center=true&vCenter=true&width=700&lines=Go+%7C+Python+%7C+TypeScript+%7C+C%2B%2B;gRPC+Microservices+%7C+AI+Inference+%7C+GPU+Infrastructure;Building+systems+that+scale" alt="Typing SVG" />

<br/>

![Profile Views](https://komarev.com/ghpvc/?username=Shreesh-Sree&style=flat-square&color=58a6ff&label=Profile+Views)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/sree-santh)
[![Portfolio](https://img.shields.io/badge/Portfolio-shreesh--sree.dev-0f172a?style=flat-square&logo=vercel&logoColor=white)](https://shreesh-sree.dev)
[![Codolio](https://img.shields.io/badge/Codolio-6c47ff?style=flat-square)](https://codolio.com/profile/shreesh-22)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:shreesh.exe22@gmail.com)

</div>

---

### About

Backend and systems engineer based in Chennai, India. I work primarily in **Go**, **Python**, and **TypeScript** — building gRPC microservices, AI inference pipelines, and bare-metal GPU infrastructure.

I work close to the metal: patching llama.cpp at the C++ level for speculative decoding, tuning NUMA topology and hugepages on dual-EPYC servers, building agentic AI systems that run in production.

- B.Tech in AI & ML at **St. Joseph's College of Engineering** (Anna University) · CGPA 8.40 · Expected 2028
- **Databricks Student Fellow APJ 2026** — 1 of 38 selected from 7,171 global applicants
- SWE Intern at **Presidio Inc.** (PRIME program — 1 of 15 from 2,000+ applicants)
- AI Research Intern at **Indian Institute of Technology Jammu**
- Technical Lead, HackerRank Campus Crew · Campus Leader, AWS Student Builder Group · Technical Coordinator, GDG SJCE

---

### Languages

<div align="center">

<img src="https://skillicons.dev/icons?i=go,python,ts,cpp" />

</div>

---

### Stack

<div align="center">

**Backend**

<img src="https://skillicons.dev/icons?i=fastapi,nodejs,react,nextjs,express" />

**Infrastructure**

<img src="https://skillicons.dev/icons?i=postgres,redis,docker,kubernetes,terraform,aws,azure,linux" />

**AI / ML**

<img src="https://skillicons.dev/icons?i=pytorch,opencv" />

&nbsp;
![vLLM](https://img.shields.io/badge/vLLM-412991?style=flat-square)
![NVIDIA NIM](https://img.shields.io/badge/NVIDIA_NIM-76B900?style=flat-square&logo=nvidia&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square)
![llama.cpp](https://img.shields.io/badge/llama.cpp-000000?style=flat-square)
![gRPC](https://img.shields.io/badge/gRPC-4285F4?style=flat-square&logo=google&logoColor=white)
![RAG](https://img.shields.io/badge/RAG_Pipelines-6c47ff?style=flat-square)
![Traefik](https://img.shields.io/badge/Traefik-24A1C1?style=flat-square&logo=traefikproxy&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white)
![Slurm](https://img.shields.io/badge/Slurm-1a7abf?style=flat-square)
![MCP](https://img.shields.io/badge/MCP-FF6B35?style=flat-square)

</div>

---

### Projects

**[AetherCode](https://github.com/Shreesh-Sree/Aethercode-main)** — Multi-tenant coding assessment platform
`Go` `gRPC` `PostgreSQL` `Casbin` `Kubernetes`
Isolated execution per tenant. gRPC microservices, Casbin RBAC with short-lived HMAC capabilities, PostgreSQL row-level security, Judge0 isolated behind a completion-only bridge.

---

**FastMTP** — Speculative decoding patch for llama.cpp
`C++` `GGML` `CUDA`
Patched qwen35/qwen35moe with d2t draft-vocabulary trimming and logit scattering. Throughput: **44.5 to 113.9 tok/s** (~2.5x) on RTX Pro 6000 Blackwell. Branch: [feat/fastmtp-ollama](https://github.com/Shreesh-Sree/llama.cpp/tree/feat/fastmtp-ollama)

---

**[Blackwell GPU Slicing](https://github.com/Shreesh-Sree/blackwell-gpu-slicing)** — Bare-metal multi-tenant GPU allocation
`Slurm` `NVIDIA MPS` `NVIDIA MIG` `CUDA`
Dynamic MPS/MIG resource management on Dual AMD EPYC 9554 (256 threads) + Dual RTX Pro 6000 Blackwell 96GB. Prolog/epilog hooks for instant VRAM reclaim on job exit.

---

**[Enterprise Edge Architecture](https://github.com/Shreesh-Sree/Server-Cloudflare-Architecture)** — Zero-trust production edge
`Traefik` `Cloudflare Tunnels` `Zitadel SSO` `Prometheus` `Grafana`
Zero-open-port edge across 15+ institutional microservices. Reverse proxy, dynamic TLS, Cloudflare tunnels, OIDC SSO, full Prometheus/Grafana observability.

---

**VeraQX** — Hackathon: citation-grounded triage agent in 24 hours
`Go` `Hybrid RAG` `Okapi BM25` `RRF`
Terminal-based agent fusing BM25 keyword search and vector search via Reciprocal Rank Fusion for precision-ranked, source-attributed answers.

---

**Reimbursement Tool** — Presidio intern capstone
`FastAPI` `React` `PostgreSQL` `Supabase` `Terraform` `Azure`
Multi-tenant expense platform with tenant-scoped RBAC, multi-level approval workflows, and complete audit logging.

---

**[LearnHouse](https://github.com/learnhouse/learnhouse)** — Open source contributor
`FastAPI` `Python` `SQLModel` `PostgreSQL`
Extending the backend of an AGPL-3.0 learning platform. Currently integrating Safe Exam Browser (SEB) support for locked-down, proctored assessment delivery.

---

### GitHub Stats

<div align="center">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Shreesh-Sree&theme=github_dark" width="100%" />

<br/>

<table>
<tr>
<td>
<img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=Shreesh-Sree&theme=github_dark" />
</td>
<td>
<img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Shreesh-Sree&theme=github_dark" />
</td>
<td>
<img src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=Shreesh-Sree&theme=github_dark" />
</td>
</tr>
<tr>
<td>
<img src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=Shreesh-Sree&theme=github_dark" />
</td>
<td colspan="2">
<img src="https://streak-stats.demolab.com/?user=Shreesh-Sree&theme=github-dark-blue&hide_border=true&background=1B2027&stroke=30363D&ring=58a6ff&fire=ff7b72&currStreakNum=c9d1d9&sideNums=c9d1d9&currStreakLabel=58a6ff&sideLabels=8b949e&dates=8b949e" />
</td>
</tr>
</table>

<br/>

<img src="https://github-trophies.vercel.app/?username=Shreesh-Sree&theme=onestar&no-frame=true&no-bg=true&margin-w=6&row=2&column=4" width="100%" />

<br/>

<img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=dark" width="100%" />

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:58a6ff,50:1a2942,100:0d1117&height=100&section=footer&animation=fadeIn" width="100%" />
