# pyrefly: ignore[missing-import]
import numpy as np

np.random.seed(42)
# NDVI sebelum & sesudah (grid 10x10), nilai tinggi = vegetasi lebat
sebelum = np.random.uniform(0.6, 0.9, (10, 10))
sesudah = sebelum.copy()
sesudah[3:6, 3:6] -= 0.5   # simulasi area yang ditebang

selisih = sebelum - sesudah
alert = selisih > 0.3      # threshold penurunan NDVI
print("Piksel terdeteksi deforestasi:", alert.sum())
print("Persentase area:", alert.mean() * 100, "%")