
import cv2
import joblib
import numpy as np
import os
import time
import pygame
from .feature_extractor import extract_landmarks

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(SCRIPT_DIR, "..", "models", "sibi_model.pkl")
AUDIO_DIR = os.path.join(SCRIPT_DIR, "..", "audio")

pygame.mixer.init()

last_played = ""
last_played_time = 0
PLAY_DELAY = 2.0

def draw_hand_landmarks(frame, landmarks):
    """
    Gambar landmark tangan dan bounding box.
    landmarks: array 63 nilai [x0,y0,z0, x1,y1,z1, ...]
    """
    if landmarks is None:
        return frame

    import mediapipe as mp
    from mediapipe.framework.formats import landmark_pb2

    h, w, _ = frame.shape

    landmark_list = landmark_pb2.NormalizedLandmarkList()
    for i in range(0, len(landmarks), 3):
        x, y, z = landmarks[i], landmarks[i+1], landmarks[i+2]
        landmark_list.landmark.add(x=x, y=y, z=z)

    mp.solutions.drawing_utils.draw_landmarks(
        frame,
        landmark_list,
        mp.solutions.hands.HAND_CONNECTIONS,
        mp.solutions.drawing_styles.get_default_hand_landmarks_style(),
        mp.solutions.drawing_styles.get_default_hand_connections_style()
    )

    xs = [lm.x * w for lm in landmark_list.landmark]
    ys = [lm.y * h for lm in landmark_list.landmark]
    x_min, x_max = int(min(xs)), int(max(xs))
    y_min, y_max = int(min(ys)), int(max(ys))

    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
    cv2.putText(frame, "TANGAN", (x_min, y_min - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame

def main():
    global last_played, last_played_time

    if not os.path.exists(MODEL_PATH):
        print("❌ Model belum dilatih! Jalankan 'python -m src.train_model' dulu.")
        return

    if not os.path.exists(AUDIO_DIR):
        print("❌ Folder audio tidak ditemukan! Jalankan 'generate_google_audio.py' dulu.")
        return

    model = joblib.load(MODEL_PATH)
    cap = cv2.VideoCapture(0)
    print("📷 Tekan ESC untuk keluar.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        landmarks = extract_landmarks(frame)

        prediction = "..."
        if landmarks is not None:
            pred = model.predict([landmarks])[0]
            prediction = pred.upper()

            current_time = time.time()
            if (prediction != last_played and 
                (current_time - last_played_time) > PLAY_DELAY and
                prediction.isalpha() and len(prediction) == 1):

                audio_file = os.path.join(AUDIO_DIR, f"{prediction}.mp3")
                if os.path.exists(audio_file):
                    last_played = prediction
                    last_played_time = current_time
                    print(f"🔊 Memutar: {prediction}")
                    pygame.mixer.music.load(audio_file)
                    pygame.mixer.music.play()

            frame = draw_hand_landmarks(frame, landmarks)

        cv2.putText(frame, f"SIBI: {prediction}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
        cv2.imshow("SIBI Translator", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    pygame.mixer.quit()

if __name__ == "__main__":
    main()