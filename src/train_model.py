import os
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from .data_loader import load_dataset

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data", "raw", "asl_alphabet")
MODEL_PATH = os.path.join(SCRIPT_DIR, "..", "models", "asl_model.pkl")

def main():
    print("Memuat dataset...")
    X, y = load_dataset(DATA_DIR)
    if len(X) == 0:
        print(" gada data ditemuin")
        return

    print(f"✅ Dataset dimuat: {X.shape[0]} sampel, {X.shape[1]} fitur")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print("latih model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    acc = model.score(X_test, y_test)
    print(f"Akurasi: {acc:.2%}")
    print("\nLaporan Klasifikasi:")
    print(classification_report(y_test, model.predict(X_test)))

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Model jadi: {MODEL_PATH}")

if __name__ == "__main__":
    main()