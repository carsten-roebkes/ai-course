from google import genai
from google.genai import types
import json

feedback = input("Paste the customer comment: ")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=feedback,
    config=types.GenerateContentConfig(
        system_instruction="You analyze customer feedback. For the given comment, return the sentiment, a category, and an urgency level.",
        thinking_config=types.ThinkingConfig(thinking_budget=0),
        response_mime_type="application/json",
        response_schema={
            "type": "object",
            "properties": {
                "sentiment": {"type": "string", "enum": ["positive", "neutral", "negative"]},
                "category": {"type": "string"},
                "urgency": {"type": "string", "enum": ["low", "medium", "high"]}
            }
        }
    )
)

try:
    data = json.loads(response.text)
    print("Sentiment:", data["sentiment"])
    print("Category:", data["category"])
    print("Urgency:", data["urgency"])
    if data["sentiment"] == "negative" and data["urgency"] == "high":
        print("🚨 ALERT: escalate this to a human now.")
except json.JSONDecodeError:
    print("Sorry — the model didn't return valid data. Here's what it sent:")
    print(response.text)

