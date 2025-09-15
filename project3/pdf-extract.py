from pypdf import PdfReader
import os
import sys

print(sys.argv)
if len(sys.argv) == 1:
    print("No command line arguments provided.")
    print("Usage: python pdf-extract.py 1 (page number)")
    sys.exit(1)

page = sys.argv[1]
if (page.isnumeric() == False):
    print("Please provide a valid page number.")
    sys.exit(1)

pageNum = int(page)
output_folder = "../content/"
file_name = "Chemistry Questions.pdf"

try:
    file_path = output_folder + file_name
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    reader = PdfReader(file_path)

    if (len(reader.pages) <= pageNum or pageNum <= 1):
        print(f"Please provide a valid page number between 1 and {len(reader.pages)}.")
        sys.exit(1)

    output_file_path = output_folder + "project3_output.txt"

    with open(output_file_path, 'w') as file:
        text = reader.pages[pageNum-1].extract_text()
        file.write(text)
            

    print(f"The {file_name}'s content extract has been stored at '{output_file_path}'")

except FileNotFoundError as e:
    print(e)

except Exception as e:
    print(f"An error occurred: {e}")