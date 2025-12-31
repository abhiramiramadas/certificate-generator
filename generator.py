from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

ASSETS_DIR = "assets"
TEMPLATE_PATH = os.path.join(ASSETS_DIR, "template.png")
FONT_PATH = os.path.join(ASSETS_DIR, "GreatVibes-Regular.ttf")

def process_single_certificate(name, base_output="certificates"):
    safe_name = name.replace(" ", "_")
    # Create person-specific subfolder: certificates/Abhirami_Ramadas/
    person_folder = os.path.join(base_output, safe_name)
    os.makedirs(person_folder, exist_ok=True)
    
    template = Image.open(TEMPLATE_PATH).convert("RGB")
    name_font = ImageFont.truetype(FONT_PATH, 120)
    img = template.copy()
    draw = ImageDraw.Draw(img)
    
    name_width = draw.textlength(name, font=name_font)
    name_x = (img.width - name_width) / 2
    name_y = 600
    
    draw.text((name_x, name_y), name, fill="#000000", font=name_font)
    
    png_path = os.path.join(person_folder, f"{safe_name}.png")
    pdf_path = os.path.join(person_folder, f"{safe_name}.pdf")
    
    img.save(png_path)
    
    c = canvas.Canvas(pdf_path, pagesize=A4)
    page_width, page_height = A4
    c.drawImage(png_path, 0, 0, width=page_width, height=page_height)
    c.save()
    
    return {"name": name, "folder": person_folder, "png": png_path, "pdf": pdf_path}

def generate_bulk(csv_path="data/names.csv", output_dir="certificates"):
    data = pd.read_csv(csv_path)
    results = []
    for name in data["name"]:
        results.append(process_single_certificate(name, output_dir))
    return results