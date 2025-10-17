# 🇮🇩 SIBI Translator – Penerjemah Bahasa Isyarat Indonesia Real-Time

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8-green?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.5-orange?logo=google)
![License](https://img.shields.io/badge/License-MIT-purple)

> **Tangan Bicara, Teknologi Mendengar.**  
> Aplikasi ini menerjemahkan **Bahasa Isyarat Indonesia (SIBI)** secara real-time menggunakan kamera — mengubah gerakan tangan menjadi teks dan suara untuk membangun komunikasi yang lebih inklusif.

---

## 🌟 Fitur Utama

- ✅ Deteksi isyarat SIBI: **abjad (A–Z)**
- ✅ Visualisasi tangan: **landmark, garis jari, dan bounding box**
- ✅ Output teks real-time di layar kamera
- ✅ Suara alami dari **Google Text-to-Speech (gTTS)**
- ✅ Ringan — berjalan di laptop biasa (tanpa GPU)
- ✅ Dataset asli SIBI dari [LEMLITBANG SIBI (Kaggle)](https://www.kaggle.com/datasets/mlanangafkaar/datasets-lemlitbang-sibi-alphabets)

---

## 📂 Struktur Folder

Repositori ini dirancang agar mudah dikembangkan:

```
sibi-translator/
├── data/                 # Tempat dataset
│   └── .gitkeep
├── models/               # Tempat model terlatih
│   └── .gitkeep
├── src/                  # Kode sumber utama
├── audio/                # File suara (A.mp3, B.mp3, ...)
├── generate_google_audio.py
├── test_load.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🚀 Cara Menjalankan

### Prasyarat
- Python 3.11 (disarankan)
- Webcam
- Koneksi internet (untuk generate suara Google TTS)

### Langkah Instalasi
1. **Clone repositori ini:**
```
git clone https://github.com/namamu/sibi-translator.git
cd sibi-translator
```

2. **Buat virtual environment & install dependensi:**
```
python -m venv sibi_env
sibi_env\Scripts\activate        # Windows
pip install -r requirements.txt
```

3. **Siapkan dataset:**
   - Unduh dataset SIBI dari [Kaggle](https://www.kaggle.com/datasets/mlanangafkaar/datasets-lemlitbang-sibi-alphabets)
   - Ekstrak ke: `data/raw/sibi_alphabet/`

4. **(Opsional) Generate suara huruf:**
```
python generate_google_audio.py
```

5. **Latih model:**
```
python -m src.train_model
```

6. **Jalankan aplikasi:**
```
python -m src.app
```

> 📝 Tekan **ESC** untuk keluar dari aplikasi.

---

## 🙏 Ucapan Terima Kasih

- Terima kasih kepada **komunitas tunarungu Indonesia** atas keberadaan SIBI.
- Terima kasih kepada **Google MediaPipe**, **OpenCV**, **scikit-learn**, dan **pygame**.
- Terima kasih kepadamu — karena peduli pada teknologi yang bermakna.

---

## 🙋‍♂️ Tentang Pembuat

<p align="center">
  Created by <strong>Gading Khairlambang</strong> – aspiring data scientist 🚀
</p>
