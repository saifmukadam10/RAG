from src.rag.data_loader import load_all_documents
from pathlib import Path
from typing import List, Optional, Tuple, Any
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
import numpy as np


class EmbeddingPipeline:
    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",
        chunk_size: int = 200,
        chunk_overlap: int = 100,
    ):
        self.model = SentenceTransformer(model_name)
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        print(f"[INFO] Loaded embedding model: {model_name}")

    def chunk_documents(self, documents: List[Any]) -> List[Any]:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""],
        )
        chunks = text_splitter.split_documents(documents)
        return chunks

    def embed_chunks(self, chunks: List[Any]) -> np.ndarray:
        texts = [chunk.page_content for chunk in chunks]
        embeddings = self.model.encode(texts, show_progress_bar=True)
        return embeddings
