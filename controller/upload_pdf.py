from io import BytesIO
from pypdf import PdfReader


def get_text_from_pdf(pdf):
    reader = PdfReader(stream=pdf)

    text = ""

    for page in reader.pages:
        text += page.extract_text(extraction_mode="layout")
 
    return text
