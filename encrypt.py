import tkinter as tk
from tkinter import filedialog

def encrypt_image():

    path = filedialog.askopenfilename()
    key = int(key_entry.get())
    print('The path of file : ', path)
    print('Key for encryption : ', key)

    try:

        fin = open(path, 'rb')


        image = fin.read()
        fin.close()

        image = bytearray(image)


        for index, values in enumerate(image):
            image[index] = values ^ key


        fin = open(path, 'wb')


        fin.write(image)
        fin.close()


        status_label.config(text="Encryption Done!")
    except Exception as e:

        status_label.config(text="Error caught : " + str(e))


root = tk.Tk()


tk.Label(root, text="Enter Key for encryption of Image : ").grid(row=0, column=0, padx=5, pady=5)
key_entry = tk.Entry(root)
key_entry.grid(row=0, column=1, padx=5, pady=5)
status_label = tk.Label(root, text="")
status_label.grid(row=1, column=0, columnspan=2)


tk.Button(root, text="Select Image", command=encrypt_image).grid(row=2, column=0, padx=5, pady=5)


root.mainloop()
