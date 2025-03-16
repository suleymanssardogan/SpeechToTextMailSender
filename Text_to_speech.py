from gtts import gTTS
import os
import speech_recognition as sr
#pwak oszd oqsg qcpj

recognizer = sr.Recognizer()

# Metni sesli olarak söyleyen fonksiyon
def text_speech(coming_text):
    text = coming_text
    tts = gTTS(text, lang="tr")  # Türkçe dilinde sesli cevap üretir
    tts.save("output.mp3")  # Sesli cevap mp3 formatında kaydedilir
    os.system("start output.mp3")  # Sesli yanıtı oynatmak için komut

# Sesli komutları dinleyip metne dönüştüren fonksiyon
def speech_to_text():
    with sr.Microphone() as source:
        print("Konuşun...")
        recognizer.adjust_for_ambient_noise(source, duration=3)  # Ortam gürültüsünü azaltır
        audio = recognizer.listen(source, phrase_time_limit=10)  # Maksimum 10 saniye dinler

        try:
            text = recognizer.recognize_google(audio, language="tr-TR")  # Türkçe dilinde tanıma yapar
            return text
        except sr.UnknownValueError:
            print("Ses anlaşılamadı")
            return ""
        except sr.RequestError:
            print("Servise ulaşılamadı")
            return ""

if __name__ == "__main__":
        text = speech_to_text()
        if text:
            print(f"Söylenen: {text}")
            text_speech( text)

