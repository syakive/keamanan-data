import tkinter as tk
from tkinter import filedialog, messagebox
from stegano import lsb
import os


def get_image_path():
    """Menampilkan dialog file untuk memilih gambar."""
    img_path = filedialog.askopenfilename(title="Pilih Gambar", filetypes=(("Image files", "*.png;*.bmp"), ("All files", "*.*")))
    return img_path


def hide_message():
    """Menyembunyikan pesan dalam gambar."""
    img_path = get_image_path()
    if not img_path:
        return

    message = message_entry.get("1.0", tk.END).strip()

    if not message:
        messagebox.showerror("Error", "Pesan tidak boleh kosong.")
        return

    try:
        # Proses menyembunyikan pesan
        secret = lsb.hide(img_path, message)
        
        # Pilih lokasi penyimpanan gambar hasil
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=(("PNG files", "*.png"), ("BMP files", "*.bmp")))
        
        if not save_path:
            return

        # Simpan gambar hasil
        secret.save(save_path)
        messagebox.showinfo("Sukses", f"Pesan berhasil disembunyikan. Gambar disimpan di: {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menyembunyikan pesan: {e}")


def show_message():
    """Menampilkan pesan tersembunyi dari gambar."""
    img_path = get_image_path()
    if not img_path:
        return

    try:
        # Ambil pesan dari gambar
        clear_message = lsb.reveal(img_path)
        if clear_message:
            messagebox.showinfo("Pesan Tersembunyi", f"Pesan tersembunyi: {clear_message}")
        else:
            messagebox.showinfo("Tidak ada Pesan", "Tidak ada pesan tersembunyi dalam gambar.")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menampilkan pesan dari gambar: {e}")


# Membuat window utama
root = tk.Tk()
root.title("Steganography Tool")
root.geometry("400x300")

# Label dan text entry untuk memasukkan pesan
message_label = tk.Label(root, text="Masukkan pesan yang akan disembunyikan:")
message_label.pack(pady=10)

message_entry = tk.Text(root, height=5, width=40)
message_entry.pack(pady=5)

# Tombol untuk sembunyikan pesan
hide_button = tk.Button(root, text="Sembunyikan Pesan", width=20, command=hide_message)
hide_button.pack(pady=10)

# Tombol untuk tampilkan pesan
show_button = tk.Button(root, text="Tampilkan Pesan", width=20, command=show_message)
show_button.pack(pady=10)

# Tombol untuk keluar dari aplikasi
exit_button = tk.Button(root, text="Keluar", width=20, command=root.quit)
exit_button.pack(pady=10)

# Menjalankan aplikasi GUI
root.mainloop()
