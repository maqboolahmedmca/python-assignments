export PYTHONPATH=$(pwd)/..

rm -rf content
unzip content.zip

python3 rearrange_pdf_files.py
echo 'Finished rearranging PDF files.'

echo 'Starting recursive extraction of all PDF text...'
python3 recursive_extract_all_pdf_text.py