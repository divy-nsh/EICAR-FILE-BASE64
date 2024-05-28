import base64

with open("<file>", "rb") as f:
    encodedZip = base64.b64encode(f.read())
    print(encodedZip.decode())
