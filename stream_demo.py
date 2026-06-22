from google import genai

client = genai.Client()

question = input("Ask me anything: ")

response = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents=question
)

for chunk in response:
    print(chunk.text, end="", flush=True)

print()