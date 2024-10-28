import requests

api_key = '3f2a964e-2e88-4cbf-ab7c-eb244b3d5b7e'
word = 'potato'
root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
final_url = f'{root_url}/{word}?key={api_key}'
r = requests.get(final_url)
result = r.json()
print(result)