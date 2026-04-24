# Customer Support LLM App with Monitoring & Evaluation

This project demonstrates a full **LLM application lifecycle** using FastAPI, MLflow, and automated evaluation.
It covers building, monitoring, and evaluating a customer support AI agent, with an optional Streamlit frontend.

---

## 🚀 Overview

The system consists of:

- Backend API (FastAPI) – serves the LLM agent
- LLM Agent – answers customer support questions
- MLflow Tracking – logs requests, responses, and metrics
- Monitoring Notebook – explores traces and builds datasets
- Evaluation Pipeline – evaluates model outputs using an LLM judge
- Frontend (Streamlit, optional) – simple UI for interacting with the agent

---

## 🧠 Key Concepts

- Prompt management with MLflow
- Trace logging (requests + responses)
- Offline evaluation using datasets
- LLM-as-a-judge evaluation
- MLOps workflow for LLM systems

---

## 📁 Project Structure

```
customer_support/
│
├── src/customer_support/
│   ├── backend/
│   │   ├── api.py
│   │   ├── agents.py
│   │   ├── middlewares.py
│   │   └── constants.py
│   │
│   ├── frontend/
│   │   └── app.py
│   │
│   └── monitoring/
│       ├── mlflow.db
│       ├── eval_data.json
│       ├── mlflow_prompts.ipynb
│       └── mlflow_monitoring.ipynb
│
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## ⚙️ Setup

### 1. Install dependencies

```bash
uv init
uv add ipykernel mlflow pydantic-ai streamlit uvicorn
```

---

### 2. Run the backend

From the backend folder:

```bash
uv run uvicorn api:app --reload
```

---

### 3. Test the API

Open in browser:

```
http://127.0.0.1:8000/docs
```

### 4. Start MLflow UI

`uv run mlflow ui --port 5001`

Open:
http://127.0.0.1:5001


---

## 📊 Monitoring (MLflow)

The app logs:

* request (user prompt)
* response (LLM output)
* latency
* status code

These are stored in:

```
monitoring/mlflow.db
```

---


## 🤖 LLM Evaluation (LLM Judge)

Evaluation is performed using MLflow GenAI:

### Metrics used:

* **Correctness** → factual accuracy
* **Guidelines** → tone, safety, behavior

---

## 🔄 Workflow Summary

1. User sends request → API
2. Agent generates response
3. Middleware logs trace to MLflow
4. Notebook extracts traces
5. Evaluation dataset created
6. LLM judge evaluates outputs

---

## 💡 Key Learnings

* LLM apps need **monitoring + evaluation**, not just deployment
* MLflow can track **LLM traces and datasets**
* Evaluation can be automated using **LLM judges**
* Separation of:

  * serving
  * monitoring
  * evaluation

---

## 🏁 Conclusion

This project demonstrates a complete **LLMOps pipeline**, from building an agent to evaluating its performance using MLflow.

---
