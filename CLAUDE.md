# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python QR code generator with two modes: simple QR codes (`main.py`) and QR codes with centered logo overlays (`generate_qr_with_logo.py`). Both scripts work as CLI tools (interactive prompt) or can be imported programmatically.

## Setup & Run

```bash
python3 -m venv venv
source venv/bin/activate
pip install qrcode[pil] pillow
```

Run either script interactively:
```bash
python main.py                    # simple QR code
python generate_qr_with_logo.py  # QR code with logo overlay
```

## Architecture

- **`main.py`** — Minimal QR generator using `qrcode` library. Low error correction (`ERROR_CORRECT_L`), version 1. Outputs `qrcode.png`.
- **`generate_qr_with_logo.py`** — Extended generator that overlays a logo (defaults to `logo.png` in cwd). Uses high error correction (`ERROR_CORRECT_H`) and version 2 to tolerate the logo covering ~30% of QR width. Creates a white rounded rectangle background behind the logo using Pillow's `ImageDraw.rounded_rectangle`.

Both expose a `generate_qr()` function. The logo variant adds an optional `logo_path` parameter.

## Dependencies

- `qrcode` (with `[pil]` extra) — QR code generation
- `Pillow` — Image manipulation for logo overlay
- Python 3.7+ / venv uses Python 3.13

## Key Design Notes

- Logo scaling is relative to QR dimensions (30% max width, see `generate_qr_with_logo.py:32`)
- Logo background padding (`30px`) and corner radius (`15px`) are hardcoded in `generate_qr_with_logo.py`
- `.gitignore` excludes `venv/` and all `*.png` files — generated QR images and logos are not tracked
