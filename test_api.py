import requests

url = "https://cowrender-api.onrender.com/predict"

headers = {
    "Content-Type": "application/json",
    "x-api-key": "rnd_1lRzmPTQcwsuJ6eleZibGO9ZSLyZ"
}

data = {
    "temperature": 38.5,
    "activity": 2.0
}

response = requests.post(url, json=data, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.text)