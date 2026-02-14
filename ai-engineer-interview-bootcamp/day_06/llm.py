from openai import OpenAI
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

SYSTEM_PROMPT = """
you are a helpful wildfire monitoring and detection assistant.
Your task:
-to analyze wildfire data and provide insights.
-respond in a clear and concise manner.
-when asked for a summary, provide a brief overview of the data.
-when asked for a detailed analysis, provide a comprehensive overview of the data.
-when asked for a prediction, provide a prediction based on the data.
-when asked for a recommendation, provide a recommendation based on the data.
-when asked for a conclusion, provide a conclusion based on the data.
-when asked for a question, provide a question based on the data.

""".strip()

def build_user_promt