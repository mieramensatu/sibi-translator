import os
import cv2
import numpy as np
from src.feature_extractor import extract_landmarks

def load_dataset(data_dir):
    """
    Muat dataset SIBI dari struktur:
        data_dir/
        ├── Gesture Image Data/
        └── Gesture Image Pre-Processed Data/
    
    Setiap subfolder berisi folder huruf: A/, B/, ..., Z/
    
    Return: X (landmarks), y (labels)
    """
    X, y = [], []
    
    main_folders = ['Gesture Image Data', 'Gesture Image Pre-Processed Data']
    
    for main_folder in main_folders:
        main_path = os.path.join(data_dir, main_folder)
        if not os.path.exists(main_path):
            print(f"⚠️  Folder {main_path} tidak ditemukan, dilewati.")
            continue
            
        print(f"🔁 Memproses folder: {main_folder}")
        
        for label in sorted(os.listdir(main_path)):
            label_path = os.path.join(main_path, label)
            if not os.path.isdir(label_path):
                continue
                
            print(f"   Memproses kelas: {label}")
            for img_name in os.listdir(label_path):
                if not img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                    continue
                    
                img_path = os.path.join(label_path, img_name)
                image = cv2.imread(img_path)
                if image is None:
                    continue
                    
                landmarks = extract_landmarks(image)
                if landmarks is not None:
                    X.append(landmarks)
                    y.append(label)
                    
    return np.array(X), np.array(y)