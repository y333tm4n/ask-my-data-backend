import fitz  # PyMuPDF

def parse_file(file):
    if file.filename.endswith(".pdf"):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    # Add DOCX, TXT parsing too
