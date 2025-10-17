from src.data_loader import load_dataset

DATA_DIR = "data/raw/asl_alphabet"

print("Memulai uji muat dataset...")

X, y = load_dataset(DATA_DIR)

print(f"Dataset berhasil dimuat!")
print(f"Jumlah sampel: {len(X)}")
print(f"Kelas unik: {sorted(set(y))}")
print(f"Jumlah kelas: {len(set(y))}")

if len(X) > 0:
    print(f"\n Nilai:")
    print(X[0])
    print(f"Label: {y[0]}")