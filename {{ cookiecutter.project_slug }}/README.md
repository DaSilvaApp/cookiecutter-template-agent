# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

---

## 🚀 Overview

This is a Python project template created using Cookiecutter.


## 🧱 Project Structure

├── config/         # Environment settings (Dev/Stg/Prod) & System Prompts
├── data/           # Persistence layer (Raw docs & Vector Store)
├── src/
│   ├── api/        # Independent REST API (FastAPI) & App DB
│   ├── core/       # Orchestration Engine & reasoning flow
│   ├── services/   # Functional Workers (Agents, RAG, LLM, Tools)
│   ├── schema/     # Pydantic validation models
|   └── utils/      # Helper functions 
└── tests/          # Unit, integration, and RAG testing

## 🚀 Getting Started

### 1. Install dependencies
- uv sync

### 2. Environment Variables
- Copy .env.example and add your own values:
- cp .env.example .env

### 3. Run the app
- uv run app

### 🚀 Running the project
This project uses `uv run` to start the app.

✅ **Important:**  
If you want `uv run` to start your app, you must define a script in `pyproject.toml`.

#### 🔹 Option 1 — Run a Python script
- Add this to `pyproject.toml`:
[tool.uv.scripts]
run = "python src/main.py"

- Then run: uv run run

#### 🔹 Option 2 — Run a FastAPI server
- Add this to pyproject.toml:
[tool.uv.scripts]
run = "uvicorn src.main:app --reload --host 0.0.0.0 --port 8000"

- Then run: uv run run

## Setup (Docker Compose) - To run the app manually
1. Build and start the services
    - docker compose up --build

2. Open your app
    - FastAPI will be available at: http://localhost:8000

3. Stop the services
    - docker compose down

## 🧑‍💻 Setup (Devcontainer) - Development

This project includes a Devcontainer configuration.

1. Open the project in VS Code
Open the Command Palette: Ctrl+Shift+P

2. Choose:
Remote-Containers: Reopen in Container

VS Code will build the container and set up the environment automatically.

### Rule of thumb for the Dockerfile
- VS Code DevContainer -> .devcontainer/Dockerfile
- CI / production / cloud -> Dockerfile

## 🧠 Metadata

Author: {{ cookiecutter.author_name }}

Python version: {{ cookiecutter.python_version }}

Project slug: {{ cookiecutter.project_slug }}

## 📚 Documentation

See the docs/ folder for additional documentation.

## ⚖️ License

 This project is licensed under the MIT License.

