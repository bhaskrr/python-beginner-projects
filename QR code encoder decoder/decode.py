from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('./qrcode.png')

# Decode the QR code
img = Image.open('./qrcode.png')
decoded_objects = decode(img)

# Print the decoded data
for obj in decoded_objects:
    print("Type:", obj.type)
    print("Data:", obj.data.decode("utf-8"))

print("QR code decoded successfully")