<p align="center">
  <img src="assets/hero-banner.svg" alt="D. Meiram - Staff AI &amp; Distributed Systems Engineer" width="100%">
</p>

<p align="center">
  <a href="https://linkedin.com"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://t.me"><img src="https://img.shields.io/badge/Telegram-Chat-229ED9?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram"></a>
  <a href="mailto:meiram@example.com"><img src="https://img.shields.io/badge/Email-Contact_Me-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://github.com/disamee"><img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
</p>

---

### ⚡ Executive Summary

I architect and deliver **production-grade Artificial Intelligence, Hybrid RAG Systems, High-Concurrency Web Scraping Farms, and Real-Time Financial/Commodity Platforms**. 

Over the past several years, I have engineered mission-critical systems for leading industrial and financial enterprises (including **KazMunayGas / OzenMunayGas**, commodity trade groups, and financial analytics platforms). My focus is end-to-end architectural rigor: from document parsing and hybrid vector retrieval down to sub-100ms async backends, Kubernetes cluster deployments, and reactive web interfaces.

---

### 📊 Production Impact & Engineering Metrics

<table>
  <tr>
    <td width="50%">
      <img src="assets/metrics/card-rag.svg" alt="20,000+ Docs RAG" width="100%">
    </td>
    <td width="50%">
      <img src="assets/metrics/card-tickers.svg" alt="<100ms Latency" width="100%">
    </td>
  </tr>
  <tr>
    <td width="50%">
      <img src="assets/metrics/card-prompts.svg" alt="400+ LOC Prompts" width="100%">
    </td>
    <td width="50%">
      <img src="assets/metrics/card-scraping.svg" alt="10,000+ Daily Scrapes" width="100%">
    </td>
  </tr>
</table>

---

### 🏗️ Enterprise System Architecture Blueprint

Below is the high-throughput, low-latency architecture pattern utilized across my industrial RAG and real-time streaming deployments:

```mermaid
flowchart LR
    subgraph INGEST ["📥 Ingestion & High-Concurrency Feeds"]
        A1["📄 Unstructured PDFs & Well Logs"]
        A2["🌐 Selenium Headless Cluster\n(10k+ Tasks / Day)"]
        A3["📈 Real-time Market Tickers\n(WebSocket Feeds)"]
    end

    subgraph ENGINE ["🧠 Hybrid RAG & Reasoning Core"]
        B1["Sparse BM25 Index\n(Lexical Precision)"]
        B2["Dense Vector DB\n(Qdrant / ChromaDB)"]
        B3["Cross-Encoder Reranker\n(Relevance Sieve)"]
        B4["LLM Guardrails Engine\n(400+ LOC System Prompts)"]
        B1 & B2 --> B3 --> B4
    end

    subgraph SERVE ["⚡ Production Delivery & Cloud"]
        C1["FastAPI Async Gateway\n(Sub-50ms Routing)"]
        C2["Redis Pub/Sub\n(Live Ticker Broadcast)"]
        C3["Kubernetes Helm Deployment\n(Gateway API & Ingress)"]
        C4["React 18 / Next.js Dashboards\n& Telegram Bots"]
        C1 --> C2 --> C4
        C3 -.-> C1
    end

    INGEST --> ENGINE --> SERVE

    style INGEST fill:#0f172a,stroke:#38bdf8,stroke-width:1.5px,color:#f8fafc
    style ENGINE fill:#0b1324,stroke:#00f0ff,stroke-width:2px,color:#f8fafc
    style SERVE fill:#062e24,stroke:#10b981,stroke-width:1.5px,color:#f8fafc
```

---

### 🏛️ Featured Enterprise Architecture Case Studies

> *(Due to corporate confidentiality and NDA compliance, proprietary codebases and internal corporate data are protected. The repositories below contain comprehensive technical architecture whitepapers, Mermaid topology diagrams, benchmark evaluations, and deployment manifests.)*

