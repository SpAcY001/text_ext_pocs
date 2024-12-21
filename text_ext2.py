import os

import pytesseract
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

image_dir = 'C:\\Users\\SESA737860\\Desktop\\bank_guarantee'
# images = convert_from_path("BG1307018880.pdf",output_folder=image_dir,  fmt='png')
images = convert_from_path("BG1307018880.pdf", fmt='png')
for i, image in enumerate(images):
    # image_path = os.path.join(image_dir, f'image_{i}.png')
    extracted_text = pytesseract.image_to_string(image, lang='eng')
    print(f"Page {i+1} text:")
    print(extracted_text)
    print('---')

# for image_path in os.listdir(image_dir):
#     os.remove(os.path.join(image_dir, image_path))