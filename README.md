# KeamananData

# CHIPERGUI
File Python ini adalah sebuah program berbasis GUI (Graphical User Interface) yang menggunakan pustaka Tkinter untuk mengimplementasikan cipher Caesar, yaitu metode sederhana untuk enkripsi dan dekripsi teks dengan menggunakan pergeseran huruf. Program ini menyediakan antarmuka untuk mengenkripsi dan mendekripsi teks berdasarkan nilai pergeseran yang dimasukkan pengguna.

Cara Kerja Program

Fungsi Enkripsi

Fungsi enkripsi(plain_text, shift) menerima teks asli (plain text) dan nilai pergeseran (shift).
Karakter dalam teks yang berupa huruf akan digeser sesuai nilai pergeseran, dengan mempertahankan kapitalisasi (huruf besar/kecil).
Karakter non-huruf tidak mengalami perubahan.

Fungsi Dekripsi
Fungsi deskripsi(chipher_text, shift) melakukan proses kebalikan dari enkripsi, yaitu mengembalikan teks yang telah dienkripsi (cipher text) menjadi teks asli menggunakan nilai pergeseran yang sama.

Fitur GUI
Input Teks: Pengguna dapat memasukkan teks asli atau teks cipher melalui kolom input.
Input Pergeseran: Nilai pergeseran (1-25) dimasukkan oleh pengguna.
Tombol Enkripsi: Jika tombol "Enkripsi" ditekan, teks asli akan diubah menjadi teks cipher menggunakan fungsi enkripsi.
Tombol Dekripsi: Jika tombol "Dekripsi" ditekan, teks cipher akan dikembalikan ke teks asli menggunakan fungsi deskripsi.
Hasil: Teks hasil enkripsi atau dekripsi ditampilkan pada kolom hasil.

Proses GUI
GUI dibuat menggunakan Tkinter dengan elemen-elemen seperti Label, Entry, dan Button.
Fungsi perform_encryption dan perform_decryption terhubung dengan tombol untuk menjalankan proses sesuai input pengguna.

Contoh Penggunaan
Input teks: HELLO
Nilai pergeseran: 3
Hasil enkripsi: KHOOR
Hasil dekripsi (dengan nilai pergeseran yang sama): HELLO.

# DESGUI
File Python ini adalah sebuah program berbasis GUI (Graphical User Interface) yang menggunakan pustaka Tkinter untuk mengimplementasikan enkripsi dan dekripsi data dengan algoritma DES (Data Encryption Standard). Program ini memungkinkan pengguna untuk memasukkan pesan dan kunci 8 karakter, lalu mengenkripsi atau mendekripsi pesan tersebut.

Cara Kerja Program

Algoritma DES

Program menggunakan pustaka PyCryptodome untuk menerapkan algoritma DES dalam mode ECB (Electronic Codebook).
Kunci (key) harus berukuran 8 karakter, sesuai dengan persyaratan DES.
Pesan dienkripsi atau didekripsi setelah diproses untuk memastikan ukuran sesuai dengan blok DES (8 byte).

Fungsi Enkripsi
Fungsi encrypt_message membaca pesan dan kunci dari input pengguna.
Pesan diproses menggunakan padding untuk memenuhi ukuran blok DES.
Pesan dienkripsi menggunakan objek cipher DES dan hasilnya dikodekan dengan Base64 untuk mempermudah representasi.

Fungsi Dekripsi
Fungsi decrypt_message membaca pesan terenkripsi dan kunci dari input pengguna.
Pesan terenkripsi didekodekan dari format Base64 dan diproses menggunakan cipher DES untuk dekripsi.
Padding yang ditambahkan saat enkripsi dihapus untuk mendapatkan pesan asli.

Validasi Input
Program memverifikasi bahwa kunci yang dimasukkan berukuran tepat 8 karakter.
Pesan atau teks yang kosong akan menghasilkan pesan kesalahan.

Fitur GUI
Input Key: Kolom untuk memasukkan kunci 8 karakter.
Input Message: Kolom untuk memasukkan pesan yang akan dienkripsi atau dekripsi.
Output Result: Kolom hanya baca untuk menampilkan hasil enkripsi atau dekripsi.
Tombol Encrypt/Decrypt: Tombol untuk menjalankan proses enkripsi atau dekripsi.