<table>
  <tr>
    <td width="50%" valign="top">
      <h4>🌾 <a href="https://github.com/disamee/fergus-commodity-analytics-case-study">Fergus Commodity Analytics</a></h4>
      <p><b>Domain:</b> FinTech &amp; Commodity Trading RAG</p>
      <p>Hybrid RAG engine for grain traders with real-time price prediction, automated SharePoint knowledge base synchronization, and currency trend charts.</p>
      <p>
        <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI">
        <img src="https://img.shields.io/badge/Hybrid_RAG-00f0ff?style=flat-square" alt="RAG">
        <img src="https://img.shields.io/badge/WebSockets-010101?style=flat-square&logo=socketdotio&logoColor=white" alt="WebSockets">
        <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL">
      </p>
      <p><a href="https://github.com/disamee/fergus-commodity-analytics-case-study"><b>→ Read Architecture Whitepaper</b></a></p>
    </td>
    <td width="50%" valign="top">
      <h4>🛢️ <a href="https://github.com/disamee/geological-rag-architecture-case-study">Geological Subsurface RAG</a></h4>
      <p><b>Domain:</b> Energy &amp; Oil &amp; Gas AI</p>
      <p>Multimodal PDF/well log chunking pipeline, sparse BM25 + dense vector search, and K8s infrastructure sizing for massive geological survey archives.</p>
      <p>
        <img src="https://img.shields.io/badge/LlamaIndex-FF6F00?style=flat-square" alt="LlamaIndex">
        <img src="https://img.shields.io/badge/Qdrant-DC2626?style=flat-square" alt="Qdrant">
        <img src="https://img.shields.io/badge/BM25-38bdf8?style=flat-square" alt="BM25">
        <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" alt="K8s">
      </p>
      <p><a href="https://github.com/disamee/geological-rag-architecture-case-study"><b>→ Read Architecture Whitepaper</b></a></p>
    </td>
  </tr>

  <tr>
    <td width="50%" valign="top">
      <h4>🛡️ <a href="https://github.com/disamee/industrial-hse-rag-case-study">OzenMunayGas HSE Assistant</a></h4>
      <p><b>Domain:</b> Industrial Safety Compliance (KMG)</p>
      <p>Zero-hallucination work permit safety assistant with 400+ LOC prompt guardrails, zero-CORS iframe embed, and automated legal compliance verification.</p>
      <p>
        <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI">
        <img src="https://img.shields.io/badge/Prompt_Engine-a855f7?style=flat-square" alt="Prompt">
        <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker">
        <img src="https://img.shields.io/badge/Audit_Logging-10b981?style=flat-square" alt="Audit">
      </p>
      <p><a href="https://github.com/disamee/industrial-hse-rag-case-study"><b>→ Read Architecture Whitepaper</b></a></p>
    </td>
    <td width="50%" valign="top">
      <h4>🚂 <a href="https://github.com/disamee/epd-shipment-tracking-case-study">EPD Railway Shipment Tracker</a></h4>
      <p><b>Domain:</b> High-Concurrency Logistics Automation</p>
      <p>Distributed headless Selenium Chrome worker pool, async queue processing, automated Excel generation, and Telegram notification bots.</p>
      <p>
        <img src="https://img.shields.io/badge/Selenium_Grid-43B02A?style=flat-square&logo=selenium&logoColor=white" alt="Selenium">
        <img src="https://img.shields.io/badge/Telegram_Bot-26A5E4?style=flat-square&logo=telegram&logoColor=white" alt="Telegram">
        <img src="https://img.shields.io/badge/Python_Async-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
        <img src="https://img.shields.io/badge/Excel_Engine-217346?style=flat-square" alt="Excel">
      </p>
      <p><a href="https://github.com/disamee/epd-shipment-tracking-case-study"><b>→ Read Architecture Whitepaper</b></a></p>
    </td>
  </tr>

  <tr>
    <td width="50%" valign="top">
      <h4>📈 <a href="https://github.com/disamee/agri-economic-dashboard-case-study">AgriDash Real-Time Dashboard</a></h4>
      <p><b>Domain:</b> Full-Stack Financial Data Platform</p>
      <p>FastAPI backend with React 18 frontend, streaming live commodity prices, FX exchange rates, and interactive correlation heatmaps via WebSockets.</p>
      <p>
        <img src="https://img.shields.io/badge/React_18-61DAFB?style=flat-square&logo=react&logoColor=black" alt="React">
        <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI">
        <img src="https://img.shields.io/badge/Recharts-22C55E?style=flat-square" alt="Recharts">
        <img src="https://img.shields.io/badge/TailwindCSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white" alt="Tailwind">
      </p>
      <p><a href="https://github.com/disamee/agri-economic-dashboard-case-study"><b>→ Read Architecture Whitepaper</b></a></p>
    </td>
    <td width="50%" valign="top">
      <h4>💰 <a href="https://github.com/disamee/microfinance-aggregator-case-study">Microfinance Aggregator Engine</a></h4>
      <p><b>Domain:</b> FinTech &amp; Regulatory Compliance</p>
      <p>Microfinance comparison engine integrated with ARDFM regulatory standards, loan rate history tracking, and multi-lingual i18n localization.</p>
      <p>
        <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI">
        <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL">
        <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" alt="Redis">
        <img src="https://img.shields.io/badge/i18n-8B5CF6?style=flat-square" alt="i18n">
      </p>
      <p><a href="https://github.com/disamee/microfinance-aggregator-case-study"><b>→ Read Architecture Whitepaper</b></a></p>
    </td>
  </tr>
