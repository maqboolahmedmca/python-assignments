# What is it?
It's a pdf text extract tool. 

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
    * ./run.sh
