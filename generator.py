from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas

ASSETS_DIR = "assets"
TEMPLATE_PATH = os.path.join(ASSETS_DIR, "template.png")
FONT_PATH = os.path.join(ASSETS_DIR, "GreatVibes-Regular.ttf")

def process_single_certificate(name, base_output="certificates"):
    safe_name = name.replace(" ", "_")
    person_folder = os.path.join(base_output, safe_name)
    os.makedirs(person_folder, exist_ok=True)
    
    # 1. Prepare the Template
    template = Image.open(TEMPLATE_PATH).convert("RGB")
    
    # 2. Define Real A4 Landscape Dimensions (300 DPI for high quality)
    # A4 landscape is 3508 x 2480 pixels at 300 DPI
    a4_width, a4_height = 3508, 2480
    img = template.resize((a4_width, a4_height), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(img)
    
    # 3. Dynamic Font Scaling for Long Names
    max_width = img.width * 0.75
    font_size = 250  # Increased base size for high-res image
    name_font = ImageFont.truetype(FONT_PATH, font_size)
    
    while draw.textlength(name, font=name_font) > max_width and font_size > 50:
        font_size -= 10
        name_font = ImageFont.truetype(FONT_PATH, font_size)
    
    # 4. Perfect Centering using Bounding Box
    bbox = draw.textbbox((0, 0), name, font=name_font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    name_x = (img.width - text_width) / 2
    # Vertically positioned at roughly 45% of the page height
    name_y = (img.height * 0.45) - (text_height / 2)
    
    draw.text((name_x, name_y), name, fill="#000000", font=name_font)
    
    # 5. Save Outputs
    png_path = os.path.join(person_folder, f"{safe_name}.png")
    pdf_path = os.path.join(person_folder, f"{safe_name}.pdf")
    img.save(png_path, quality=95)
    
    # 6. Generate PDF in Real Landscape A4 Size
    c = canvas.Canvas(pdf_path, pagesize=landscape(A4))
    width_pts, height_pts = landscape(A4)
    c.drawImage(png_path, 0, 0, width=width_pts, height=height_pts)
    c.showPage()
    c.save()
    
    return {"name": name, "folder": person_folder, "png": png_path, "pdf": pdf_path}

def generate_bulk(csv_path="data/names.csv", output_dir="certificates"):
    data = pd.read_csv(csv_path)
    results = []
    for name in data["name"]:
        results.append(process_single_certificate(name, output_dir))
    return results