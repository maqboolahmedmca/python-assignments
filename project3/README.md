# Project 3
Read content from a particular page

## Requirements
* Update project 1 and update the reading of content 
* Take a page number as an input from command prompt
* Read content of the page number provided and write to the output file

## Error Handling
* Take care of case where folder is not available
* Take care of case where PDF file is not present in a sub-folder
* Take care of case where the output.txt file is not available in a sub-folder

Note: It uses [pypdf](https://github.com/py-pdf/pypdf) library

# Install dependencies
pip install pypdf

# Content Resources
It uses `/content/Chemistry Questions.pdf`, extracts the text  & stores it in to `./output.txt`.

# How to Run?
python3 extract_pdf_page_text.py
