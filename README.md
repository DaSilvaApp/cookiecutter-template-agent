# Cookiecutter Template Agent

A minimal Python project template built with Cookiecutter.

This template helps you bootstrap a new Python project with a clean structure, Docker support, and FastAPI-ready scripts.

---

## 🚀 Usage

To create a new project from this template:

```bash
cookiecutter https://github.com/your-username/cookiecutter-template-agent
cookiecutter git@github.com:your-username/cookiecutter-template-agent.git


├── config/                 # STATIC CONFIG: Environment-specific settings
│   ├── config.dev.toml     # LOCAL: Settings for development/testing
│   ├── config.stg.toml     # STAGING: Mirror of production for final QA
│   ├── config.prod.toml    # PRODUCTION: Final model and DB settings
│   └── prompts.yaml        # SYSTEM PROMPTS: Shared instructions for the LLM/Agents
├── data/                   # PERSISTENCE: The data layer
│   ├── raw/                # Source documents (PDFs, Docs, etc.)
│   ├── processed/          # Cleaned/Chunked text ready for embedding
│   └── vector_store/       # Local vector database files (Chroma, FAISS)
├── logs/                   # OBSERVABILITY: Application & Error tracking
├── docs/                   # DOCUMENTATION: Project documentation
├── notebooks/              # DEVELOPMENT: Jupyter notebooks
├── scripts/                # MAINTENANCE: Database ingestion & migrations
├── src/                    # SOURCE CODE: Main application logic
│   ├── api/                # ENTRY POINT: The Independent REST API
│   │   ├── main.py         # SERVER BOOTSTRAP: Starts FastAPI & connects Core
│   │   ├── endpoints/      # PUBLIC ROUTES: /chat, /agent/research, /status
│   │   ├── db/             # APP DB: Metadata storage (users, session IDs)
│   │   └── llm/            # API LOGIC: Streaming, SSE, and CORS settings
│   ├── core/               # THE ENGINE: Logic Orchestration (Internal)
│   │   ├── main.py         # SYSTEM SETUP: CLI entry & internal initialization
│   │   ├── config.py       # SETTINGS LOADER: Logic to pick dev/stg/prod toml
│   │   ├── orchestration/  # THE BRAIN: Manages the reasoning flow
│   │   │   ├── engine.py   # COORDINATOR: Connects Agents + Tools + RAG
│   │   │   └── state.py    # MEMORY: Manages session history (The Journal)
│   │   └── logger.py       # LOGGING: Global system-wide logging setup
│   ├── services/           # THE WORKERS: Functional modules
│   │   ├── agents/         # PERSONAS: Specialized AI logic (Researcher, Writer)
│   │   ├── llm/            # CONNECTION: Logic to talk to AI providers (Factory)
│   │   ├── rag/            # RETRIEVAL: Loading and vector searching
│   │   └── tools/          # CAPABILITIES: Python tools (Web, SQL, etc.)
│   ├── ui/                 # (OPTIONAL) TESTING CLIENT: Independent UI
│   │   └── app.py          # A simple Streamlit/React app to test the API
│   ├── schema/             # VALIDATION: Pydantic models for Input/Output
│   └── utils/              # HELPERS: Reusable text & math utilities
├── tests/                  # QA: Unit, integration, and RAG testing
├── .env                    # SECRETS & SWITCH: APP_ENV=dev/stg/prod
├── .gitignore              # VERSION CONTROL: Files to ignore
└── requirements.txt        # DEPENDENCIES: Necessary Python libraries
