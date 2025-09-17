## Project 4
Read regular expression from a config file and extract content

## Requirements
* Update project 3
* Add support for a configuration file 
* In the configuration file set a config with key “regex” and value some regular expression that will match a part of the content in the PDF
* Update code to extract only the content matching the regular expression 
* Write to the output file

## Error Handling
* Take care of case where folder is not available
* Take care of case where PDF file is not present in a sub-folder
* Take care of case where the output.txt file is not available in a sub-folder
* Take care of case where no configuration file is available
* Take care of the case where configuration file does not have the regular expression


Note: It uses [pypdf](https://github.com/py-pdf/pypdf) library

# Install dependencies
pip install pypdf

# Content Resources
It uses `/content/Chemistry Questions.pdf`, extracts the text  & stores it in to `./output.txt`.

# How to Run?
python3 extract_pdf_text_regex.py
