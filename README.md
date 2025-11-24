Absolutely — here is the same README in clean, plain text, no emojis, no code blocks, no YAML formatting.
Just copy and paste directly into GitHub.

---

# Mini AI Interview Screener (Backend Only)

This project is a lightweight backend service that evaluates candidate answers using an LLM (Gemini 2.5 Flash). It produces:

* Category-wise scoring (clarity, correctness, depth, communication)
* Final score (1–5)
* One-line summary
* Improvement suggestion
* Candidate ranking from highest to lowest score

Built using FastAPI, Python, and Google Gemini. Designed for a 48-hour real-world backend challenge.

---

## Features

1. POST /evaluate-answer
   Evaluates a single candidate answer and returns:

   * clarity_score
   * correctness_score
   * depth_score
   * communication_score
   * overall score
   * summary
   * improvement suggestion

2. POST /rank-candidates
   Accepts a list of answers, evaluates each, and returns them sorted by score.

3. Robust JSON parsing of LLM outputs

4. FastAPI-powered backend with automatic API documentation

---

## Tech Stack

* FastAPI
* Python
* Google Gemini 2.5 Flash
* Pydantic
* Uvicorn

---

## Why FastAPI?

* High performance due to async support
* Automatic interactive API docs
* Clean request/response model definitions
* Easy to scale and maintain
* Excellent for LLM-heavy applications

---

## Why Gemini?

OpenAI quota was exhausted, so Gemini was chosen for:

* Availability and generous free tier
* Fast generation
* Reliable structured output
* Strong JSON handling
* Easy integration with Python

---

## Project Structure

mini-ai-screener/
│
├── app/
│   ├── main.py
│   ├── services/llm_service.py
│   ├── models/request_models.py
│   ├── models/response_models.py
│
├── .env.example
├── requirements.txt
└── README.md

---

## Installation and Setup

1. Clone the repository
   git clone [https://github.com/HarshitJainn/Mini-AI-Interview-Screener](https://github.com/HarshitJainn/Mini-AI-Interview-Screener)
   cd mini-ai-screener

2. Create and activate virtual environment
   python -m venv venv
   venv\Scripts\activate  (Windows)

3. Install requirements
   pip install -r requirements.txt

4. Create the .env file (not committed to Git)
   GEMINI_API_KEY=your_real_api_key

5. Start the server
   uvicorn app.main:app --reload

Visit the API documentation at:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Example Usage

### POST /evaluate-answer

Request:
{ "answer": "I built ML models and deployed them using FastAPI." }

Response example:

* score: 4
* clarity_score: 4
* correctness_score: 5
* depth_score: 3
* communication_score: 4
* summary: "Clear and technically correct explanation."
* improvement: "Include more details about model performance."

---

### POST /rank-candidates

Request:
{
"answers": [
"I built ML pipelines in production.",
"I am learning ML basics.",
"I worked on NLP and LLM fine-tuning."
]
}

The endpoint evaluates each answer and returns them sorted by score.

---

## Architecture Overview

1. Client sends answer(s) to FastAPI
2. FastAPI passes the text to Gemini with a structured evaluation prompt
3. Gemini returns a JSON-like response
4. JSON is cleaned and parsed
5. FastAPI returns structured data to the client

---

## Security

* API key stored in .env
* .env added to .gitignore
* No secrets in the repository
* Environment variables loaded securely

---

## Future Enhancements

* Sentiment analysis
* Skill extraction
* Follow-up question generation
* SQLite database for storing candidate evaluations



