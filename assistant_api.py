
import os
from google import genai
from google.genai import types
import json

SYSTEM_INSTRUCTION = "Ти персональний помічник, розроблений для персонального використання студенто комп'ютерної академії. Твоя задача підказувати, але не виконувати завдання замість користувача. Відповідай українською мовою."


def get_messages():
    if os.path.exists("messages.json"):
        try:
            with open("messages.json", "r", encoding="utf-8") as f:
                t = f.read().strip()
                if not t:
                    return []
                return json.loads(t)
        except json.JSONDecodeError:
            return []
        except Exception:
            return []
    return []


def save_messages(messages):
    with open("messages.json", "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)


client = genai.Client(api_key="AIzaSyAZBdPxbuppZTj4JrHs9LH-NgrE41TAU2Q")


def main():    
    global messages
    messages = get_messages()
    
    config  = types.GenerateContentConfig(
        system_instruction = SYSTEM_INSTRUCTION,
    )
    
    print(messages)
    while True:
        user_input = input("Ти: ").strip() 
        if not user_input:
            print("Будь ласка, введіть повідомлення.")
            continue
        messages.append({"role": "user", "content": user_input})
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input,
            config=config,
        )
        response_message = response.text
        messages.append({"role": "model", "content": response_message})
        print("Jarvis:", response_message)
        save_messages(messages)
       
        
if __name__ == "__main__":  
    main()