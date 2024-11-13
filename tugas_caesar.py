import tkinter as tk
from tkinter import messagebox

def enkripsi(plain_text, shift):
    chipher_text = ""
    for char in plain_text:
        # Huruf Besar
        if char.isupper():
            chipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        
        # Huruf Kecil
        elif char.islower():
            chipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        
        # Karakter Selain Huruf Tetap
        else:
            chipher_text += char
    return chipher_text

def deskripsi(chipher_text, shift):
    plain_text = ""
    for char in chipher_text:
        # Huruf Besar
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        
        # Huruf Kecil
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        
        # Karakter Selain Huruf Tetap
        else:
            plain_text += char
    return plain_text

def perform_encryption():
    plain_text = entry_plain_text.get()
    shift = int(entry_shift.get())
    chipher_text = enkripsi(plain_text, shift)
    entry_chipher_text.delete(0, tk.END)
    entry_chipher_text.insert(tk.END, chipher_text)

def perform_decryption():
    chipher_text = entry_chipher_text.get()
    shift = int(entry_shift.get())
    plain_text = deskripsi(chipher_text, shift)
    entry_plain_text.delete(0, tk.END)
    entry_plain_text.insert(tk.END, plain_text)

# Setup GUI Window
window = tk.Tk()
window.title("Caesar Cipher")
window.configure(bg="#f8e8f2")  # Background color in a pastel pink shade

# Custom styling options
label_font = ("Helvetica", 12, "italic")
entry_bg = "#fde8f0"  # Light pink background for entry fields
button_bg = "#f5c7d0"  # Soft pink for buttons
button_fg = "white"
button_font = ("Helvetica", 10, "bold")

# Plain Text Label and Entry
label_plain_text = tk.Label(window, text="Plain Text:", bg="#f8e8f2", font=label_font, fg="#b5485c")
label_plain_text.grid(row=0, column=0, padx=10, pady=10)
entry_plain_text = tk.Entry(window, width=40, bg=entry_bg, font=label_font)
entry_plain_text.grid(row=0, column=1, padx=10, pady=10)

# Shift Label and Entry
label_shift = tk.Label(window, text="Shift (1-25):", bg="#f8e8f2", font=label_font, fg="#b5485c")
label_shift.grid(row=1, column=0, padx=10, pady=10)
entry_shift = tk.Entry(window, width=5, bg=entry_bg, font=label_font)
entry_shift.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Cipher Text Label and Entry
label_chipher_text = tk.Label(window, text="Cipher Text:", bg="#f8e8f2", font=label_font, fg="#b5485c")
label_chipher_text.grid(row=2, column=0, padx=10, pady=10)
entry_chipher_text = tk.Entry(window, width=40, bg=entry_bg, font=label_font)
entry_chipher_text.grid(row=2, column=1, padx=10, pady=10)

# Encrypt Button
button_encrypt = tk.Button(window, text="Encrypt", command=perform_encryption, bg=button_bg, fg=button_fg, font=button_font)
button_encrypt.grid(row=3, column=0, padx=10, pady=10)

# Decrypt Button
button_decrypt = tk.Button(window, text="Decrypt", command=perform_decryption, bg=button_bg, fg=button_fg, font=button_font)
button_decrypt.grid(row=3, column=1, padx=10, pady=10)

# Run the main loop
window.mainloop()