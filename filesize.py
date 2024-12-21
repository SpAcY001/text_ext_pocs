
import os

#import fitz
from PyPDF2 import PdfReader

file = open("C:\\Users\\SESA737860\\Downloads\\input_text_files\\BG200800358 RIZZANI DE ECCHER .txt",'rb')
print(file.seek(0, os.SEEK_END))

print("Size of file is :", file.tell(), "bytes")
if(file.tell()>15000):
    reader = PdfReader("C:\\Users\\SESA737860\\Desktop\\bank_guarantee\\BG170700346.pdf")
    pdf_page_count = len(reader.pages)
    print(pdf_page_count)