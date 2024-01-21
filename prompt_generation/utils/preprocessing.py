import PyPDF2

class pre_processing:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_text_from_pdf(self):
        with open(self.pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            extracted_text = ""

            for page in range(num_pages):
                page_obj = pdf_reader.pages[page]
                extracted_text += page_obj.extract_text()

            return extracted_text

    def chunk_text(self, extracted_text, chunk_size, overlap):
        chunks = []
        text_length = len(extracted_text)

        for start in range(0, text_length, chunk_size - overlap):
            end = min(start + chunk_size, text_length)
            chunk = extracted_text[start:end]
            chunks.append(chunk)

        return chunks

if __name__ == "__main__":
    pdf_extractor = PDFTextExtractor("/home/hp/Documents/week 5/precision-RAG-prompt-tuning/prompt_generation/challenge.pdf")
    extracted_text = pdf_extractor.extract_text_from_pdf()

    chunk_size = 50
    overlap = 20
    chunks = pdf_extractor.chunk_text(extracted_text, chunk_size, overlap)

    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}:", chunk)
