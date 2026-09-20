# Sreesanth R

**Systems Architect & AI Infrastructure Engineer**  
Chennai, India · Technical Lead @ HackerRank Campus Crew · Systems Lead @ AetherCode

[Website](https://shreesh-sree.dev) &nbsp;·&nbsp; [LinkedIn](https://linkedin.com/in/sree-santh) &nbsp;·&nbsp; [GitHub](https://github.com/Shreesh-Sree) &nbsp;·&nbsp; [Email](mailto:shreesh.exe22@gmail.com) &nbsp;·&nbsp; [Codolio](https://codolio.com/profile/shreesh-22)

---

### Overview

Backend and systems engineer specializing in low-level AI inference optimization, distributed systems architecture, and bare-metal cluster orchestration. Pursuing B.Tech in Artificial Intelligence & Machine Learning at St. Joseph's College of Engineering, Anna University (CGPA 8.40 / 10).

- **Low-Level Inference Engineering**: Author of speculative decoding patches for `llama.cpp` (`FastMTP` draft-vocabulary trimming), achieving up to 2.5x token/s throughput acceleration on NVIDIA Blackwell architectures.
- **Bare-Metal GPU Orchestration**: Architected multi-tenant compute allocation with Slurm, NVIDIA MPS, and dynamic MIG slicing across dual AMD EPYC (256 threads) and dual RTX Pro 6000 Ada/Blackwell nodes.
- **Zero-Trust Distributed Edge**: Deployed production edge architectures spanning 15+ microservices with Traefik, Cloudflare Zero-Trust tunnels, and Zitadel OIDC SSO.
- **Enterprise Engineering**: Former SDE Intern at Presidio (PRIME program, selected 1 of 15 from 2,000+ applicants) and AI Research Intern at IIT Jammu. Databricks Student Fellow APJ 2026 (selected 1 of 38 from 7,171 global applicants).

---

### Core Technical Arsenal

| Domain | Stack & Frameworks |
|:---|:---|
| **Core Languages** | Go, C++, Python, TypeScript, SQL, Bash |
| **Backend & Distributed Systems** | gRPC, Gin, FastAPI, Node.js, Express, BullMQ, WebSockets, REST |
| **AI Systems & Acceleration** | CUDA, `llama.cpp`, GGML, vLLM, NVIDIA NIM, PyTorch, LangGraph, RAG |
| **Compute & Orchestration** | Slurm Workload Manager, NVIDIA MPS / MIG, Docker, Podman, Kubernetes, K3s |
| **Storage & Caching** | PostgreSQL (Row-Level Security, pgvector), Redis, SQLite, ClickHouse |
| **Infrastructure & Security** | Terraform, AWS (ECS, Lambda), Azure, Cloudflare Zero-Trust, Traefik, Zitadel |
| **Observability & Telemetry** | Prometheus, Grafana, OpenTelemetry |

---

### Featured Systems & Architecture

<table>
<tr>
<td width="50%" valign="top">

#### [FastMTP — llama.cpp Speculative Acceleration](https://github.com/Shreesh-Sree/llama.cpp/tree/feat/fastmtp-ollama)
*Upstream C++ optimization for qwen35 / qwen35moe architectures*
- Engineered `d2t` draft-vocabulary tensor trimming and logit scattering kernels, eliminating 152k-dimension speculative overhead.
- Accelerated generation throughput from **44.5 tok/s to 113.9 tok/s (~2.5x)** on RTX Pro 6000 hardware.
- **Stack:** `C++`, `CUDA`, `GGML`, `llama.cpp`

</td>
<td width="50%" valign="top">

#### [AetherCode — Distributed Execution Engine](https://github.com/Shreesh-Sree/Aethercode-main)
*High-throughput multi-tenant code assessment & judge platform*
- Architected Go microservices over strict gRPC contracts with Casbin authorization and PostgreSQL row-level security.
- Integrated Judge0 sandboxed execution behind completion-only worker bridges to prevent cross-tenant data exposure.
- **Stack:** `Go`, `gRPC`, `PostgreSQL`, `Casbin`, `Kubernetes`

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### [Blackwell Dynamic GPU Slicing](https://github.com/Shreesh-Sree/blackwell-gpu-slicing)
*Bare-metal multi-tenant GPU allocation with Slurm*
- Built dynamic NVIDIA MPS and MIG resource managers with custom Slurm prolog/epilog hooks for sub-second VRAM reclamation.
- Optimized for Dual AMD EPYC 9554 (256 vCPUs) + Dual RTX Pro 6000 GPUs with NUMA node binding.
- **Stack:** `Slurm`, `NVIDIA MPS`, `NVIDIA MIG`, `Linux Kernel`

</td>
<td width="50%" valign="top">

#### [Enterprise Edge & Cloudflare Architecture](https://github.com/Shreesh-Sree/Server-Cloudflare-Architecture)
*Zero-trust edge gateway for multi-tenant microservices*
- Production ingress routing across 15+ services with automated Let's Encrypt TLS, Zitadel OIDC authentication, and zero exposed public ports.
- Real-time telemetry pipeline via Prometheus and Grafana dashboards.
- **Stack:** `Traefik`, `Cloudflare Tunnels`, `Zitadel SSO`, `Prometheus`

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### [VeraQX — Real-Time Support Triage Agent](https://github.com/Shreesh-Sree/Aethercode-main)
*Citation-grounded hybrid retrieval engine*
- Fused Okapi BM25 sparse keyword ranking with dense vector embeddings via Reciprocal Rank Fusion (RRF).
- Implemented as a high-performance Go terminal application delivering sub-second source-attributed responses.
- **Stack:** `Go`, `Hybrid RAG`, `BM25`, `Reciprocal Rank Fusion`

</td>
<td width="50%" valign="top">

#### [LearnHouse — Proctored Delivery Integration](https://github.com/learnhouse/learnhouse)
*Open-source learning platform contribution (AGPL-3.0)*
- Extended FastAPI/SQLModel backend services to support Safe Exam Browser (SEB) configuration and locked-down test delivery.
- **Stack:** `Python`, `FastAPI`, `SQLModel`, `PostgreSQL`

</td>
</tr>
</table>

---

### Engineering Experience & Leadership

- **Presidio Inc.** · Software Development Engineer Intern (PRIME SWE) · *Jun 2026 – Jul 2026*
  - Selected 1 of 15 from 2,000+ applicants. Built JWT/RBAC-secured microservices deploying to AWS ECS and Cloud Run.
  - Implemented LangGraph & Ollama agentic pipelines for automated structured document parsing.
- **Indian Institute of Technology Jammu** · Agentic AI Research Intern · *Jun 2026 – Jul 2026*
  - Implemented physics-informed neural networks (PINNs) in PyTorch to model heat-transfer dynamics and print-parameter accuracy for SLS 3D manufacturing.
- **HackerRank Campus Crew** · Technical Lead & Campus Ambassador · *Jun 2026 – Present*
  - Architecting automated bot and test delivery tooling for campus ambassador hackathons and contests.
- **Databricks** · Student Fellow APJ 2026 · *Selected 1 of 38 from 7,171 global applicants*
- **AWS Student Builder Group** · Campus Leader & Core Member · *Jan 2026 – Present*
- **Google Developer Group (GDG) SJCE** · Technical Coordinator · *Dec 2025 – Present*

---

### Activity & Telemetry

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Shreesh-Sree/Shreesh-Sree/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Shreesh-Sree/Shreesh-Sree/output/github-contribution-grid-snake.svg" />
  <img alt="Contribution Snake" src="https://raw.githubusercontent.com/Shreesh-Sree/Shreesh-Sree/output/github-contribution-grid-snake-dark.svg" width="100%" />
</picture>

<br/><br/>

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Shreesh-Sree&theme=github_dark" width="100%" />

<br/>

<table border="0">
<tr>
<td width="50%" valign="top">
<img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=Shreesh-Sree&theme=github_dark" width="100%" />
</td>
<td width="50%" valign="top">
<img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Shreesh-Sree&theme=github_dark" width="100%" />
</td>
</tr>
</table>

</div>

---

<div align="center">
<sub>Sreesanth R · Chennai, India · <a href="mailto:shreesh.exe22@gmail.com">shreesh.exe22@gmail.com</a> · <a href="https://shreesh-sree.dev">shreesh-sree.dev</a></sub>
</div>
