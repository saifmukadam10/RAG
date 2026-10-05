from pathlib import Path
from typing import List, Optional, Tuple, Any
from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    CSVLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredPowerPointLoader,
)
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders.excel import UnstructuredExcelLoader
from langchain_community.document_loaders import JSONLoader


def load_all_documents(data_dir: str) -> List[Any]:
    """
    Load all documents from the specified data directory.

    Args:
        data_dir (str): The path to the data directory.

    Returns:
        List[Any]: A list of loaded documents.
    """
    data_path = Path(data_dir).resolve()
    documents = []

    # Load PDF files
    pdf_files = list(data_path.glob("**/*.pdf"))
    print(f"[DEBUG] Found {len(pdf_files)} PDF files: {[str(f) for f in pdf_files]}")
    for pdf_file in pdf_files:
        try:
            loader = PyPDFLoader(str(pdf_file))
            documents.extend(loader.load())

        except Exception as e:
            print(f"[ERROR] Failed to load PDF file {pdf_file}: {e}")
            continue

    # Load text files
    text_files = list(data_path.glob("**/*.txt"))
    print(f"[DEBUG] Found {len(text_files)} text files: {[str(f) for f in text_files]}")
    for text_file in text_files:
        try:
            loader = TextLoader(str(text_file))
            documents.extend(loader.load())
        except Exception as e:
            print(f"[ERROR] Failed to load text file {text_file}: {e}")
            continue

    # Load CSV files
    csv_files = list(data_path.glob("**/*.csv"))
    print(f"[DEBUG] Found {len(csv_files)} CSV files: {[str(f) for f in csv_files]}")
    for csv_file in csv_files:
        try:
            loader = CSVLoader(str(csv_file))
            documents.extend(loader.load())
        except Exception as e:
            print(f"[ERROR] Failed to load CSV file {csv_file}: {e}")
            continue

    # Load Word documents
    word_files = list(data_path.glob("**/*.docx"))
    print(f"[DEBUG] Found {len(word_files)} Word files: {[str(f) for f in word_files]}")
    for word_file in word_files:
        try:
            loader = Docx2txtLoader(str(word_file))
            documents.extend(loader.load())
        except Exception as e:
            print(f"[ERROR] Failed to load Word file {word_file}: {e}")
            continue

    # Load Excel files
    excel_files = list(data_path.glob("**/*.xlsx"))
    print(
        f"[DEBUG] Found {len(excel_files)} Excel files: {[str(f) for f in excel_files]}"
    )
    for excel_file in excel_files:
        try:
            loader = UnstructuredExcelLoader(str(excel_file))
            documents.extend(loader.load())
        except Exception as e:
            print(f"[ERROR] Failed to load Excel file {excel_file}: {e}")
            continue

    # Load JSON files
    json_files = list(data_path.glob("**/*.json"))
    print(f"[DEBUG] Found {len(json_files)} JSON files: {[str(f) for f in json_files]}")
    for json_file in json_files:
        try:
            loader = JSONLoader(str(json_file))
            documents.extend(loader.load())
        except Exception as e:
            print(f"[ERROR] Failed to load JSON file {json_file}: {e}")
            continue

    return documents


check = load_all_documents(r"C:\Users\Saif\Documents\RAG\data")
check
