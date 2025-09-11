from pypdf import PdfReader

output_folder = "../content/"
file_name = "Chemistry Questions.pdf"
reader = PdfReader(output_folder + file_name)

file_path = output_folder + "project1_output.txt"

with open(file_path, 'w') as file:
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        file.write(text)

print(f"The {file_name}'s content extract has been stored at '{file_path}'")