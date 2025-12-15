from PyPDF2 import PdfReader
from docx import Document

def extract_text_from_pdf(path):
    text = ""
    reader = PdfReader(path)
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

def extract_text_from_docx(path):
    doc = Document(path)
    return " ".join([para.text for para in doc.paragraphs])
