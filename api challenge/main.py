import json
import requests

base_url="https://anapioficeandfire.com/api/houses"

try:
    r=requests.get(base_url,timeout=10)
except requests.exceptions.ConnectionError :
    print("Invalid url")
    exit(1)

if r.status_code!=200:
    print("Invalid Url")
    exit(1)

n=int(input("Enter a number whose information you want:"))
n=n-1
response=r.json()[n]


name=response.get("name")
region=response.get("region")
coat=response.get("coatOfArms")

print("""
Name: {name}
Region: {region}
CoatOfArms: {coat}
""".format(name=name,region=region,coat=coat))
