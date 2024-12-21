import os
import shutil

from langdetect import detect

english_files=[]
lang_file={}

def detect_language(text_file):
  with open(text_file, "r",encoding="utf8") as f:
    text = f.read()

  lang = detect(text)
  if(lang=='en'):
     english_files.append(text_file.split('\\')[-1].split('.')[0])
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
         if file_name.split('.')[0] in english_files:
            source_path=os.path.join(root,file_name)
            destination_path=os.path.join("C:\\Users\\SESA737860\\Downloads\\english_text_files",file_name)
            shutil.copyfile(source_path,destination_path)
            print("copied")

path="C:\\Users\\SESA737860\\Downloads\\input_text_files"
for text_file in os.listdir(path):
  f = os.path.join(path, text_file)
  dlang = detect_language(f)
  print(dlang)
  lang_count_dictionary(dlang)

print(lang_file)
print(english_files)
print(len(english_files))
root_directory="C:\\Users\\SESA737860\\Downloads\\input_text_files"
iterate_folders(root_directory)