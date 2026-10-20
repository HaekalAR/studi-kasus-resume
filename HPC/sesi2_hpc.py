import time
from multiprocessing import Pool

def hitung(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    tugas = [5_000_000] * 8

    t = time.time()
    [hitung(n) for n in tugas]
    print("Serial  :", round(time.time() - t, 2), "detik")

    t = time.time()
    with Pool() as p:
        p.map(hitung, tugas)
    print("Paralel :", round(time.time() - t, 2), "detik")