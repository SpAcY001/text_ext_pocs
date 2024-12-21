# import os

import pytesseract

# from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

extracted_text = pytesseract.image_to_string("C:\\Users\\SESA737860\\Desktop\\bank_guarantee\\table_extraction\\WhatsApp Image 2024-02-05 at 12.42.17 (1).jpeg", lang='eng')
    
# Printing the extracted text
# print(f"Page {i+1} text:")
print(extracted_text)
print('---')
# image_dir = 'C:\\Users\\SESA737860\\Desktop\\bank_guarantee\\images'
# images = convert_from_path("Doc1.pdf", output_folder=image_dir, fmt='png')
# for i, image in enumerate(images):
#     image_path = os.path.join(image_dir, f'image_{i}.png')
    
#     # Performing OCR using Tesseract
#     extracted_text = pytesseract.image_to_string(image, lang='eng')
    
#     # Printing the extracted text
#     print(f"Page {i+1} text:")
#     print(extracted_text)
#     print('---')

# for image_path in os.listdir(image_dir):
#     os.remove(os.path.join(image_dir, image_path))