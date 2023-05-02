import tkinter as tk
from tkinter import filedialog
import os

def decrypt_image():
    # get the selected file path
    path = filedialog.askopenfilename()

    # get the decryption key from the entry widget
    key = int(key_entry.get())

    # print path of image file and decryption key that we are using
    print('The path of file : ', path)
    print('Key for decryption : ', key)

    try:
        # open the encrypted image file for reading purpose
        fin = open(path, 'rb')

        # create a new file name for the decrypted image
        file_name, file_ext = os.path.splitext(path)
        output_file = file_name + '_decrypted' + file_ext

        # create a copy of the encrypted image file
        with open(output_file, 'wb') as fout:
            fout.write(fin.read())

        # close the input file
        fin.close()

        # open the output file for writing purpose
        fout = open(output_file, 'rb+')

        # read the encrypted data from the output file
        image = bytearray(fout.read())

        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key

        # write the decrypted data back to the output file
        fout.seek(0)
        fout.write(image)

        # close the output file
        fout.close()

        # display success message in the label widget
        status_label.config(text="Decryption Done!")
    except Exception as e:
        # display error message in the label widget
        status_label.config(text="Error caught : " + str(e))


# create the main window
root = tk.Tk()

# create the label widgets
tk.Label(root, text="Enter Key for decryption of Image : ").grid(row=0, column=0, padx=5, pady=5)
key_entry = tk.Entry(root)
key_entry.grid(row=0, column=1, padx=5, pady=5)
status_label = tk.Label(root, text="")
status_label.grid(row=1, column=0, columnspan=2)

# create the button widget
tk.Button(root, text="Select Encrypted Image", command=decrypt_image).grid(row=2, column=0, padx=5, pady=5)

# start the main event loop
root.mainloop()