</table>

---

### 🛠️ Production Tech Stack Matrix

```
┌──────────────────────────────┬──────────────────────────────────────────────────────────────┐
│ DOMAIN                       │ TECHNOLOGIES & TOOLS                                         │
├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ 🧠 AI / RAG / Data           │ LangChain · LlamaIndex · PyTorch · BM25 · ChromaDB · Qdrant  │
│                              │ Embeddings · Cross-Encoder Rerankers · Strict Guardrails     │
├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ ⚡ Systems & Backend          │ Python 3.11+ · FastAPI · Celery · Redis · PostgreSQL · SQL   │
│                              │ SQLAlchemy · AsyncIO · WebSockets · Distributed Task Queues  │
├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ 💻 Frontend & Visualization  │ TypeScript · JavaScript · React 18 · Next.js · Vite · Recharts│
│                              │ Tailwind CSS · Radix UI · WebSocket Clients · i18n           │
├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ 🛡️ Cloud, DevOps & Scraping  │ Kubernetes · Helm · Docker · Docker Compose · Gateway API    │
│                              │ GitHub Actions CI/CD · Selenium Headless · Linux / Bash      │
└──────────────────────────────┴──────────────────────────────────────────────────────────────┘
```

---

### 🎯 Fast-Track for Recruiters & Engineering Leadership

* **Immediate Value Add**: Full-cycle architectural ownership — capable of taking an ambiguous problem statement from research/POC to resilient, production-hardened K8s deployment in weeks.
* **Domain Fluency**: Proven execution in high-stakes domains (Energy/Oil &amp; Gas, FinTech, Commodity Trading, Regulatory Compliance).
* **Work Arrangement**: Open to **Staff / Senior AI Engineer, Systems Architect, or Lead Full-Stack Roles** (Remote Global / Hybrid / Relocation).
* **Languages**: English (Professional / Technical), Russian (Native).

<p align="center">
  <a href="https://linkedin.com"><b>Connect on LinkedIn</b></a> • 
  <a href="https://t.me"><b>Message on Telegram</b></a> • 
  <a href="mailto:meiram@example.com"><b>Send Email</b></a>
</p>
