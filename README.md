# Sreesanth R

**Systems Architect & Backend Infrastructure Engineer**  
Chennai, India &bull; Technical Lead @ HackerRank Campus Crew &bull; Systems Lead @ AetherCode

[Portfolio](https://shreesh-sree.dev) &nbsp;&bull;&nbsp; [LinkedIn](https://linkedin.com/in/sree-santh) &nbsp;&bull;&nbsp; [GitHub](https://github.com/Shreesh-Sree) &nbsp;&bull;&nbsp; [Email](mailto:shreesh.exe22@gmail.com) &nbsp;&bull;&nbsp; [Codolio](https://codolio.com/profile/shreesh-22)

---

### Overview

Backend and systems engineer specializing in low-level AI inference acceleration, bare-metal cluster orchestration, and zero-trust distributed architectures. Currently pursuing a B.Tech in Artificial Intelligence & Machine Learning at St. Joseph's College of Engineering, Anna University (CGPA 8.40 / 10).

- **Low-Level Inference Engineering:** Author of speculative decoding patches for `llama.cpp` (`FastMTP` draft-vocabulary trimming), achieving 2.5x token throughput acceleration on NVIDIA Blackwell architectures.
- **Bare-Metal Cluster Orchestration:** Architect of multi-tenant compute frameworks using Slurm, NVIDIA MPS, and dynamic MIG resource slicing on dual AMD EPYC (256 threads) and dual RTX Pro 6000 Blackwell workstations.
- **Zero-Trust Edge Networks:** Engineered enterprise edge architectures running 15+ isolated microservices with Traefik, Cloudflare Zero-Trust tunnels, and Zitadel OIDC authentication.
- **Selective Engineering Programs:** Former SDE Intern at Presidio (PRIME program, selected 1 of 15 from 2,000+ applicants), AI Research Intern at IIT Jammu, and Databricks Student Fellow APJ 2026 (selected 1 of 38 from 7,171 global applicants).

---

### Active Focus & Research

- **Speculative Inference:** Extending draft-vocabulary trimming and tensor logit scattering to Multi-Token Prediction (MTP) architectures.
- **Bare-Metal Memory Tiering:** NUMA-aware dynamic VRAM allocation and automated kernel hooks for high-density multi-tenant LLM serving.
- **Sandboxed Execution Security:** Zero-leakage isolation primitives using Linux cgroups, namespaces, and seccomp filters for untrusted code execution.

---

### Featured Systems & Engineering

<table>
<tr>
<td width="50%" valign="top">

#### [FastMTP — llama.cpp Speculative Acceleration](https://github.com/Shreesh-Sree/llama.cpp/tree/feat/fastmtp-ollama)
*Upstream C++ optimization for qwen35 and qwen35moe architectures*
- Trimmed the 152k speculative vocabulary tensor to active draft subspace dimensions, slashing tensor compute overhead.
- Engineered logit scattering kernels for low-latency speculative verification.
- Validated on dual RTX Pro 6000 hardware with **44.5 &rarr; 113.9 tok/s (2.5x sustained speedup)**.
- **Stack:** `C++`, `CUDA`, `GGML`, `llama.cpp`

</td>
<td width="50%" valign="top">

#### [AetherCode — Distributed Execution Engine](https://github.com/Shreesh-Sree/Aethercode-main)
*High-throughput multi-tenant code assessment & judge platform*
- Architected Go microservices communicating over strict gRPC protobuf definitions.
- Enforced zero cross-tenant data exposure via Casbin capability-based access control, short-lived HMAC tokens, and PostgreSQL row-level security.
- Isolated untrusted code evaluation using Judge0 sandboxed worker clusters behind an async completion bridge.
- **Stack:** `Go`, `gRPC`, `PostgreSQL`, `Casbin`, `Kubernetes`

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### [Blackwell Dynamic GPU Slicing & Slurm](https://github.com/Shreesh-Sree/blackwell-gpu-slicing)
*Bare-metal multi-tenant GPU allocation framework*
- Custom multi-tenant compute engine with dynamic NVIDIA MPS and MIG resource allocation for dual AMD EPYC (256 threads) + dual RTX Pro 6000 GPUs.
- Automated lifecycle management hooks reducing multi-tenant VRAM reclamation latency from **~45s to <500ms**.
- **Stack:** `Slurm`, `NVIDIA MPS`, `NVIDIA MIG`, `Linux Kernel`

</td>
<td width="50%" valign="top">

#### [Enterprise Edge & Cloudflare Architecture](https://github.com/Shreesh-Sree/Server-Cloudflare-Architecture)
*Zero-trust ingress gateway for production microservices*
- Production routing across 15+ institutional microservices with zero publicly exposed ports.
- Automated dynamic TLS certificate renewal, Zitadel OIDC enterprise single sign-on, and sub-millisecond local routing.
- Real-time Prometheus metrics scraping and Grafana infrastructure dashboards.
- **Stack:** `Traefik`, `Cloudflare Tunnels`, `Zitadel SSO`, `Prometheus`, `Grafana`

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### [VeraQX — Real-Time Support Triage Agent](https://github.com/Shreesh-Sree/Aethercode-main)
*Citation-grounded hybrid retrieval engine*
- Fused Okapi BM25 sparse keyword ranking with dense vector embeddings via Reciprocal Rank Fusion (RRF).
- Terminal-based Go application delivering sub-second source-attributed responses for technical campus support queries.
- **Stack:** `Go`, `Hybrid RAG`, `Okapi BM25`, `Reciprocal Rank Fusion`

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

### Upstream Open-Source Contributions

| Project | Area | Contribution & Technical Impact | Link |
|:---|:---|:---|:---|
| **`ggml-org/llama.cpp`** | Speculative Decoding | Built `d2t` draft-vocabulary tensor trimming and speculative logit scatter kernels for Qwen-35 models (+156% tok/s). | [`feat/fastmtp-ollama`](https://github.com/Shreesh-Sree/llama.cpp/tree/feat/fastmtp-ollama) |
| **`learnhouse/learnhouse`** | Assessment Infrastructure | Integrated Safe Exam Browser (SEB) proctoring protocol into backend service layer (AGPL-3.0). | [learnhouse](https://github.com/learnhouse/learnhouse) |

---

### Engineering Principles

- **Zero-Allocation Hot Paths:** Eliminate heap allocations inside critical tensor operations, speculative validation loops, and high-frequency gRPC streams.
- **Default-Deny Boundary Isolation:** Enforce capability-based tokens, strict tenant row-level security, and hardened Linux kernel cgroups over implicit application trust.
- **Deterministic Resilience:** Favor explicit state machine transitions, circuit breakers, and bounded work queues over unbounded heuristic retries.

---

### Technical Arsenal

| Domain | Technologies & Frameworks |
|:---|:---|
| **Core Languages** | Go, C++, Python, TypeScript, SQL, Bash |
| **Backend & Distributed Systems** | gRPC, Protocol Buffers, Gin, FastAPI, Node.js, Express, Fastify, BullMQ, WebSockets |
| **AI Systems & Acceleration** | CUDA, `llama.cpp`, GGML, vLLM, NVIDIA NIM, PyTorch, LangGraph, RAG Pipelines, MCP |
| **Compute & Orchestration** | Slurm Workload Manager, NVIDIA MPS, NVIDIA MIG, Docker, Podman, Kubernetes, K3s |
| **Databases & Storage** | PostgreSQL (Row-Level Security, pgvector), Redis, SQLite, ClickHouse |
| **Infrastructure & Networking** | Terraform, AWS (ECS, Lambda), Azure, Cloudflare Zero-Trust, Traefik, Zitadel OIDC |
| **Observability & Telemetry** | Prometheus, Grafana, OpenTelemetry, Linux Kernel Tuning (`sysctl`, HugePages, NUMA) |

---

### Problem Solving & Foundations

- Active competitive problem solving across **[Codolio (`shreesh-22`)](https://codolio.com/profile/shreesh-22)**, LeetCode, and HackerRank.
- Core algorithmic focus: Graph Algorithms, Dynamic Programming, Distributed Consensus, and Low-Level Concurrency Primitives.

---

### Experience & Leadership

- **Presidio Inc.** &bull; *Software Development Engineer Intern (PRIME SWE)* &bull; `Jun 2026 – Jul 2026`
  - Selected 1 of 15 from 2,000+ applicants. Built JWT/RBAC-secured Node.js microservices deploying to AWS ECS and Cloud Run.
  - Implemented LangGraph and Ollama agentic pipelines for secure parsing and structured extraction from unstructured corporate documents.
- **Indian Institute of Technology Jammu** &bull; *Agentic AI Research Intern* &bull; `Jun 2026 – Jul 2026`
  - Implemented physics-informed neural networks (PINNs) in PyTorch to model heat-transfer dynamics and print-parameter accuracy for SLS 3D manufacturing (12% dimensional accuracy gain).
- **HackerRank Campus Crew** &bull; *Technical Lead & Campus Ambassador* &bull; `Jun 2026 – Present`
  - Directing technical test-delivery architecture, automated support tooling, and campus ambassador hackathon operations.
- **Databricks** &bull; *Student Fellow APJ 2026* &bull; `2026`
  - Selected 1 of 38 from 7,171 global applicants across the Asia-Pacific & Japan region.
- **AWS Student Builder Group** &bull; *Campus Leader & Core Member* &bull; `Jan 2026 – Present`
  - Leading campus-wide cloud computing workshops, hands-on build challenges, and hackathons.
- **Google Developer Group (GDG) SJCE** &bull; *Technical Coordinator* &bull; `Dec 2025 – Present`
  - Organizing technical sessions on scalable system architectures, AI/ML, and open-source development.

---

### Education

**St. Joseph’s College of Engineering (Anna University)**  
B.Tech, Artificial Intelligence & Machine Learning &bull; **CGPA: 8.40 / 10** &bull; Expected May 2028 &bull; Chennai, Tamil Nadu  
*Core Coursework:* Distributed Systems, Operating Systems, Database Management Systems, Computer Networks, Object-Oriented Design, Data Structures & Algorithms.

---

### Activity

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Shreesh-Sree/Shreesh-Sree/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Shreesh-Sree/Shreesh-Sree/output/github-contribution-grid-snake.svg" />
  <img alt="Contribution Snake" src="https://raw.githubusercontent.com/Shreesh-Sree/Shreesh-Sree/output/github-contribution-grid-snake-dark.svg" width="100%" />
</picture>

</div>

---

<div align="center">
<sub>Sreesanth R &bull; Chennai, India &bull; <a href="mailto:shreesh.exe22@gmail.com">shreesh.exe22@gmail.com</a> &bull; <a href="https://shreesh-sree.dev">shreesh-sree.dev</a></sub>
</div>
