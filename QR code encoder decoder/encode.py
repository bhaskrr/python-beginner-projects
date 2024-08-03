import qrcode

data = 'https://youtu.be/dQw4w9WgXcQ?si=tSg3k8sdw4noxBpZ'

qr = qrcode.QRCode(
    version= 1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size= 10,
    border=4
)

# Add data to the QR Code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("qrcode.png")

print("QR code generated and saved as qrcode.png")