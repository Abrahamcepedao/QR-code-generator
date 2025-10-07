import qrcode
from PIL import Image, ImageDraw
import os

def generate_qr(domain: str, filename: str = "qrcode.png", logo_path: str = None):
    """
    Generate a QR code for a given web domain or URL, with optional logo overlay.
    The logo is centered and given a white rounded background for better contrast.
    """
    # --- Step 1: Create QR Code ---
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # high correction to tolerate logo overlay
        box_size=10,
        border=4,
    )
    qr.add_data(domain)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # --- Step 2: Locate and prepare logo ---
    if not logo_path:
        if os.path.exists("logo.png"):
            logo_path = "logo.png"

    if logo_path and os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")

        # Scale the logo relative to QR size (max width 30% of QR)
        qr_width, qr_height = qr_img.size
        max_logo_width = qr_width * 0.3
        logo_ratio = logo.width / logo.height
        logo_width = int(min(max_logo_width, qr_width))
        logo_height = int(logo_width / logo_ratio)
        logo = logo.resize((logo_width, logo_height), Image.LANCZOS)

        # --- Step 3: Create rounded white background ---
        padding = 30
        bg_width = logo_width + padding * 2
        bg_height = logo_height + padding * 2
        bg = Image.new("RGBA", (bg_width, bg_height), (255, 255, 255, 0))

        # Draw rounded white rectangle
        draw = ImageDraw.Draw(bg)
        corner_radius = 15
        draw.rounded_rectangle(
            [(0, 0), (bg_width, bg_height)],
            radius=corner_radius,
            fill=(255, 255, 255, 255),
        )

        # Paste logo on top of background
        bg.paste(logo, (padding, padding), mask=logo)

        # --- Step 4: Merge background+logo into QR ---
        combined_logo = bg
        pos = ((qr_width - bg_width) // 2, (qr_height - bg_height) // 2)
        qr_img.paste(combined_logo, pos, mask=combined_logo)

    # --- Step 5: Save result ---
    qr_img.save(filename)
    print(f"✅ QR code saved as '{filename}' for: {domain}")
    if logo_path:
        print(f"🖼️ Logo added with white rounded background from: {logo_path}")

if __name__ == "__main__":
    url = input("Enter a web domain or URL: ")
    generate_qr(url)
