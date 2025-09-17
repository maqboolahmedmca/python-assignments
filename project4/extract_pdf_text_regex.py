import os
import json 
import re
from services.PdfTextExtractor import PdfExtractor

# Load config.json
config_path = "config.json"
if not os.path.exists(config_path):
    raise FileNotFoundError(f"Error! Config file not found: {config_path}")

with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

# Get regex from config
pattern_str = config.get("regex")
if not pattern_str:
    raise ValueError("'regex' key not found in config.json")
else:
    print(f"Using regex pattern from config: {pattern_str}")
# Compile regex
pattern = re.compile(pattern_str)

try:
    extractor = PdfExtractor()
    page_limit=extractor.load_pdf()
    page_num=input(f"Enter a page number between 1 and {page_limit} to extract text from (or press Enter to extract from all pages): ")
    if page_num.strip().isdigit():
        page_num = int(page_num)
        text = extractor.extract_text_from_page(page_num)
    else:
        text = extractor.extract_text_from_all_pages()
        
    matches = pattern.findall(text)
    extractor.write_text_to_output_file('Here is extracted text by regex\n', 'w')
    for match in matches:
        extractor.write_text_to_output_file(match + '\n', 'a')
except FileNotFoundError as e:
    print(e)

except Exception as e:
    print(f"An error occurred: {e}")