# Scenario Generator API

This is a FastAPI-based microservice for generating emotionally intelligent workplace conversation scenarios using Google Gemini LLM.

## ✨ Features

- Strict scenario schema compliance
- LLM-driven generation using Gemini
- Dockerized for deployment
- Built with modular, testable architecture
- Input validation + section enforcement (11-section prompt)

---

## 📦 Tech Stack

- Python 3.11
- FastAPI
- Google Gemini (Generative Language API)
- Pydantic
- Docker
- httpx

---

## 🚀 How to Run

1. **Clone**

```bash
git clone https://github.com/your-repo/scenario-generator
cd scenario-generator
```

2. **Set up the environment**

```bash
# Put your GEMINI_API_KEY in .env
```

3. **Build and run with Docker**

```bash
docker build -t scenario-generator .
docker run -p 8000:8000 --env-file .env scenario-generator
```