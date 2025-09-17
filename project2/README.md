# Project 2
Traverse through folder tree and filter pdf files

## Requirements
* Add sub-folders called “One”, “Two”, “Three” under the folder called “/content”
* Add PDF files under each of the sub-folders
* Load all PDF files under the sub-folders and load the PDF content
* Write the content to a text file called “output.txt” under each sub-folder respectively

## Error Handling
* Take care of case where folder is not available
* Take care of case where PDF file is not present in a sub-folder
* Take care of case where the output.txt file is not available in a sub-folder

Note: It uses [pypdf](https://github.com/py-pdf/pypdf) library

# Install dependencies
pip install pypdf

# Content Resources
It uses `/content/` folder to recursively walk through the folder & subfolder to list the pdf files, then extracts the pdf text & stores it in to `./output.txt`.

# How to Run?

1. Re-arrange files (One time)
    * The folder has content.zip file, extract it.
    * run 'python3 rearrange_pdf_files.py' to arrange the pdfs in subfolders

2. Extract pdf text from all recursively
    * ./run.sh (runs Step 1 as well)
