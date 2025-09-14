import re
import os

phone_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
folder = os.getcwd()
for cur_folder, sub_folders, files in os.walk(folder):
    for f in files:
        file_path = os.path.join(cur_folder, f)
        if f.lower().endswith(".txt"):
            try:
                with open(file_path,'r') as file:
                    content = file.read()
                    searched_phones = phone_pattern.findall(content)
                    if (len(searched_phones) > 0):
                        print(searched_phones)
            except Exception as e:
                print(f" Could not read {f}: {e}")