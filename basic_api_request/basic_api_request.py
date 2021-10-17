import requests

r = requests.get("https://www.google.com")

print(r.headers)
print(r.status_code)
print(r.text)
print(r.raw)
print(r.reason)
print(r.request)
