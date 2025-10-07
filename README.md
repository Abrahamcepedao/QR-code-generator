# QR Code Generator

A Python-based QR code generator with support for both simple QR codes and QR codes with custom logo overlays.

## Features

- **Simple QR Code Generation**: Create basic QR codes for any URL or text
- **Logo Overlay**: Add your custom logo to the center of the QR code
- **Rounded Background**: Logos are displayed with a white rounded background for better contrast
- **High Error Correction**: Uses high error correction level to ensure QR codes remain scannable even with logo overlays
- **Customizable**: Easy to modify colors, sizes, and styling

## Project Structure

```
qr-code/
├── main.py                      # Simple QR code generator
├── generate_qr_with_logo.py    # Advanced QR code generator with logo support
├── logo.png                     # Sample logo file
├── .gitignore                   # Git ignore configuration
└── README.md                    # This file
```

## Installation

1. **Clone or download this repository**

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required dependencies**:
   ```bash
   pip install qrcode[pil] pillow
   ```

## Usage

### Simple QR Code Generator

Use `main.py` for basic QR code generation:

```bash
python main.py
```

When prompted, enter the URL or text you want to encode:
```
Enter a web domain or URL: https://www.example.com
```

The QR code will be saved as `qrcode.png` in the current directory.

**Programmatic Usage:**
```python
from main import generate_qr

generate_qr("https://www.example.com", "output.png")
```

### QR Code with Logo

Use `generate_qr_with_logo.py` for QR codes with custom logo overlays:

```bash
python generate_qr_with_logo.py
```

**Features:**
- Automatically looks for `logo.png` in the current directory
- Scales the logo to 30% of the QR code width
- Adds a white rounded background behind the logo for better visibility
- Uses high error correction to maintain scannability

**Programmatic Usage:**
```python
from generate_qr_with_logo import generate_qr

# With default logo.png
generate_qr("https://www.example.com", "output.png")

# With custom logo path
generate_qr("https://www.example.com", "output.png", logo_path="path/to/logo.png")
```

## Configuration

### QR Code Parameters

Both scripts use the `qrcode.QRCode` class with customizable parameters:

**main.py:**
- `version=1`: Controls QR code size (1 is smallest)
- `error_correction=ERROR_CORRECT_L`: Low error correction (~7% recovery)
- `box_size=10`: Size of each box in pixels
- `border=4`: Thickness of the border (minimum is 4)

**generate_qr_with_logo.py:**
- `version=2`: Slightly larger to accommodate logo
- `error_correction=ERROR_CORRECT_H`: High error correction (~30% recovery) - essential for logo overlays
- `box_size=10`: Size of each box in pixels
- `border=4`: Thickness of the border

### Logo Customization

In `generate_qr_with_logo.py`, you can adjust:

- **Logo size**: Modify `max_logo_width = qr_width * 0.3` (line 32)
- **Background padding**: Change `padding = 30` (line 39)
- **Corner radius**: Adjust `corner_radius = 15` (line 46)
- **Background color**: Modify `fill=(255, 255, 255, 255)` (line 50)

## Requirements

- Python 3.7+
- qrcode[pil]
- Pillow (PIL)

## Examples

### Example 1: Simple QR Code
```python
python main.py
# Enter: https://www.example.com
# Output: qrcode.png
```

### Example 2: QR Code with Logo
```python
python generate_qr_with_logo.py
# Enter: https://www.example.com
# Output: qrcode.png (with logo overlay)
```

### Example 3: Custom Output
```python
from generate_qr_with_logo import generate_qr

generate_qr(
    domain="https://www.mycompany.com",
    filename="company_qr.png",
    logo_path="company_logo.png"
)
```

## Tips

1. **Logo Format**: Use PNG files with transparency for best results
2. **Logo Size**: Keep logos relatively simple for better QR code readability
3. **Testing**: Always test your QR codes with multiple scanners before deploying
4. **Error Correction**: Higher error correction levels allow for larger logos but create denser QR codes
5. **Contrast**: Ensure good contrast between QR code and background for reliable scanning

## Troubleshooting

**QR Code won't scan:**
- Try reducing logo size (decrease the 0.3 multiplier in line 32)
- Ensure logo doesn't cover too much of the QR code
- Test with different QR code scanning apps

**Logo looks distorted:**
- Use high-resolution logo images
- Ensure logo aspect ratio is maintained
- Try adjusting the `Image.LANCZOS` resampling filter

**Import errors:**
- Make sure you've activated your virtual environment
- Reinstall dependencies: `pip install --upgrade qrcode[pil] pillow`

## License

This project is available for personal and commercial use.

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## Author

Created as part of the dfuture project collection.
