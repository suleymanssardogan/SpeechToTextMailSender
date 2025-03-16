import os
import queue
import sounddevice as sd
import vosk
import json

# 📌 Modeli yükle (model dosyanın olduğu yolu güncelle)
MODEL_PATH = r"C:\Users\SuleymanSardogan\Downloads\vosk-model-small-tr-0.3\vosk-model-small-tr-0.3"
if not os.path.exists(MODEL_PATH):
    print("Lütfen modeli indir ve belirtilen klasöre koy.")
    exit(1)

# 📌 Vosk modelini başlat
model = vosk.Model(MODEL_PATH)
samplerate = 16000  # Standart örnekleme oranı

# 📌 Ses kaydı için kuyruk oluştur
q = queue.Queue()


def callback(indata, frames, time, status):
    """Ses verisini kuyruğa ekler"""
    if status:
        print(status, flush=True)
    q.put(bytes(indata))


# 📌 Mikrofonu aç ve sesi al
with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype="int16",
                       channels=1, callback=callback):
    recognizer = vosk.KaldiRecognizer(model, samplerate)

    print("🎙️ Konuşmaya başlayabilirsin... (Çıkış için Ctrl+C)")
    sayac =0
    while sayac<1:
        data = q.get()
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            print("✅ Algılanan Metin:", result["text"])
            sayac  +=1
import pyttsx3

def speak_text(text):
    """Metni sesli olarak okur"""
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Konuşma hızını ayarla
    engine.setProperty("volume", 1.0)  # Ses seviyesini ayarla
    engine.say(text)
    engine.runAndWait()

# Test et
speak_text(result["text"])
