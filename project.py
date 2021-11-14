# Importing library
import pyqrcode
"""First We make 'data' as a variable and then to get some user input to create a QR Code."""

data = input("Enter the text or link to generate QR code: ")

# Using pyqrcode.create() to create a qr code of the input data
qr = pyqrcode.create(data, error='H', version=30, mode='binary')

qr.png('qr_code.png', scale=10, module_color=(0, 0, 0, 255),
       background=(0xff, 0xff, 0xff, 0x88), quiet_zone=4)
