import os
import openai

# Get key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

with open("payloads.txt", "r") as f:
    payloads = f.read().splitlines()

tagged = []

for payload in payloads[:100]:  # Analyze 100 at a time
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tag the payload as XSS, SQLi, LFI, RCE, etc."},
                {"role": "user", "content": f"Payload: {payload}"}
            ]
        )
        tag = response['choices'][0]['message']['content']
        tagged.append(f"{payload}  # {tag}")
    except Exception as e:
        tagged.append(f"{payload}  # ERROR: {e}")

with open("payloads_tagged.txt", "w") as f:
    for line in tagged:
        f.write(line + "\n")

print("Tagged payloads saved to payloads_tagged.txt")
