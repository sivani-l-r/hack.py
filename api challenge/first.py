import requests

base_url="https://catfact.ninja.fact"
try:

    r = requests.get(base_url,timeout=10)
except requests.ConnectionError


print(r.stattus_code)

if r.status_code!=200:
    print("ivalid url")
    exit(1)

