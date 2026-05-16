from PIL import Image
import os

# Single image to PDF
def image_to_pdf(image_path, output_pdf="output.pdf"):
    image = Image.open(image_path)
    
    # Convert to RGB (important for PDF)
    if image.mode in ('RGBA', 'LA', 'P'):
        image = image.convert('RGB')
    
    image.save(output_pdf, "PDF", resolution=100.0)
    print(f"PDF saved as: {output_pdf}")

# Usage
image_to_pdf("resume.jpeg")   # Change filename