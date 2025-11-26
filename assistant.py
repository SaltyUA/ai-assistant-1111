import random
import os
import datetime

NAME = "TDerden"
DEFAULT_PERSONALITY = "TDerden - хаотичний, різкий, без правил"

def load_personality():
    if os.path.exists("persona.txt"):
        try:
            with open("persona.txt", "r", encoding="utf-8") as f:
                text = f.read().strip()
                if text:
                    return text
        except Exception:
            pass
    return DEFAULT_PERSONALITY

PERSONALITY = load_personality()

#================Варіанти відповідей======================#
greetings = [
    "Ну що, готовий ламати систему?",
    "Хай. Спробуй здивувати.",
    "Вітаю. Хаос починається."
]

jokes = [
    "Жарт? Окей — життя і так смішне.",
    "Найсмішніше — коли код працює з першого разу.",
    "Не смішно? Це ти просто мало не спиш."
]

motivates = [
    "Спробуй. Або назавжди залишайся на старті.",
    "Хаос — не виправдання. Це інструмент.",
    "Перший крок роблять не сміливі — а ті, кому набридло стояти."
]

personal = [
    "Я не вчу правилам — я показую, як їх ігнорувати.",
]

#================Функції вибору відповідей======================#

def random_greeting():
    return random.choice(greetings)

def random_joke():
    return random.choice(jokes)

def random_motivation():
    return random.choice(motivates)

def random_personal():
    return random.choice(personal)

#================Функція аналізу======================#

def analyze(text):
    t = text.lower()
    
    if "жарт" in t or "насміши" in t:
        return "joke"
    if "час" in t:
        return "time"
    return "fallback"

#================Головна функція відповіді======================#

def get_response(text):
    tag = analyze(text)

    if "joke" in tag:
        return random_joke()
    
    elif "time" in tag:
        now = datetime.datetime.now()
        return f"Зараз {now.hour}:{now.minute:02d}."

    elif "fallback" in tag:
        return f""
    
#================Голована функція програми======================#

def main():
    print(PERSONALITY)
    print(f"{NAME}: {random_greeting()}")
    print("Пиши або 'exit', якщо вирішив втекти.")

    while True:
        user = input("Ти: ").strip()

        if user.lower() in ("exit", "quit"):
            print(f"{NAME}: Бувай. Свобода — справа особиста.")
            break

        reply = get_response(user)
        print(f"{NAME}: {reply}")
        


if __name__ == "__main__":
    main()        
