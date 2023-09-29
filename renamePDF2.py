import os
import re
import pdfplumber
import shutil

# Function to extract the 14-digit number from a PDF file
def extract_number(pdf_file):
    text = ""
    
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            text += page_text  # Concatenate text from all pages
    
    number_match = re.search(r'\b73\d{12}\b', text)
    if number_match:
        number = number_match.group(0)
        return number
    
    return None

# Function to rename PDF files based on the 14-digit number and move them to the destination folder
def rename_and_move_pdf_files(source_folder, dest_folder):
    # Create the destination folder if it doesn't exist
    os.makedirs(dest_folder, exist_ok=True)
    
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.pdf'):
            pdf_file = os.path.join(source_folder, filename)
            number = extract_number(pdf_file)
            if number:
                new_filename = f"{number}.pdf"
                dest_filepath = os.path.join(dest_folder, new_filename)
                shutil.move(pdf_file, dest_filepath)  # Move the renamed file to the destination folder
                print(f"Renamed and moved '{filename}' to '{dest_filepath}'")

if __name__ == "__main__":
    source_folder = r"C:\Users\Mateo\Desktop\code\AFIP_CAE\ejemplos"  # Replace with the path to your folder of PDF files
    dest_folder = r"C:\Users\Mateo\Desktop\code\AFIP_CAE\ejemplos\Renombradas"  # Destination folder
    rename_and_move_pdf_files(source_folder, dest_folder)

