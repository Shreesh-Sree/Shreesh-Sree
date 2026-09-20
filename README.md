<div align="center">

# Sreesanth R aka Shreesh
### **Systems Architect & AI Infrastructure Engineer**
*Chennai, India &bull; Technical Lead @ HackerRank Campus Crew &bull; Systems Lead @ AetherCode*

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/sree-santh)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Shreesh-Sree)
[![Portfolio](https://img.shields.io/badge/Portfolio-shreesh--sree.dev-0f172a?style=flat-square&logo=vercel&logoColor=white)](https://shreesh-sree.dev)
[![Codolio](https://img.shields.io/badge/Codolio-shreesh--22-6c47ff?style=flat-square&logo=codeforces&logoColor=white)](https://codolio.com/profile/shreesh-22)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:shreesh.exe22@gmail.com)

<br/>

</div>

---

### 👨‍💻 Executive Profile

I am a Systems Architect and Backend/AI Infrastructure Engineer focused on building high-performance distributed systems, low-level LLM inference engines, and enterprise edge architectures. Currently pursuing B.Tech in **Artificial Intelligence & Machine Learning** at **St. Joseph's College of Engineering, Anna University** (CGPA 8.40 / 10 · Expected May 2028).

* ⚡ **High-Performance AI Inference:** Author of low-level speculative decoding patches for `llama.cpp` (FastMTP draft-vocabulary trimming), achieving 2.3x–2.5x tok/s acceleration on Blackwell architectures.
* 🖥️ **GPU & Cluster Orchestration:** Designing bare-metal multi-tenant GPU allocation frameworks using **Slurm, NVIDIA MPS, and MIG** on Dual AMD EPYC 256-thread, Dual NVIDIA RTX Pro 6000 Blackwell workstations.
* 🌐 **Edge & Zero-Trust Cloud Infrastructure:** Architecting production edge networks using **Traefik, Cloudflare Zero Trust tunnels, Zitadel OIDC SSO, and Prometheus/Grafana** observability suites.
* 🎓 **Leadership & Community:** Technical Lead for the **HackerRank Campus Crew (HRCC)** program, empowering student ambassadors with automated support agents, test delivery platforms, and event analytics.
* 🏅 **Databricks Student Fellow APJ 2026** — selected as 1 of 38 from 7,171 global applicants.

---

### 🛠️ Core Engineering Competencies

<div align="center">

| Domain | Technologies & Frameworks |
| :--- | :--- |
| **Primary Languages** | `Go` &bull; `Python` &bull; `TypeScript` &bull; `C++` |
| **Backend & APIs** | `Gin` &bull; `FastAPI` &bull; `Node.js` &bull; `gRPC` &bull; `Express` &bull; `Fastify` &bull; `BullMQ` &bull; `WebSockets / SSE` |
| **AI Systems & Inference** | `CUDA` &bull; `llama.cpp` &bull; `vLLM` &bull; `NVIDIA NIM` &bull; `PyTorch` &bull; `Ollama` &bull; `LangGraph` &bull; `RAG Pipelines` &bull; `MCP` |
| **Distributed Systems & Edge** | `Slurm` &bull; `NVIDIA MPS` &bull; `Docker` &bull; `Podman` &bull; `Kubernetes / K3s` &bull; `Traefik` &bull; `Cloudflare Tunnels` |
| **Databases & Telemetry** | `PostgreSQL` &bull; `pgvector` &bull; `ClickHouse` &bull; `Redis` &bull; `SQLite` &bull; `Prometheus` &bull; `Grafana` |
| **Cloud & DevOps** | `AWS (ECS, Lambda)` &bull; `Azure` &bull; `Terraform` &bull; `CI/CD` &bull; `Kubernetes` |

</div>

---

### 💼 Work Experience

#### Software Development Engineer Intern & Agentic AI Research Intern
**Presidio Inc.** · Hybrid, Chennai · Jun 2026 – Jul 2026

> Selected for the **PRIME Software Engineering Internship** as **1 of 15 from 2,000+ applicants** through multi-round technical and system-design screening.

- Shipped **JWT/RBAC-secured Node.js microservices** with automated CI/CD pipelines to AWS ECS and Cloud Run by decomposing a monolithic auth flow into independently deployable services with role-scoped access control.
- Built a **React 19 + TypeScript operations dashboard** with TanStack Query for cache-consistent data fetching and JWT-focused security test cases against the auth boundary.
- Designed **agentic pipelines with LangGraph & Ollama** to automate secure parsing and structured extraction from unstructured documents, reducing manual document-review effort in internal workflows.

#### Agentic AI Research Intern
**Indian Institute of Technology Jammu** · On-site, Jammu · Jun 2026 – Jul 2026

- Improved SLS 3D-printing dimensional accuracy by **12%** by implementing **physics-informed neural networks in PyTorch** with custom energy-density constraints to model print-parameter behaviour.
- Built numerical simulation pipelines for printer thermal accumulation, modelling heat-transfer dynamics across print cycles to validate PINN predictions against physical printer output.

---

### 🚀 Featured Systems & Architecture

<table>
<tr>
<td width="50%" valign="top">

#### ⚡ Blackwell Dynamic GPU Slicing & Slurm
* **Architecture:** Custom multi-tenant compute engine for Dual AMD EPYC 9554 (256 threads) + Dual NVIDIA RTX Pro 6000 Blackwell 96GB.
* **Impact:** Implemented dynamic NVIDIA MPS & MIG resource managers, Slurm cluster configs, and automated prolog/epilog hooks that immediately reclaim idle VRAM upon job completion.
* **Tags:** `C++` &bull; `Slurm` &bull; `NVIDIA MPS` &bull; `CUDA`

</td>
<td width="50%" valign="top">

#### 🧠 FastMTP Speculative Decoding (`llama.cpp`)
* **Architecture:** Upstream C++ patch for `qwen35` and `qwen35moe` architectures introducing `d2t` draft-vocabulary trimming and logit scattering.
* **Impact:** Reduced speculative draft tensor overhead from 152k to trimmed draft dimensions, increasing generation throughput from **44.5 tok/s to 113.9 tok/s** (~2.5x speedup).
* **Tags:** `C++` &bull; `llama.cpp` &bull; `CUDA Kernels` &bull; `GGML`

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### 🛡️ Enterprise Edge & Cloudflare Architecture
* **Architecture:** Production edge network orchestrating reverse proxying, dynamic TLS, Cloudflare tunnels, and Zitadel SSO across 15+ institutional microservices.
* **Impact:** Zero-open-port security model with real-time Prometheus/Grafana telemetry, automated SSL renewal, and sub-millisecond local routing.
* **Tags:** `Traefik` &bull; `Cloudflare Tunnels` &bull; `Zitadel SSO` &bull; `Grafana`

</td>
<td width="50%" valign="top">

#### 💻 AetherCode — Multi-Tenant Assessment Platform
* **Architecture:** Go microservices over gRPC-defined contracts with Casbin-backed authorization, PostgreSQL row-level security, and a completion-only Judge0 execution bridge.
* **Impact:** Eliminated cross-tenant data exposure risk with short-lived HMAC capabilities and kernel-level limits tuning (`sysctl`, `limits.conf`) for campus-wide concurrent exams.
* **Tags:** `Go` &bull; `gRPC` &bull; `PostgreSQL` &bull; `Casbin` &bull; `Kubernetes`

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### 🔍 VeraQX — Enterprise Support Triage Agent
* **Architecture:** Terminal-based Go application fusing Okapi BM25 keyword search with vector search via Reciprocal Rank Fusion (RRF) for citation-grounded answers.
* **Impact:** Delivered a working triage agent within a **24-hour hackathon window**.
* **Tags:** `Go` &bull; `Hybrid RAG` &bull; `Okapi BM25` &bull; `RRF`

</td>
<td width="50%" valign="top">

#### 📦 LearnHouse — Open Source Contributor
* **Architecture:** AGPL-3.0 learning platform for course delivery, auto-graded code execution, and analytics; extending the FastAPI/Python/SQLModel service layer.
* **Impact:** Currently integrating **Safe Exam Browser (SEB)** support to enable locked-down, proctored assessment delivery.
* **Tags:** `FastAPI` &bull; `Python` &bull; `SQLModel` &bull; `PostgreSQL`

</td>
</tr>
</table>

---

### 🎓 Education

**St. Joseph's College of Engineering** *(Anna University)*
B.Tech, Artificial Intelligence & Machine Learning · **CGPA 8.40 / 10** · Chennai, Tamil Nadu · Expected May 2028

*Relevant Coursework:* Data Structures & Algorithms · Object-Oriented Design · Operating Systems · Database Management Systems · Distributed Systems · Computer Networks

---

### 🏆 Leadership & Recognition

| Role | Organisation | Period |
|:---|:---|:---|
| 🏅 **Databricks Student Fellow, APJ 2026** | Databricks | 2026 — selected 1 of 38 from 7,171 global applicants |
| 🛠 **Technical Lead & Campus Ambassador** | HackerRank Campus Crew | Jun 2026 – Present |
| ☁️ **Campus Leader & Core Member** | AWS Student Builder Group | Jan 2026 – Present |
| 💡 **Technical Coordinator** | Google Developer Group (GDG) SJCE | Dec 2025 – Present |

---

### 📊 GitHub Activity & Metrics

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

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Shreesh-Sree&layout=compact&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=58a6ff&text_color=c9d1d9" alt="Top Languages"/>

</div>

---

<div align="center">

### 📬 Connect & Collaborate

Interested in high-performance computing, AI systems architecture, or distributed engineering? Let's connect!

[![Email](https://img.shields.io/badge/shreesh.exe22%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:shreesh.exe22@gmail.com)
[![GitHub](https://img.shields.io/badge/Shreesh--Sree-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Shreesh-Sree)
[![Portfolio](https://img.shields.io/badge/shreesh--sree.dev-0f172a?style=for-the-badge&logo=vercel&logoColor=white)](https://shreesh-sree.dev)

<sub>Designed & Architected by Sreesanth R &bull; 2026</sub>

</div>
