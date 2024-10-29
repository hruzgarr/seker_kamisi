import os

# Kendi dizininizi belirleyin
folder_path = r"C:\Users\PC\Desktop\seker_kamisi"

# Klasördeki tüm dosyaları listele
for dirname, _, filenames in os.walk(folder_path):
    for filename in filenames:
        print(os.path.join(dirname, filename))  # Dosya yolunu yazdır

