from pypdf import PdfReader
import os

output_folder = "../content/"
file_name = "Chemistry Questions.pdf"

try:
    file_path = output_folder + file_name
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    reader = PdfReader(file_path)

    output_file_path = output_folder + "project1_output.txt"

    with open(output_file_path, 'w') as file:
        for i, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            file.write(text)

    print(f"The {file_name}'s content extract has been stored at '{output_file_path}'")

except FileNotFoundError as e:
    print(e)

except Exception as e:
    print(f"An error occurred: {e}")