from pypdf import PdfReader
import os

class PdfExtractor:
    def __init__(self, pdf_file_path="Chemistry Questions.pdf", content_dir="../content/", output_dir="./", output_file="output.txt"):
        self.reader = None
        self.content_dir = content_dir
        self.pdf_file_path = os.path.join(self.content_dir, pdf_file_path)
        self.output_dir = output_dir
        self.output_file = os.path.join(self.output_dir, output_file)
        print(f"PDF File Path: {self.pdf_file_path}")
        print(f"Output File Path: {self.output_file}")

    def load_pdf(self):
        if not os.path.exists(self.pdf_file_path):
            raise FileNotFoundError(f"File not found: {self.pdf_file_path}")
        self.reader = PdfReader(self.pdf_file_path)
        print(f"PDF loaded successfully. Total pages: {len(self.reader.pages)}")
        return len(self.reader.pages)

    def extract_text_from_page(self, page_number):
        if self.reader is None:
            raise ValueError("PDF not loaded. Call load_pdf() first.")
        if page_number < 1 or page_number > len(self.reader.pages):
            raise ValueError(f"Page number must be between 1 and {len(self.reader.pages)}")
        print(f"Extracting text from page {page_number}")
        print("*" * 100)
        return self.reader.pages[page_number - 1].extract_text()

    def extract_text_from_all_pages(self):
        if self.reader is None:
            raise ValueError("PDF not loaded. Call load_pdf() first.")
        print("Extracting text from all pages")
        print("*" * 100)

        all_text = ""
        for page in self.reader.pages:
            all_text += page.extract_text()
        
        return all_text
    
    def extract_text_by_regex(self, pattern):
        import re
        if self.reader is None:
            raise ValueError("PDF not loaded. Call load_pdf() first.")
        all_text = self.extract_text_from_all_pages()
        print(f"Extracting text by regex pattern: '{pattern}'")
        print("*" * 100)
        return re.findall(pattern, all_text)
    
    def write_text_to_output_file(self, text, mode='w'):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        with open(self.output_file, mode, encoding='utf-8') as file:
            file.write(text)
            print(f"Extracted text written to {self.output_file}")
            print("*" * 100)