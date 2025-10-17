import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands

def extract_landmarks(image):
    """
    Ekstrak 21 landmark tangan dari gambar OpenCV (BGR).
    Return: array (63,) atau None jika tangan tidak terdeteksi.
    """
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    with mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=1,
        min_detection_confidence=0.5
    ) as hands:
        results = hands.process(rgb)
        if results.multi_hand_landmarks:
            landmarks = []
            for lm in results.multi_hand_landmarks[0].landmark:
                landmarks.extend([lm.x, lm.y, lm.z])
            return np.array(landmarks)
    return None