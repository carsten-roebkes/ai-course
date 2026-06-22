from google import genai
from google.genai import types
import json

comments = [
    "I was charged twice and support has ignored my emails for a week. Furious.",
    "Honestly the new dashboard is fantastic, saved me hours. Thank you!",
    "How do I reset my password?",
]

client = genai.Client()

for comment in comments:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=comment,
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
        print("---")
        print("Comment:", comment)
        print("Sentiment:", data["sentiment"])
        print("Category:", data["category"])
        print("Urgency:", data["urgency"])
        if data["sentiment"] == "negative" and data["urgency"] == "high":
            print("🚨 ALERT: escalate this to a human now.")
    except json.JSONDecodeError:
        print("Could not parse the model's reply for this comment.")