import os
import time

from dotenv import load_dotenv
from google import genai


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


if not API_KEY:
    raise ValueError("Gemini API key is missing")


client = genai.Client(api_key=API_KEY)


def generate_response(prompt: str) -> dict:

    start_time = time.perf_counter()

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    latency = time.perf_counter() - start_time

    return {
        "answer": response.text or "",
        "latency": round(latency, 3)
    }