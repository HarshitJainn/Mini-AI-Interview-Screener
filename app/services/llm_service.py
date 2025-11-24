import os
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
from typing import Dict
import json
import re



# Load API Key

GENAI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GENAI_API_KEY)

model = genai.GenerativeModel("models/gemini-2.5-flash")



# Prompt Template


EVALUATION_PROMPT = """
You are an expert technical interviewer.

Evaluate the candidate's answer based on 4 categories:

1. clarity_score (1–5)
2. correctness_score (1–5)
3. depth_score (1–5)
4. communication_score (1–5)

Then compute a final "score" between 1 and 5
based on the average of the four category scores (round to nearest integer).

You must ALWAYS return a JSON object in the EXACT format:

{{
  "score": <1–5 integer>,
  "clarity_score": <1–5 integer>,
  "correctness_score": <1–5 integer>,
  "depth_score": <1–5 integer>,
  "communication_score": <1–5 integer>,
  "summary": "<one-line summary>",
  "improvement": "<one improvement suggestion>"
}}

Candidate answer:
\"\"\"{answer}\"\"\"
"""


# LLM Evaluation Function


async def evaluate_with_llm(answer: str) -> Dict:
    try:
        # Insert answer into prompt
        prompt = EVALUATION_PROMPT.format(answer=answer)

        print("\n\nSENDING TO GEMINI >>>\n", prompt)

        # Run Gemini
        response = model.generate_content(prompt)

        raw_output = response.text
        print("\n\nRAW GEMINI OUTPUT >>>\n", repr(raw_output), "\n")

       
        # JSON CLEANUP (same logic, Gemini sometimes over-talks)
        

        cleaned = raw_output.strip()

        if cleaned.startswith('"score"'):
            cleaned = "{ " + cleaned + " }"

        cleaned = cleaned.replace("```json", "").replace("```", "")

        json_match = re.search(r"{[\s\S]*}", cleaned)
        if json_match:
            return json.loads(json_match.group(0))

        if '"score"' in cleaned:
            return json.loads("{\n" + cleaned + "\n}")

        raise ValueError(f"Could not parse JSON from Gemini output:\n{raw_output}")

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise
