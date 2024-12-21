import fitz

doc = fitz.open("C:\\Users\\SESA737860\\Desktop\\bank_guarantee\\BG1307018880.pdf")
for page_num in range(doc.page_count):
    page=doc[page_num]
    text = page.get_text("text")
    print(text)