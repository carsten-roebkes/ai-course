from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="In one sentence, what is an API?"
)

print(response.text)
print(response.usage_metadata)
