from services.PdfTextExtractor import PdfExtractor

try:
    extractor = PdfExtractor()
    extractor.load_pdf()
    text = extractor.extract_text_from_all_pages()
    extractor.write_text_to_output_file(text)
except FileNotFoundError as e:
    print(e)

except Exception as e:
    print(f"An error occurred: {e}")
