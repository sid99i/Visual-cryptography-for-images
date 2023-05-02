import tkinter as tk
from tkinter import filedialog

def encrypt_image():
    # get the selected file path
    path = filedialog.askopenfilename()

    # get the encryption key from the entry widget
    key = int(key_entry.get())

    # print path of image file and encryption key that we are using
    print('The path of file : ', path)
    print('Key for encryption : ', key)

    try:
        # open file for reading purpose
        fin = open(path, 'rb')

        # storing image data in variable "image"
        image = fin.read()
        fin.close()

        # converting image into byte array to perform encryption easily on numeric data
        image = bytearray(image)

        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key

        # opening file for writing purpose
        fin = open(path, 'wb')

        # writing encrypted data in image
        fin.write(image)
        fin.close()

        # display success message in the label widget
        status_label.config(text="Encryption Done!")
    except Exception as e:
        # display error message in the label widget
        status_label.config(text="Error caught : " + str(e))


# create the main window
root = tk.Tk()

# create the label widgets
tk.Label(root, text="Enter Key for encryption of Image : ").grid(row=0, column=0, padx=5, pady=5)
key_entry = tk.Entry(root)
key_entry.grid(row=0, column=1, padx=5, pady=5)
status_label = tk.Label(root, text="")
status_label.grid(row=1, column=0, columnspan=2)

# create the button widget
tk.Button(root, text="Select Image", command=encrypt_image).grid(row=2, column=0, padx=5, pady=5)

# start the main event loop
root.mainloop()
