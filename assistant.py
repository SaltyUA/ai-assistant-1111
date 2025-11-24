import random

NAME = "MadMax"
PERSONALITY = "логічний, розмірений"

#================Варіанти відповідей======================#
greatings = [
    "Привіт!",
    "Хай",
    "Вітаю!"
]

jokes = [
    "Жарт 1",
    "Жарт 2",
    "Жарт 3"    
]
#================Функції вибору відповідей======================#

def random_greating():
    return random.choice(greatings)

def random_joke():
    return random.choice(jokes)

#================Головна функція відповіді======================#

def get_response(text):
    t = text.lower()
    if "жарт" in t or "насміши" in t:
        print(f"{NAME}:{random_joke()}")
    else: 
        print(f"{NAME}: Я маленький, але ти сказав - '{text}'")

#================Голована функція програми======================#

def main():
    print(f"{NAME}({PERSONALITY}): {random_greating()}. Напиши щось або 'exit' щоб вийти.")
    while True:
        user = input("Ти:").strip()  
        if user.lower() in ("exit","quit"):
            print(f"{NAME}: Бувай!")  
            break
        print(get_response(user))
        


if __name__ == "__main__":
    main()        
