<div align="center">

# Sreesanth R
### **Systems Architect & AI Infrastructure Engineer**
*Chennai, India &bull; Technical Lead @ HackerRank Campus Crew &bull; Systems Lead @ AetherCode*

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Shreesh-Sree)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:shreesh.exe22@gmail.com)
[![Portfolio](https://img.shields.io/badge/Architecture-00C7B7?style=flat-square&logo=diagram-next&logoColor=white)](#-featured-systems--architecture)

<br/>

</div>

---

### 👨‍💻 Executive Profile

I am a Systems Architect and Backend/AI Infrastructure Engineer focused on building high-performance distributed systems, low-level LLM inference engines, and enterprise edge architectures. 

* ⚡ **High-Performance AI Inference:** Author of low-level speculative decoding patches for `llama.cpp` (FastMTP draft-vocabulary trimming), achieving 2.3x–2.5x tok/s acceleration on Blackwell architectures.
* 🖥️ **GPU & Cluster Orchestration:** Designing bare-metal multi-tenant GPU allocation frameworks using **Slurm, NVIDIA MPS, and MIG** on Dual AMD EPYC 256-thread, Dual NVIDIA RTX Pro 6000 Blackwell workstations.
* 🌐 **Edge & Zero-Trust Cloud Infrastructure:** Architecting production edge networks using **Traefik, Cloudflare Zero Trust tunnels, Zitadel OIDC SSO, and Prometheus/Grafana** observability suites.
* 🎓 **Leadership & Community:** Technical Lead for the **HackerRank Campus Crew (HRCC)** program, empowering student ambassadors with automated support agents, test delivery platforms, and event analytics.

---

### 🛠️ Core Engineering Competencies

<div align="center">

| Domain | Technologies & Frameworks |
| :--- | :--- |
| **AI Systems & Inference** | `CUDA` &bull; `C++` &bull; `llama.cpp` &bull; `vLLM` &bull; `NVIDIA NIM` &bull; `PyTorch` &bull; `Ollama` &bull; `TensorRT-LLM` |
| **Distributed Systems & Edge** | `Slurm Workload Manager` &bull; `NVIDIA MPS` &bull; `Docker` &bull; `Podman` &bull; `Kubernetes / K3s` &bull; `Traefik` &bull; `Cloudflare Tunnels` |
| **Backend & Messaging** | `Python 3.12` &bull; `TypeScript` &bull; `Node.js` &bull; `FastAPI` &bull; `Express` &bull; `BullMQ` &bull; `WebSockets / SSE` |
| **Databases & Telemetry** | `PostgreSQL` &bull; `pgvector` &bull; `ClickHouse` &bull; `Redis` &bull; `MariaDB` &bull; `Prometheus` &bull; `Grafana` |
| **Tools & Environments** | `Linux (Ubuntu Server)` &bull; `Git / GitHub CLI` &bull; `NUMA Optimization` &bull; `HugePages` &bull; `Bash` |

</div>

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

#### 💻 AetherCode Distributed Execution Platform
* **Architecture:** High-concurrency online code evaluation platform with multi-worker Judge0 clustering, BullMQ queue dispatching, and SSE testcase telemetry.
* **Impact:** Kernel-level limits tuning (`sysctl`, `limits.conf`) and native PostgreSQL migration supporting concurrent campus-wide competitive exams.
* **Tags:** `Node.js` &bull; `TypeScript` &bull; `BullMQ` &bull; `Judge0` &bull; `Postgres`

</td>
</tr>
</table>

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

<sub>Designed & Architected by Sreesanth R &bull; 2026</sub>

</div>
