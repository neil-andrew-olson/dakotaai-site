import PyPDF2
import sys
import os

pdf_path = 'NVDA.pdf'

try:
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
    with open('nvda_text.txt', 'w', encoding='utf-8') as outfile:
        outfile.write(text)
    print(f"Text extracted successfully to nvda_text.txt ({len(text)} characters)")
except Exception as e:
    print(f"Error extracting text: {e}", file=sys.stderr)
