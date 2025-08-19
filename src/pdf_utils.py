import fitz  # PyMuPDF

def extract_text_from_pdf(file) -> str:
    """
    Extracts text from a PDF file.

    Args:
        file: A file-like object (e.g., from st.file_uploader or an open file).

    Returns:
        str: Extracted text from the PDF, or an empty string if extraction fails.
    """
    text = ""
    if file is not None:
        try:
            # Reset pointer in case file was already read
            file.seek(0)
            # Open the PDF file using PyMuPDF
            pdf_document = fitz.open(stream=file.read(), filetype="pdf")

            # Iterate through each page and extract text
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)
                text += page.get_text("text") + "\n"
            pdf_document.close() # Close the PDF document


        except Exception as e:
            # Raise instead of handling with st.error (keeps this util independent)
            raise RuntimeError(f"Error reading PDF: {str(e)}")
        
    return text.strip() if text else "" # Return empty string if no text was extracted
