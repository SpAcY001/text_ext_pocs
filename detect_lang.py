import os
import shutil

from langdetect import detect

french_files=[]
lang_file={}

def detect_language(text_file):
  with open(text_file, "r",encoding="utf8") as f:
    text = f.read()

  lang = detect(text)
  if(lang=='pt'):
    #  french_files.append(text_file.split('\\')[-1].split('.')[0].split('_')[0])
     french_files.append(text_file.split('\\')[-1].split('.')[0])
  return lang

def lang_count_dictionary(language):
    if language in lang_file:
        lang_file[language] += 1
    else:
        lang_file[language] = 1

def iterate_folders(root_dir):
   for root, dirs, files in os.walk(root_dir):
      print("current directory ", root)

      for dir_name in dirs:
         print("sub_directory :", os.path.join(root,dir_name))

      for file_name in files:
         
        #  if file_name.split('.')[0].split('_')[0] in french_files:
         if file_name.split('.')[0] in french_files:
            source_path=os.path.join(root,file_name)
            # destination_path=os.path.join("C:\\Users\\SESA737860\\Downloads\\french_files",file_name)
            destination_path=os.path.join("C:\\Users\\SESA737860\\Downloads\\bla_pt_data",file_name)
            shutil.copyfile(source_path,destination_path)
            print("copied")

# path="C:\\Users\\SESA737860\\Downloads\\input_text_files"
path="C:\\Users\\SESA737860\\Downloads\\bonding_line_textfiles\\bonding_line_textfiles"
for text_file in os.listdir(path):
  f = os.path.join(path, text_file)
  dlang = detect_language(f)
  print(dlang)
  lang_count_dictionary(dlang)

print(lang_file)
print(french_files)
# root_directory="c:\\Users\\SESA737860\\Downloads\\excel_results"
# root_directory="C:\\Users\\SESA737860\\Downloads\\input_text_files"
root_directory=r"C:\Users\SESA737860\Desktop\BondingLine_data"
iterate_folders(root_directory)