<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=28&duration=3000&pause=1000&color=58A6FF&center=true&vCenter=true&width=600&lines=Hey%2C+I'm+Sreesanth+%F0%9F%91%8B;Backend+%26+Systems+Engineer;Go+%7C+Python+%7C+TypeScript;Building+things+that+scale" alt="Typing SVG"/>

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/sree-santh)
[![Portfolio](https://img.shields.io/badge/Portfolio-shreesh--sree.dev-0f172a?style=flat-square&logo=vercel&logoColor=white)](https://shreesh-sree.dev)
[![Codolio](https://img.shields.io/badge/Codolio-shreesh--22-6c47ff?style=flat-square&logo=codeforces&logoColor=white)](https://codolio.com/profile/shreesh-22)
[![Email](https://img.shields.io/badge/shreesh.exe22@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:shreesh.exe22@gmail.com)

</div>

---

### About Me

I'm a backend & systems engineer based in Chennai, India. I spend most of my time writing **Go**, **Python**, and **TypeScript** — building things from gRPC microservices and AI inference pipelines to bare-metal GPU infrastructure.

I enjoy working close to the metal. I've patched **llama.cpp** at the C++ level for speculative decoding throughput, tuned NUMA topology and hugepages on dual-EPYC servers, and shipped agentic AI systems that actually run in production.

When I'm not writing backend code, I'm contributing to open source, running coding events as a **HackerRank Campus Crew Technical Lead**, or figuring out how to make LLMs go faster.

- 🎓 B.Tech in AI & ML @ **St. Joseph's College of Engineering** (Anna University) · CGPA **8.40** · 2028
- 🏅 **Databricks Student Fellow APJ 2026** — 1 of 38 selected from 7,171 global applicants
- 🛠 Interned at **Presidio Inc.** (PRIME SWE, 1-of-15 from 2000+ applicants) & **IIT Jammu** (AI Research)
- 📍 Chennai, India · Open to Backend, AI Systems & Infrastructure roles

---

### Tech Stack

**Languages I work in daily**

![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=c%2B%2B&logoColor=white)

**Backend**

![Gin](https://img.shields.io/badge/Gin-00ADD8?style=flat-square&logo=go&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=node.js&logoColor=white)
![gRPC](https://img.shields.io/badge/gRPC-4285F4?style=flat-square&logo=google&logoColor=white)
![BullMQ](https://img.shields.io/badge/BullMQ-FF0000?style=flat-square&logo=redis&logoColor=white)

**Data & Infrastructure**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-844FBA?style=flat-square&logo=terraform&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white)
![Traefik](https://img.shields.io/badge/Traefik-24A1C1?style=flat-square&logo=traefikproxy&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white)

**AI / ML**

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![vLLM](https://img.shields.io/badge/vLLM-412991?style=flat-square)
![NVIDIA NIM](https://img.shields.io/badge/NVIDIA_NIM-76B900?style=flat-square&logo=nvidia&logoColor=white)
![llama.cpp](https://img.shields.io/badge/llama.cpp-000000?style=flat-square)

---

### What I've Built

**[AetherCode](https://github.com/Shreesh-Sree/Aethercode-main)** — Multi-tenant coding assessment platform
Go · gRPC · PostgreSQL · Casbin · Kubernetes
> Fully isolated execution per tenant — gRPC microservices, Casbin RBAC with HMAC capabilities, PostgreSQL row-level security, and Judge0 behind a completion-only bridge.

---

**FastMTP** — Speculative decoding patch for `llama.cpp`
C++ · GGML · CUDA
> Patched the qwen35/qwen35moe architecture with `d2t` draft-vocabulary trimming and logit scattering. Took generation from **44.5 → 113.9 tok/s** (~2.5x) on RTX Pro 6000 Blackwell.

---

**Blackwell GPU Slicing** — Bare-metal multi-tenant GPU allocation
Slurm · NVIDIA MPS · NVIDIA MIG · CUDA
> Dynamic MPS/MIG resource management on Dual AMD EPYC 9554 (256 threads) + Dual RTX Pro 6000 Blackwell 96GB. Prolog/epilog hooks for instant VRAM reclaim on job exit.

---

**VeraQX** — Hackathon: Support triage agent in 24h
Go · Hybrid RAG · Okapi BM25 · RRF
> Terminal-based triage agent that fuses BM25 keyword search + vector search with Reciprocal Rank Fusion. Citation-grounded answers, built in a single hackathon day.

---

**[Reimbursement Tool](https://github.com/Shreesh-Sree/Aethercode-main)** — Presidio intern capstone
FastAPI · React · PostgreSQL · Supabase · Terraform · Azure
> Multi-tenant expense platform with RBAC, multi-level approval workflows, and full audit logging. Built during my internship at Presidio.

---

**[LearnHouse](https://github.com/learnhouse/learnhouse)** — Open source contribution
FastAPI · Python · SQLModel · PostgreSQL
> Extending the backend of an AGPL-3.0 learning platform. Currently landing Safe Exam Browser (SEB) integration for proctored assessment delivery.

---

**Enterprise Edge & Cloudflare Architecture**
Traefik · Cloudflare Tunnels · Zitadel SSO · Grafana
> Zero-open-port production edge across 15+ institutional microservices — reverse proxy, dynamic TLS, Cloudflare tunnels, OIDC SSO, and Prometheus/Grafana observability.

---

### GitHub Stats

<div align="center">

<table border="0">
<tr>
<td valign="top" width="50%">
<img src="https://github-readme-stats.vercel.app/api?username=Shreesh-Sree&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=58a6ff&icon_color=1f6feb&text_color=c9d1d9&count_private=true&include_all_commits=true" width="100%" alt="GitHub Stats"/>
</td>
<td valign="top" width="50%">
<img src="https://github-readme-streak-stats.herokuapp.com/?user=Shreesh-Sree&theme=tokyonight&hide_border=true&background=0d1117&stroke=58a6ff&ring=58a6ff&fire=ff7b72&currStreakNum=c9d1d9&sideNums=c9d1d9&currStreakLabel=58a6ff&sideLabels=58a6ff&dates=8b949e" width="100%" alt="GitHub Streak"/>
</td>
</tr>
</table>

<br/>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Shreesh-Sree&layout=compact&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=58a6ff&text_color=c9d1d9&langs_count=8" alt="Top Languages"/>

</div>

---

<div align="center">
<sub>Chennai, India · <a href="mailto:shreesh.exe22@gmail.com">shreesh.exe22@gmail.com</a> · <a href="https://shreesh-sree.dev">shreesh-sree.dev</a></sub>
</div>
