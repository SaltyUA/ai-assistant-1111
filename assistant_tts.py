# pip install pygame gtts

import os
from gtts import gTTS
import pygame
from time import sleep

# --- Налаштування ---
TEXT_TO_SPEAK = "Як справи?"
LANGUAGE = 'uk'  # Код мови для української
OUTPUT_FILENAME = "temp_audio_pygame.mp3"
# --- Кінець налаштувань ---

def text_to_speech_and_play_pygame(text, lang, filename):
    """
    Перетворює текст на мовлення, зберігає у файл MP3 
    та відтворює його за допомогою pygame.mixer.
    """
    print(f"✅ Генерація TTS для тексту: '{text[:50]}...'")
    
    try:
        # 1. Створення та збереження MP3 за допомогою gTTS
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(filename)
        print(f"Аудіо збережено як '{filename}'")
        
        # 2. Ініціалізація pygame.mixer
        pygame.mixer.init()
        
        # 3. Завантаження та відтворення аудіо
        print("▶️ Відтворення аудіо через Pygame...")
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        
        # 4. Чекаємо, доки відтворення завершиться
        while pygame.mixer.music.get_busy():
            sleep(0.1)
            
        print("⏹️ Відтворення завершено.")
        
    except Exception as e:
        print(f"\n❌ Виникла помилка: {e}")
        print("Можливо, pygame не зміг ініціалізувати мікшер або знайти аудіофайл.")
    finally:
        # 5. Очищення
        if os.path.exists(filename):
            pygame.mixer.quit() # Важливо: зупинити мікшер перед видаленням файлу
            os.remove(filename)
            print(f"Тимчасовий файл '{filename}' видалено.")
        
if __name__ == "__main__":
    text_to_speech_and_play_pygame(TEXT_TO_SPEAK, LANGUAGE, OUTPUT_FILENAME)