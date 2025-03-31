import requests

def test_payloads(payloads, url):
    results = []
    for p in payloads:
        try:
            r = requests.get(url, params={"input": p}, timeout=10)
            reflected = p in r.text
            results.append({"payload": p, "reflected": reflected})
        except Exception as e:
            results.append({"payload": p, "reflected": False, "error": str(e)})
    return results
