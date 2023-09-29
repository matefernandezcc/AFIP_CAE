import os
import re
from pdf2image import convert_from_path
import pytesseract

# Function to perform OCR on an image
def ocr_image(image_path):
    return pytesseract.image_to_string(image_path, lang='eng')

# Function to extract the "CAE N°:" number from a PDF file using OCR
def extract_cae_number_ocr(pdf_file):
    pages = convert_from_path(pdf_file)
    for i, page in enumerate(pages):
        image_path = f"page_{i}.png"
        page.save(image_path, 'PNG')
        text = ocr_image(image_path)
        os.remove(image_path)
        match = re.search(r'CAE N°:\s*(\d+)', text)
        if match:
            return match.group(1)
    return None

# Function to rename PDF files based on the "CAE N°:" number using OCR
def rename_pdf_files_with_ocr(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            pdf_file = os.path.join(folder_path, filename)
            cae_number = extract_cae_number_ocr(pdf_file)
            if cae_number:
                new_filename = f"{cae_number}.pdf"
                new_filepath = os.path.join(folder_path, new_filename)
                os.rename(pdf_file, new_filepath)
                print(f"Renamed '{filename}' to '{new_filename}'")

if __name__ == "__main__":
    folder_path = "C:\Users\Mateo\Desktop\code\AFIP_CAE\ejemplos"  # Replace with the path to your folder of PDF files
    rename_pdf_files_with_ocr(folder_path)
