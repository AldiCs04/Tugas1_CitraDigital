import cv2

def tampilkan_dan_akses_piksel(path_gambar, skala=0.5):
    """
    Menampilkan gambar dan mengakses 10 nilai piksel pertama dalam bentuk RGB.
    Gambar diubah ukurannya sebelum ditampilkan.

    Args:
        path_gambar (str): Path ke file gambar.
        skala (float): Faktor skala untuk mengubah ukuran gambar.
                       Nilai antara 0 dan 1 untuk memperkecil, lebih besar dari 1 untuk memperbesar.
    """

    # Membaca gambar menggunakan OpenCV
    gambar = cv2.imread(path_gambar)

    # Periksa apakah gambar berhasil dibaca
    if gambar is None:
        print("Error: Gambar tidak dapat dibaca.")
        return

    # Mengubah ukuran gambar
    tinggi, lebar = gambar.shape[:2]
    ukuran_baru = (int(lebar * skala), int(tinggi * skala))
    gambar_resized = cv2.resize(gambar, ukuran_baru)

    # Menampilkan gambar yang diubah ukurannya
    cv2.imshow("Gambar", gambar_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Mengakses 10 nilai piksel pertama dari gambar asli (sebelum diubah ukurannya)
    jumlah_piksel = min(10, tinggi * lebar)

    print("10 Nilai Piksel Pertama (RGB) dari Gambar Asli:")
    for i in range(jumlah_piksel):
        # Menghitung koordinat piksel
        y = i // lebar
        x = i % lebar

        # Mendapatkan nilai RGB piksel
        b, g, r = gambar[y, x]  # OpenCV menggunakan urutan BGR

        # Menampilkan nilai RGB
        print(f"Piksel {i+1}: ({r}, {g}, {b})")  # Mengubah ke urutan RGB


# Contoh penggunaan
path_gambar = r"D:\KULIAH\SEMESTER VI\Coba_opencv\cs.jpg"  # Ganti dengan path gambar Anda
tampilkan_dan_akses_piksel(path_gambar, skala=0.5)  # Mengubah ukuran menjadi 30% dari ukuran asli