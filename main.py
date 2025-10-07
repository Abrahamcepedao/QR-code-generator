import qrcode

def generate_qr(domain: str, filename: str = "qrcode.png"):
    """
    Generate a QR code for a given web domain or URL.
    Example:
        generate_qr("https://www.example.com")
    """
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # size of each box in pixels
        border=4,  # thickness of the border
    )
    qr.add_data(domain)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"✅ QR code saved as '{filename}' for: {domain}")

if __name__ == "__main__":
    url = input("Enter a web domain or URL: ")
    generate_qr(url)
