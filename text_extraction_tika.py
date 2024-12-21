import os

from tika import parser

count=0
filetexts=dict()
# text = parser.from_file('BG220200379.pdf')
# print(text['content'])
file_path="C:\\Users\\SESA737860\\Desktop\\bank_guarantee\\pdffiles"
for filename in os.listdir(file_path):
    f = os.path.join(file_path, filename)
    file=f.split('\\')[-1]
    text = parser.from_file(f"C:\\Users\\SESA737860\\Desktop\\bank_guarantee\\pdffiles\\{file}")
    filetexts[file]=text['content']
    # print(text['content'])
    count=count+1
    print(f"{count}"*30)
print(f"total extracted : {count}")

for file, text in filetexts.items():
    file2 = file.split('.')[0]
    file2 = file.replace('.pdf','').replace('.','')
    with open(f'{file2}.txt', 'w', encoding = "utf-8") as outfile:
        # for line in text:
        outfile.write(text)
        outfile.close()