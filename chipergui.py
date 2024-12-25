import tkinter as tk
from tkinter import messagebox

def enkripsi(plain_text, shift):
    chipher_text = ""
    for char in plain_text:
        if char.isupper():
            chipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        
        elif char.islower():
            chipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        
        else:
            chipher_text += char
    return chipher_text

def deskripsi(chipher_text, shift):
    plain_text = ""
    for char in chipher_text:
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        
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

label_plain_text = tk.Label(window, text="Text:")
label_plain_text.grid(row=0, column=0, padx=10, pady=10)
entry_plain_text = tk.Entry(window, width=40)
entry_plain_text.grid(row=0, column=1, padx=10, pady=10)

label_shift = tk.Label(window, text="Pergeseran (1-25):")
label_shift.grid(row=1, column=0, padx=10, pady=10)
entry_shift = tk.Entry(window, width=5)
entry_shift.grid(row=1, column=1, padx=10, pady=10, sticky="w")

label_chipher_text = tk.Label(window, text="Cipher Text:")
label_chipher_text.grid(row=2, column=0, padx=10, pady=10)
entry_chipher_text = tk.Entry(window, width=40)
entry_chipher_text.grid(row=2, column=1, padx=10, pady=10)

button_encrypt = tk.Button(window, text="Enkripsi", command=perform_encryption)
button_encrypt.grid(row=3, column=0, padx=10, pady=10)

button_decrypt = tk.Button(window, text="Dekripsi", command=perform_decryption)
button_decrypt.grid(row=3, column=1, padx=10, pady=10)

window.mainloop()
