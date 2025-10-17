import os
from gtts import gTTS

os.makedirs("audio", exist_ok=True)

LANGUAGE = 'en'

print("🔊 Mengunduh suara huruf A-Z dari Google...")

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    filename = f"audio/{letter}.mp3"
    if not os.path.exists(filename):
        try:
            tts = gTTS(text=letter, lang=LANGUAGE, slow=False)
            tts.save(filename)
            print(f"✅ {letter} disimpan")
        except Exception as e:
            print(f"❌ Gagal mengunduh {letter}: {e}")

print("🎵 Semua file audio siap di folder 'audio/'")