import tkinter as tk
from tkinter import filedialog
import os

def decrypt_image():

    path = filedialog.askopenfilename()
    key = int(key_entry.get())
    print('The path of file : ', path)
    print('Key for decryption : ', key)

    try:
        fin = open(path, 'rb')
        file_name, file_ext = os.path.splitext(path)
        output_file = file_name + '_decrypted' + file_ext

        with open(output_file, 'wb') as fout:
            fout.write(fin.read())
        fin.close()
        fout = open(output_file, 'rb+')
        image = bytearray(fout.read())
        for index, values in enumerate(image):
            image[index] = values ^ key


        fout.seek(0)
        fout.write(image)
        fout.close()
        status_label.config(text="Decryption Done!")
        
    except Exception as e:
        status_label.config(text="Error caught : " + str(e))

root = tk.Tk()
tk.Label(root, text="Enter Key for decryption of Image : ").grid(row=0, column=0, padx=5, pady=5)
key_entry = tk.Entry(root)
key_entry.grid(row=0, column=1, padx=5, pady=5)
status_label = tk.Label(root, text="")
status_label.grid(row=1, column=0, columnspan=2)
tk.Button(root, text="Select Encrypted Image", command=decrypt_image).grid(row=2, column=0, padx=5, pady=5)

root.mainloop()
