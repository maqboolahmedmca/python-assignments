# Project 1
Read a pdf file from a folder. Refer to the PDF file Chemistry Questions.pdf

## Requirements
* Store a PDF file in a folder called “/content”
* Read PDF file from the folder
* Write the content to a text file called “output.txt”
* Store this file under the “/content” folder

## Error Handling
* Take care of case where folder is not available
* Take care of case where PDF file is not present in the content folder
* Take care of case where the output.txt file is not available

Note: It uses [pypdf](https://github.com/py-pdf/pypdf) library

# Install dependencies
pip install pypdf

# Content Resources
It uses `/content/Chemistry Questions.pdf`, extracts the text  & stores it in to `./output.txt`.

# How to Run?
./run.sh
