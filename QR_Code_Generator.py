import qrcode
from PIL import Image

def generate_qr(data, filename="custom_qr.png", fill_color="black", back_color="white", logo_path=None):
    # Create QR code object with high error correction
    qr = qrcode.QRCode(
        version=5,  # Higher version means larger size
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for better logo visibility
        box_size=10,
        border=4
    )
    
    qr.add_data(data)
    qr.make(fit=True)

    # Create the QR code image with custom colors
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")

    # If a logo is provided, add it to the center
    if logo_path:
        try:
            logo = Image.open(logo_path)
            
            # Resize logo (20% of QR code size)
            qr_width, qr_height = img.size
            logo_size = qr_width // 5
            logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
            
            # Paste logo at the center
            pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
            img.paste(logo, pos, mask=logo if logo.mode == "RGBA" else None)
        except Exception as e:
            print(f"Error loading logo: {e}")

    # Save the QR code image
    img.save(filename)
    print(f"QR Code saved as {filename}")

# User input for QR code
text_or_url = input("Enter text or URL for the QR code: ")
logo_path = input("Enter path to logo image (or press Enter to skip): ")

# Generate the QR code with customization
generate_qr(text_or_url, filename="my_qrcode.png", fill_color="blue", back_color="white", logo_path=logo_path if logo_path else None)
