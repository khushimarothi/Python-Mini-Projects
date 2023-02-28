'''
You need to install 2 modules for this code to work
1.qrcode - (pip install qrcode)
2.image - (pip install image)
in the terminal.
'''

import qrcode
import image
qr = qrcode.QRCode(
    version=15, #15 means the version of the QR code, the higher the version the more complex the QR code is
    box_size = 10, #size of the box which will be used to create the QR code
    border = 5, #it is the white part of the image

     
)
data = "https://github.com/khushimarothi"
#give the path that you want to convert into QR code
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", back_color="white")
img.save("test.png")