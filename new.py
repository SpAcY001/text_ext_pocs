import os

from langchain.document_loaders import PyPDFLoader

count=0
failed_count=0
filetexts=dict()
# text = parser.from_file('BG220200379.pdf')
# print(text['content'])
file_path="C:\\Users\\SESA737860\\Desktop\\bank_guarantee\\pdffiles"
for filename in os.listdir(file_path):
    f = os.path.join(file_path, filename)
    file=f.split('\\')[-1]
    loader = PyPDFLoader(f"C:\\Users\\SESA737860\\Desktop\\bank_guarantee\\pdffiles\\{file}", extract_images=True)
    try:
        pages=loader.load()
        text=""
        for i in range(len(pages)):
            page_content = pages[i].page_content
            text+=page_content
            # print(f"{i}"*20)
        filetexts[file]=text
        # print(text['content'])
        count=count+1
        print(count)
    except (ValueError, NotImplementedError):
        failed_count=failed_count+1
        pass
print(f"total extracted : {count}")
print(f"total failed : {failed_count}")
for file, text in filetexts.items():
    file2 = file.split('.')[0]
    file2 = file.replace('.pdf','').replace('.','')
    with open(f'{file2}.txt', 'w', encoding = "utf-8") as outfile:
        # for line in text:
        outfile.write(text)
        outfile.close()





# loader = PyPDFLoader("C:\\Users\\SESA737860\\Desktop\\bank_guarantee\\pdffiles\\BG220200379.pdf", extract_images=True)
# pages=loader.load()
# text=""
# for i in range(len(pages)):
#     page_content = pages[i].page_content
#     text+=page_content
#     print(f"{i}"*20)
# print(text)