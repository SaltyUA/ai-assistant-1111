import requests
import json

API_KEY = "AIzaSyDgPdmLPaUdouJfmpEmphOygYOvoxCx6bQ"

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

headers = {
    "Content-Type" : "application/json",
    "X-goog-api-key": API_KEY
}

payload = {
    "contents": [
        {
        "parts":[
            {
                "text": "Привіт! Хто ти такий? Який у тебе настрій? Як справи?"
                }
        ]   
    
    }
    ]
}

response = requests.post(url, headers=headers, json=payload)

print(response.json()['candidates'][0]['content']['parts'][0]['text'])




