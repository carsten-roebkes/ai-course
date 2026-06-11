from google import genai
from google.genai import types

topic = input("What should I explain? ")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"Explain {topic} in 3 simple sentences, like I'm five.",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0)
    )
)

print(response.text)
print(f"Tokens used: {response.usage_metadata.total_token_count}")
