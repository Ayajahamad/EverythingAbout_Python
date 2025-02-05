import qrcode

# Step 1: Define the URL you want to link to
url = "https://www.example.com"  # Replace with your desired URL

# Step 2: Create the QR code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # Size of each box in the QR code
    border=4,  # Width of the border
)

# Add the URL to the QR code instance
qr.add_data(url)
qr.make(fit=True)

# Step 3: Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Step 4: Save or display the QR code image
img.save("qr_code_url.png")  # Saves the QR code image with the URL embedded
print("QR Code for the URL generated and saved as 'qr_code_url.png'")

# Optionally: Show the QR code image
img.show()
