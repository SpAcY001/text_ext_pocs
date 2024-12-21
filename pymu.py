import fitz

with fitz.open("BG1307018880.pdf") as doc:
    text = ""
    for page in doc:
        text += page.get_text()

print(text)