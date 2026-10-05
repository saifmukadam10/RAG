from pathlib import Path
from typing import List, Optional, Tuple, Any
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader, UnstructuredWordDocumentLoader, UnstructuredPowerPointLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders.excel import UnstructuredExcelLoader
from langchain_community.document_loaders import JSONLoader


def load_all_documents()