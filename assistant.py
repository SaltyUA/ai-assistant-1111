import random

NAME = "TDerden"
PERSONALITY = "хаотичний, різкий, без правил"

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

#================Головна функція відповіді======================#

def get_response(text):
    t = text.lower()

    if "жарт" in t or "насміши" in t:
        return random_joke()

    elif "мотив" in t or "підтримай" in t:
        return random_motivation()

    elif "хто ти" in t or "про себе" in t:
        return random_personal()

    else:
        return f"Ти сказав: '{text}'. Цікаво, але робити щось будеш?"
#================Голована функція програми======================#

def main():
    print(f"{NAME} ({PERSONALITY}): {random_greeting()}")
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
