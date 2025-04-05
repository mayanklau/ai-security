import requests

url = input("Enter website URL again: ")

with open("payloads.txt", "r") as f:
    payloads = f.readlines()

results = []
for payload in payloads:
    test_payload = payload.strip()
    response = requests.get(url, params={"input": test_payload})
    if test_payload in response.text:
        results.append(f"Potential issue detected with payload: {test_payload}")
    else:
        results.append(f"No obvious issue for payload: {test_payload}")

with open("results.txt", "w") as f:
    f.write("\n".join(results))

print("Testing complete. Check results.txt for findings.")
