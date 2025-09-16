from pdf_text_extractor.PdfTextExtractor import PdfExtractor

try:
    extractor = PdfExtractor()
    page_limit=extractor.load_pdf()
    page_num=input(f"Enter a page number between 1 and {page_limit} to extract text from (or press Enter to extract from all pages): ")
    if page_num.strip().isdigit():
        page_num = int(page_num)
        text = extractor.extract_text_from_page(page_num)
    else:
        text = extractor.extract_text_from_all_pages()
    extractor.write_text_to_output_file(text)
except FileNotFoundError as e:
    print(e)

except Exception as e:
    print(f"An error occurred: {e}")
