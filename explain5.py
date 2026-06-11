from google import genai
from google.genai import types
import json

topic = input("What should I explain? ")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=topic,
    config=types.GenerateContentConfig(
        system_instruction="You are a teacher. For the given topic, return a simple explanation, a difficulty level, and a fun fact.",
        thinking_config=types.ThinkingConfig(thinking_budget=0),
        response_mime_type="application/json",
        response_schema={
            "type": "object",
            "properties": {
                "explanation": {"type": "string"},
                "difficulty": {"type": "string"},
                "fun_fact": {"type": "string"}
            }
        }
    )
)

data = json.loads(response.text)

print("Explanation:", data["explanation"])
print("Difficulty:", data["difficulty"])
print("Fun fact:", data["fun_fact"])

