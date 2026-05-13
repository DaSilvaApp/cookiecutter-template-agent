# Cookiecutter Template Agent

A minimal Python project template built with Cookiecutter.

This template helps you bootstrap a new Python project with a clean structure, Docker support, and FastAPI-ready scripts.

---

## 🚀 Usage

To create a new project from this template:

cookiecutter https://github.com/your-username/cookiecutter-template-agent
cookiecutter git@github.com:your-username/cookiecutter-template-agent.git



# ⚙️ CONFIGURATION (env configs + system prompts)
├── config/
│   ├── config.dev.toml
│   ├── config.stg.toml
│   ├── config.prod.toml
│   └── prompts.yaml

# 📦 LOCAL DEV ONLY (NOT production)
# Used for offline testing, mock data, local vector DBs
├── data/
│   ├── raw/
│   ├── processed/
│   └── vector_store/

# 📜 LOGS (application + debugging)
├── logs/

# 📚 DOCUMENTATION
├── docs/

# 🧰 DEV / MAINTENANCE SCRIPTS
├── scripts/


# 🌐 API LAYER (HTTP entrypoint)
├── api/
│   ├── main.py
│   ├── endpoints/
│   ├── middleware.py              # auth hooks, rate limiting
│   └── db.py                     # lightweight metadata access only


# 🧠 CORE ORCHESTRATION ENGINE (stateless brain)
├── core/
│   ├── engine.py                 # request orchestration
│   ├── memory.py                 # session context builder
│   ├── prompts/
│   ├── schemas/
│   └── telemetry.py              # tokens, cost, tracing hooks


# ⚙️ CAPABILITIES LAYER (LLM + RAG + tools)
├── services/
│   ├── agents/
│   ├── llm/
│   ├── rag/
│   ├── tools/
│   └── prompts_registry.py       # prompt versions + experiments


# 💾 STATE LAYER (PRODUCTION MEMORY + DATA ABSTRACTION)
├── state/
│   ├── users/                    # identity + preferences
│   ├── sessions/                 # conversation history
│   ├── memory/                   # long-term + summaries
│   ├── billing/                  # token + cost tracking
│   │
│   └── storage/                 # 🔌 production DB adapters
│       ├── postgres.py          # users, sessions, billing
│       ├── redis.py             # cache + session + queues
│       └── vector_db.py         # embeddings + retrieval


# 🚀 BACKGROUND JOB SYSTEM (ASYNC WORKERS)
├── workers/
│   ├── celery_app.py
│   ├── tasks.py
│   └── jobs/
│       ├── ingestion.py         # document ingestion pipeline
│       ├── embeddings.py        # embedding generation
│       └── memory.py            # memory summarization


# 🔐 AUTHENTICATION + SECURITY
├── auth/
│   ├── jwt.py
│   ├── permissions.py
│   └── rate_limits.py


# 🧪 LLM EVALUATION SYSTEM (quality control)
├── evals/
│   ├── datasets/
│   ├── runners/
│   └── metrics/


# 📊 OBSERVABILITY (logs, metrics, tracing)
├── observability/
│   ├── logging.py
│   ├── metrics.py
│   └── tracing.py


# 🖥️ OPTIONAL DEV UI
├── ui/


# 🧪 TESTING STRATEGY
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── api/
│   ├── rag/
│   ├── workers/
│   └── fixtures/


# 🐳 INFRASTRUCTURE (DEPLOYMENT)
├── infra/
│   ├── docker/
│   │   ├── Dockerfile            # main API container
│   │   └── docker-compose.yml    # full stack (api + worker + db + redis)
│   ├── ci/                       # CI/CD pipelines
│   └── scripts/                  # deploy helpers


# 🔐 ENV + PROJECT CONFIG
├── .env.example
└── README.md
