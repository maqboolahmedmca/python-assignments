import os
from pypdf import PdfReader
import shutil

content_dir='content'
output_dir='output'

def rearrange_pdf_files():
    if (not os.path.exists(content_dir)):
        print(f"Error! Content directory not found: {content_dir}")
        return
    pdf_files = get_pdf_files_os(content_dir)
    if (len(pdf_files) == 0):
        print("No pdf files to be arranged")
        return
    
    for pdf_file in pdf_files:
        folder_name = pdf_file.split('-')[0]
        dest_folder_path=content_dir+'/'+folder_name
        src_file=content_dir+'/'+pdf_file
        os.makedirs(dest_folder_path, exist_ok=True) 
        shutil.move(src_file, dest_folder_path)
        print(f"File '{src_file}' moved successfully to '{dest_folder_path}'.")

def get_pdf_files_os(folder_path):
        """
        Lists all PDF files in a given folder using os module.
        """
        pdf_files = []
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(".pdf") and os.path.isfile(os.path.join(folder_path, filename)):
                pdf_files.append(filename)
        return pdf_files

rearrange_pdf_files()