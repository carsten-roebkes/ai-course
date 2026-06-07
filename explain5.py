from google import genai
topic = input("What should I explain? ")
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"Explain {topic} in 3 simple sentences, like I'm five."
)

print(response.text)
print(f"Tokens used: {response.usage_metadata.total_token_count}")
