import os
import re
from PyPDF2 import PdfReader

# Function to extract the "CAE N°:" number from a PDF file
def extract_cae_number(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text = page.extract_text()
        match = re.search(r'CAE N°:\s*(\d+)', text)
        if match:
            return match.group(1)
    return None

# Function to rename PDF files based on the "CAE N°:" number
def rename_pdf_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            pdf_file = os.path.join(folder_path, filename)
            cae_number = extract_cae_number(pdf_file)
            if cae_number:
                new_filename = f"CAE_{cae_number}.pdf"
                new_filepath = os.path.join(folder_path, new_filename)
                os.rename(pdf_file, new_filepath)
                print(f"Renamed '{filename}' to '{new_filename}'")

if __name__ == "__main__":
    folder_path = r"C:\Users\Mateo\Desktop\code\AFIP_CAE\ejemplos"  # Replace with the path to your folder of PDF files
    rename_pdf_files(folder_path)


