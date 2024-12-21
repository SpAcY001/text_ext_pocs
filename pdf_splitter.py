from PyPDF2 import PdfReader, PdfWriter

inputpdf = PdfReader(open("C:\\Users\\SESA737860\\Desktop\\BondingLine_data\\Identification 2\\Indonesia\\SE Indonesia_JP Morgan Chase_2015.pdf", "rb"))
print(f"no of pages :{len(inputpdf.pages)}")
n=len(inputpdf.pages)

for i in range(0,n+1,2):
    output = PdfWriter()
    for j in range(i,i+3):
        if j<n:
            output.add_page(inputpdf.pages[j])
    if i<n:
        with open("document-page%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)
