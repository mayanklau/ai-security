import openai
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def tag_payloads(payloads):
    tagged = []
    for p in payloads:
        try:
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Tag this payload as XSS, SQLi, LFI, RCE, or Unknown. Also rate its risk level as High, Medium, or Low."},
                    {"role": "user", "content": f"Payload: {p}"}
                ]
            )
            tag = res.choices[0].message.content
        except Exception as e:
            tag = f"ERROR: {e}"
        tagged.append({"payload": p, "tag": tag, "time": datetime.now().isoformat()})
    return tagged
