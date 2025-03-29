import openai
import os

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    api_key = input("Enter your OpenAI API key securely: ")

openai.api_key = api_key

with open("site_content.txt", "r") as f:
    content = f.read()

prompt = f"Suggest 3 simple test payloads for vulnerabilities (XSS, SQL Injection, Directory Traversal) based on this text: {content[:2000]}"

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": prompt}]
)

payloads = response.choices[0].message.content

with open("payloads.txt", "w") as f:
    f.write(payloads)

print("Payloads generated and saved.")
