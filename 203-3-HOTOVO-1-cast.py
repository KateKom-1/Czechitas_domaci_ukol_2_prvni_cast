import json

import requests

ico = input("Zadejte IČO subjektu: ")

response = requests.get("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/" + ico)

data = response.json()

jmeno = data["obchodniJmeno"]
adresa = data["sidlo"]["textovaAdresa"]

print(jmeno)
print(adresa)