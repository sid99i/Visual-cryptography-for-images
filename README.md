# Image Encryption and Decryption using GUI

Welcome to the repository containing Python code for image encryption and decryption with a graphical user interface (GUI). This project demonstrates the process of encrypting and decrypting images using a user-provided key.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Example](#example)
- [Contributing](#contributing)

## Introduction
This repository provides two separate scripts, each responsible for either encrypting or decrypting an image file. The user interacts with a graphical user interface created using the Tkinter library to input the encryption/decryption key and select the image file. The image is then processed, and the encrypted/decrypted result is displayed.

## Features
- **Image Encryption:** The `encrypt_image` script takes an image file and encrypts its content using bitwise XOR operations with a provided key.
- **Image Decryption:** The `decrypt_image` script decrypts an encrypted image file by performing bitwise XOR operations with the key.
- **Graphical User Interface:** Both scripts use a Tkinter-based GUI to prompt the user for the key and image file path, making the process user-friendly.


## Example
1. Run the `encrypt_image.py` script and provide the encryption key and image file.
2. View the status message to see if the encryption was successful.
3. To decrypt the encrypted image, run the `decrypt_image.py` script and provide the decryption key and encrypted image file.

## Contributing
Contributions are welcome! Feel free to enhance the features or fix any issues by creating a pull request.

*Note: This README provides an overview of the code's functionality and usage. For detailed implementation, please refer to the source code in `encrypt_image.py` and `decrypt_image.py`.*
