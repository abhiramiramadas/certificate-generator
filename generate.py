from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Load names
data = pd.read_csv("names.csv")
os.makedirs("certificates", exist_ok=True)

# Load template
template = Image.open("template.png").convert("RGB")

# Font
name_font = ImageFont.truetype("./GreatVibes-Regular.ttf", 120)

for name in data["name"]:
    img = template.copy()
    draw = ImageDraw.Draw(img)

    # ---- NAME POSITION ----
    name_width = draw.textlength(name, font=name_font)
    name_x = (img.width - name_width) / 2
    name_y = 600

    draw.text(
        (name_x, name_y),
        name,
        fill="#000000",
        font=name_font
    )

    # ---- SAFE FILE NAME ----
    safe_name = name.replace(" ", "_")

    # ---- SAVE PNG ----
    png_path = f"certificates/{safe_name}.png"
    img.save(png_path)

    # ---- SAVE PDF ----
    pdf_path = f"certificates/{safe_name}.pdf"
    c = canvas.Canvas(pdf_path, pagesize=A4)

    # A4 size in points (ReportLab)
    page_width, page_height = A4

    c.drawImage(
        png_path,
        0,
        0,
        width=page_width,
        height=page_height
    )
    c.save()

print("✅ All certificates generated as PNG and PDF!")
