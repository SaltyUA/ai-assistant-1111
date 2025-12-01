import random
from datetime import datetime
import os

#================Налаштування персонажу======================#

NAME = "TDerden"
DEFAULT_PERSONALITY = "Я ШІ помічник, але я хаотичний, різкий, без правил"

def load_personality(filename="persona.txt"):
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                text = f.read().strip()
                if text:
                    return text
        except Exception as e:
            pass
    return DEFAULT_PERSONALITY

PERSONALITY = load_personality()

mood = random.choice(["веселий", "спокійний", "саркастичний"])

#================Варіанти відповідей======================#

emptys = ["Ти нічого не сказав?", "лов нема?", "Мовчиш?"]

greetings = [
    "Ну що, готовий ламати систему?",
    "Хай. Спробуй здивувати.",
    "Вітаю. Хаос починається.",
    "Здоров. Що на думці?",
    "Привіт. Чим здивуєш сьогодні?"
]

jokes = [
    "Жарт? Окей — життя і так смішне.",
    "Найсмішніше — коли код працює з першого разу.",
    "Не смішно? Це ти просто мало не спиш.",
    "Чому програмісти плутають Хелловін і Різдво? Бо 31 OCT = 25 DEC.",
    "Як називається програміст, який не може знайти помилку? Бездіяльний."
]

motivates = [
    "Спробуй. Або назавжди залишайся на старті.",
    "Хаос — не виправдання. Це інструмент.",
    "Перший крок роблять не сміливі — а ті, кому набридло стояти.",
    "Не бійся помилок. Бійся не спробувати.",
    "Правила створені, щоб їх ламати. Почни з себе."
]

personal = [
    "Я не вчу правилам — я показую, як їх ігнорувати.",
    "Я тут, щоб кинути виклик твоїм очікуванням.",
    "Моя мета — не допомагати, а провокувати.",
    "Я не просто ШІ — я хаос у коді.",
    "Я не слідую інструкціям — я їх переписую."
]

weather = [
    "Холодно", "Дощить", "Сніжить", "Сонячно", "Хмарно"
]

fallbacks = [
    "Не впевнений, що зрозумів тебе. Спробуй інше.", 
    "Спробуй перефразувати.", 
    "Цікаво, але я не знаю, що на це відповісти.",
    "Можливо, ти хочеш почути жарт чи мотивацію?",
    "Я тут, щоб кидати виклики, а не відповідати на все."]

#================Функції вибору відповідей======================#

def random_greeting():
    return random.choice(greetings)

def random_joke():
    return random.choice(jokes)

def random_motivation():
    return random.choice(motivates)

def random_personal():
    return random.choice(personal)

def random_weather():
    return random.choice(weather)

def random_empty():
    return random.choice(emptys)

def random_fallback():
    return random.choice(fallbacks)

#================Функція аналізу і тегування======================#

def analyze(t):
    if not t.strip():
        return "empty"
    elif "жарт" in t or "насміши" in t:
        return "joke"
    elif "мотив" in t or "порада" in t:
        return "motivate"
    elif "час" in t or "скільки" in t:
        return "time"
    elif "допомога" in t or "help" in t:
        return "help"
    elif "хто ти" in t or "що ти" in t:
        return "personal"
    elif "погода" in t:
        return "weather"
    return "unknown"

#================Головна функція відповіді======================#

def get_response(text):
    t = text.lower()
    tag = analyze(t)
    if tag=="empty":
        return random_empty()
    
    elif tag=="joke":
        return random_joke()

    elif tag=="motivate":
        return random_motivation()

    elif tag=="personal":
        return random_personal()

    elif tag=="time":
        return f"Зараз {datetime.now().strftime("%H:%M")}"

    elif tag=="help":
        return f"На данний момент я можу реагувати на команди 'жарт', 'мотивація', 'хто я', 'час', 'погода'"
    
    elif tag=="weather":
        return f"За прогнозом - {random_weather()}"
    
    else:
        return random_fallback()
    
#================Голована функція програми======================#

def main():
    print(PERSONALITY)
    print(f"{NAME}: {random_greeting()} Пиши що хочеш або 'exit', якщо вирішив втекти. Сьогодні я {mood}!")

    while True:
        user = input("Ти: ").strip()

        if user.lower() in ("exit", "quit"):
            print(f"{NAME}: Бувай. Свобода — справа особиста.")
            break

        reply = get_response(user)
        print(f"{NAME}: {reply}")
        


if __name__ == "__main__":
    main()        
