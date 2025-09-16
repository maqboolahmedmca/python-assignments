import os
from pdf_text_extractor.PdfTextExtractor import PdfExtractor

content_dir='content'
output_dir='output'

def recursive_extract_all_pdf_text():
    """
    Walks through folder and subfolders & creates the output.txt at folder level.
    """   
    try:  
        if not os.path.exists(content_dir):
            raise FileNotFoundError(f"Error! Content directory not found: {content_dir}")
        
        for dirpath, dirnames, filenames in os.walk(content_dir):
            print(f"Current directory: {dirpath}")

            for filename in filenames:
                if (filename.endswith('.pdf')):
                    extractor = PdfExtractor(pdf_file_path=filename, content_dir=dirpath, output_dir=dirpath + '/' + output_dir)
                    extractor.load_pdf()
                    text = extractor.extract_text_from_all_pages()
                    extractor.write_text_to_output_file(text, 'a')
    except FileNotFoundError as e:
        print(e)

    except Exception as e:
        print(f"An error occurred: {e}")

recursive_extract_all_pdf_text()