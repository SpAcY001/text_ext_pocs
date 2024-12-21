from PyPDF2 import PdfReader

reader = PdfReader("C:\\Users\\SESA737860\\Desktop\\bank_guarantee\\BG1307018880.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

print(text)