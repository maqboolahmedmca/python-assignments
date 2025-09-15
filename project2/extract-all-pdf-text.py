import os
from pypdf import PdfReader
import shutil

content_dir='content'
output_dir='output'


def extract_pdftext():
    """
    Walks through folder and subfolders & creates the output.txt at folder level.
    """     
    for dirpath, dirnames, filenames in os.walk(content_dir):
        print(f"Current directory: {dirpath}")
        output_dir = create_output_dir(dirpath)

        for filename in filenames:
            if (filename.endswith('.pdf')):
                pdf_file_path = os.path.join(dirpath, filename)
                print(f"  File: {pdf_file_path}")
                if not os.path.exists(pdf_file_path):
                    raise FileNotFoundError(f"File not found: {pdf_file_path}")
                
                reader = PdfReader(pdf_file_path)

                output_file_path = output_dir + "/output.txt"

                with open(output_file_path, 'w') as file:
                    for i, page in enumerate(reader.pages, start=1):
                        text = page.extract_text()
                        file.write(text)

                print(f"The {filename}'s content extract has been stored at '{output_file_path}'")
        
        print("-" * 20)


def create_output_dir(dirpath):
    path = dirpath + "/" + output_dir
    os.makedirs(path, exist_ok=True) 
    return path

def rearrange_pdf_files():
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
extract_pdftext()