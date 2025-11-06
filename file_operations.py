from PyPDF2 import PdfReader

def read_file(file_path):
    content = ""
    if file_path.endswith(".txt"):
        with open(file_path, "r") as file:
            content = file.read()
    elif file_path.endswith(".pdf"):
        pdf_reader = PdfReader(file_path)
        for page in pdf_reader.pages:
            content += page.extract_text()
    return content
