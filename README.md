<div align="center">

# Sreesanth R

**Backend Engineer · AI Systems · Infrastructure**

[![Portfolio](https://img.shields.io/badge/Portfolio-shreesh--sree.dev-0f172a?style=flat-square&logo=vercel&logoColor=white)](https://shreesh-sree.dev)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-sree--santh-0077B5?style=flat-square&logo=linkedin)](https://linkedin.com/in/sree-santh)
[![Codolio](https://img.shields.io/badge/Codolio-shreesh--22-6c47ff?style=flat-square&logo=codeforces&logoColor=white)](https://codolio.com/profile/shreesh-22)
[![Email](https://img.shields.io/badge/Email-shreesh.exe22@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:shreesh.exe22@gmail.com)

</div>

---

## About

B.Tech in **Artificial Intelligence & Machine Learning** at **St. Joseph's College of Engineering, Anna University** (CGPA 8.40 / 10 · Expected May 2028). I build **high-throughput backend systems** in Go, Python, and TypeScript — from gRPC microservices and multi-tenant platforms to agentic AI pipelines and GPU-accelerated inference infrastructure.

I have interned at **Presidio Inc.** (PRIME SWE Program — 1 of 15 from 2,000+ applicants) and at **IIT Jammu** (physics-informed neural networks for SLS 3D printing). I'm also a **Databricks Student Fellow APJ 2026** — selected as 1 of 38 from 7,171 global applicants.

---

## Technical Stack

**Languages**

![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=c%2B%2B&logoColor=white)

**Backend & APIs**

![Gin](https://img.shields.io/badge/Gin-00ADD8?style=flat-square&logo=go&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=node.js&logoColor=white)
![gRPC](https://img.shields.io/badge/gRPC-4285F4?style=flat-square&logo=google&logoColor=white)
![REST](https://img.shields.io/badge/REST-FF6C37?style=flat-square&logo=postman&logoColor=white)

**Data & Infrastructure**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-844FBA?style=flat-square&logo=terraform&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoft-azure&logoColor=white)

**AI / ML**

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=llama&logoColor=white)
![RAG](https://img.shields.io/badge/RAG_Pipelines-6c47ff?style=flat-square)
![MCP](https://img.shields.io/badge/Model_Context_Protocol-FF6B35?style=flat-square)

---

## Work Experience

### Software Development Engineer Intern & Agentic AI Research Intern
**Presidio Inc.** · Hybrid, Chennai · Jun 2026 – Jul 2026

> Selected for the **PRIME Software Engineering Internship** as **1 of 15 from 2,000+ applicants** through multi-round technical and system-design screening.

- Shipped **JWT/RBAC-secured Node.js microservices** with automated CI/CD pipelines to AWS ECS and Cloud Run by decomposing a monolithic auth flow into independently deployable services with role-scoped access control.
- Built a **React 19 + TypeScript operations dashboard** with TanStack Query for cache-consistent data fetching and JWT-focused security test cases against the auth boundary.
- Designed **agentic pipelines with LangGraph & Ollama** to automate secure parsing and structured extraction from unstructured documents — reducing manual document-review effort in internal workflows.

---

### Agentic AI Research Intern
**Indian Institute of Technology Jammu** · On-site, Jammu · Jun 2026 – Jul 2026

- Improved SLS 3D-printing dimensional accuracy by **12%** by implementing **physics-informed neural networks in PyTorch** with custom energy-density constraints to model print-parameter behaviour.
- Built numerical simulation pipelines for printer thermal accumulation, modelling heat-transfer dynamics across print cycles to validate PINN predictions against physical printer output.

---

## Featured Projects

### [AetherCode](https://github.com/Shreesh-Sree/Aethercode-main) — Multi-Tenant Coding Assessment Platform
`Go` `gRPC` `PostgreSQL` `Casbin` `Kubernetes`

Architected independently deployable **Go microservices over gRPC-defined contracts** to eliminate cross-tenant data exposure risk. Enforced least-privilege access via a Casbin-backed authorization layer with short-lived HMAC capabilities, PostgreSQL row-level security, and the Judge0 execution engine isolated behind a completion-only bridge.

---

### VeraQX — Enterprise Support Triage Agent
`Go` `Ollama` `Hybrid RAG` `Okapi BM25` `RRF`

Delivered a **citation-grounded support triage agent within a 24-hour hackathon window** — a terminal-based Go application fusing Okapi BM25 keyword search with vector search via Reciprocal Rank Fusion (RRF) for precision-ranked, source-attributed answers.

---

### Reimbursement Tool — Presidio Intern Capstone
`FastAPI` `React` `PostgreSQL` `Supabase` `Terraform` `Azure`

Built tenant-scoped RBAC and complete audit logging into a **FastAPI + React expense-reimbursement platform** with multi-level approval workflows, enforcing tenant-level data isolation and full auditability.

---

### [LearnHouse](https://github.com/learnhouse/learnhouse) — Open Source Contributor
`FastAPI` `Python` `SQLModel` `PostgreSQL`

Contributing backend features to an AGPL-3.0 learning platform used for course delivery, auto-graded code execution, and analytics. Currently integrating **Safe Exam Browser (SEB) support** to enable locked-down, proctored assessment delivery.

---

## Education

**St. Joseph's College of Engineering** _(Anna University)_
B.Tech, Artificial Intelligence & Machine Learning · **CGPA 8.40 / 10** · Chennai, Tamil Nadu · Expected May 2028

*Relevant Coursework:* Data Structures & Algorithms · Object-Oriented Design · Operating Systems · Database Management Systems · Distributed Systems · Computer Networks

---

## Leadership & Recognition

| Role | Organisation | Period |
|---|---|---|
| 🏅 **Databricks Student Fellow, APJ 2026** | Databricks | 2026 — selected 1 of 38 from 7,171 global applicants |
| 🛠 **Technical Lead & Campus Ambassador** | HackerRank Campus Crew | Jun 2026 – Present |
| ☁️ **Campus Leader & Core Member** | AWS Student Builder Group | Jan 2026 – Present |
| 💡 **Technical Coordinator** | Google Developer Group (GDG) SJCE | Dec 2025 – Present |

---

## GitHub Stats

<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Shreesh-Sree&show_icons=true&theme=github_dark&hide_border=true&count_private=true&rank_icon=github)
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Shreesh-Sree&layout=compact&theme=github_dark&hide_border=true&langs_count=8)

</div>

---

<div align="center">
<sub>Chennai, India · Open to Backend Engineering, AI Systems, and Distributed Infrastructure roles</sub>
</div>