Proses GUI
Antarmuka dibuat menggunakan elemen-elemen Tkinter seperti Label, Entry, dan Button.
Hasil proses enkripsi atau dekripsi ditampilkan di kolom hasil.

Contoh Penggunaan
Kunci: abcdefgh
Pesan asli: HelloWorld
Hasil enkripsi: VGLOR8SbE/k=
Hasil dekripsi (menggunakan kunci yang sama): HelloWorld.


# ENIGMAGUI
File Python ini adalah program berbasis GUI menggunakan pustaka Tkinter yang mensimulasikan metode enkripsi dan dekripsi mirip mesin Enigma sederhana. Program ini mengenkripsi dan mendekripsi pesan menggunakan rotasi huruf berdasarkan nilai rotor yang ditentukan.

Cara Kerja Program

Enigma Cipher Sederhana

Kelas EnigmaCipher:
Menggunakan rotasi huruf berbasis modul 26 untuk alfabet.
Setiap huruf teks digeser sesuai dengan nilai rotor, dengan memperhatikan kapitalisasi huruf.
Jika teks tidak berupa huruf (contoh: spasi atau simbol), teks dibiarkan tidak berubah.

Fungsi:
encrypt: Mengenkripsi teks berdasarkan nilai rotor.
decrypt: Membalik proses enkripsi untuk mendapatkan teks asli.

Fitur GUI
Input Pesan: Kolom untuk memasukkan teks yang akan dienkripsi atau didekripsi.
Hasil: Kolom hanya baca yang menampilkan hasil enkripsi atau dekripsi.
Tombol Enkripsi/Dekripsi: Tombol untuk menjalankan proses sesuai kebutuhan pengguna.

Pengaturan Default Rotor
Rotor default adalah [3, 1, 4], yang digunakan untuk menentukan pola pergeseran huruf. Pola ini diterapkan berulang jika panjang teks melebihi jumlah rotor.

Fungsi Enkripsi
Teks dari kolom input diproses menggunakan EnigmaCipher.encrypt.
Hasil enkripsi ditampilkan di kolom hasil.

Fungsi Dekripsi
Teks terenkripsi diproses menggunakan EnigmaCipher.decrypt.
Hasil dekripsi dikembalikan ke teks asli dan ditampilkan di kolom hasil.

Contoh Penggunaan
Rotor default: [3, 1, 4]
Pesan asli: HELLO
Hasil enkripsi: KFNOR
Hasil dekripsi (menggunakan rotor yang sama): HELLO.

# STEGANOGUI
File ini adalah sebuah aplikasi GUI sederhana berbasis Python untuk melakukan steganografi. Aplikasi ini memungkinkan pengguna untuk menyembunyikan pesan teks di dalam sebuah gambar (format PNG atau BMP) dan mengekstrak pesan tersembunyi dari gambar tersebut. Aplikasi menggunakan pustaka Tkinter untuk antarmuka pengguna dan stegano.lsb untuk operasi steganografi.

Cara Kerja:

Fungsi hide_message:

Mengambil gambar dari file yang dipilih pengguna.
Mengambil pesan teks dari input GUI.
Menyembunyikan pesan dalam gambar menggunakan metode Least Significant Bit (LSB) dari pustaka stegano.
Menyimpan gambar hasil dengan pesan tersembunyi di lokasi yang dipilih pengguna.

Fungsi show_message:
Mengambil gambar dari file yang dipilih pengguna.
Mengungkap pesan tersembunyi di dalam gambar menggunakan metode LSB.
Menampilkan pesan tersembunyi melalui kotak dialog jika ditemukan.

Antarmuka Pengguna (GUI):
Menampilkan teks input untuk memasukkan pesan yang akan disembunyikan.
Tombol untuk:
Menyembunyikan pesan ke dalam gambar.
Mengungkap pesan dari gambar.
Keluar dari aplikasi.

Teknologi yang Digunakan:
Tkinter untuk membangun antarmuka pengguna.
stegano.lsb untuk menyisipkan dan mengungkap pesan pada gambar.
filedialog dari Tkinter untuk memilih file gambar atau lokasi penyimpanan.

Contoh Penggunaan
Menyembunyikan Pesan:
Pesan: "HELLO WORLD"
Gambar asli: image.png
Gambar hasil: image_secret.png

Mengungkap Pesan:
Gambar: image_secret.png
Pesan tersembunyi: "HELLO WORLD"
