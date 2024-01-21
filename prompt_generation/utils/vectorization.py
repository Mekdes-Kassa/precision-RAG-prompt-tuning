from pinecone import Pinecone
from dotenv import load_dotenv, find_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from preprocessing import chunk_text
import os
import time
import hashlib

class PineconeIndexer:
    def __init__(self, api_key, index_name, model="text-embedding-ada-002"):
        self.pc = Pinecone(api_key=api_key)
        self.index = self.pc.Index(index_name)
        self.embed_model = OpenAIEmbeddings(model=model)

    def embed_and_upsert(self, chunks):
        res = self.embed_model.embed_documents(chunks)

        for chunk, embedding in zip(chunks, res):
            document_id = self.generate_unique_id_for_chunk(chunk)
            self.index.upsert(vectors=[(document_id, embedding)], metadata=[{"text": chunk}])

    @staticmethod
    def generate_unique_id_for_chunk(chunk):
        timestamp = str(time.time())
        chunk_hash = hashlib.sha256(chunk.encode()).hexdigest()
        unique_id = f"{timestamp}_{chunk_hash}"
        return unique_id

if __name__ == "__main__":
    load_dotenv(find_dotenv())
    api_key = os.getenv("PINECONE_API_KEY")

    pdf_extractor = PDFTextExtractor("/home/hp/Documents/week 5/precision-RAG-prompt-tuning/prompt_generation/challenge.pdf")
    extracted_text = pdf_extractor.extract_text_from_pdf()

    chunk_size = 50
    overlap = 20
    chunks = pdf_extractor.chunk_text(extracted_text, chunk_size, overlap)

    indexer = PineconeIndexer(api_key=api_key, index_name="mekdes-index")
    indexer.embed_and_upsert(chunks)
