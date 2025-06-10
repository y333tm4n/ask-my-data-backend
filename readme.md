# Data Backend for Document Parsing and LLM Integration

This backend is a Flask-based API designed to parse documents, generate embeddings, and interact with LLMs (such as Gemini) using LangChain. It supports file uploads, text extraction, and vector storage for semantic search.

## Features
- **File Upload & Parsing:** Supports PDF (via PyMuPDF), DOCX, and other formats (extensible).
- **Text Embedding & Vector Store:** Uses LangChain with FAISS for storing and retrieving text embeddings.
- **LLM Integration:** Connects to Google Gemini via LangChain for question answering.
- **CORS Enabled:** Allows cross-origin requests for frontend integration.

## Project Structure
```
app/
  __init__.py        # Flask app factory
  routes.py          # API endpoints for file upload and LLM Q&A
  file_parser.py     # File parsing logic (PDF, DOCX, etc.)
  gemini_chain.py    # LangChain + Gemini integration
  vector_store.py    # Vector store logic (FAISS/Chroma)
  utils.py           # (Reserved for utility functions)
run.py               # Entry point for running the Flask app
requirements.txt     # Python dependencies
```

## Setup Instructions

### 1. Clone the Repository
```sh
git clone <repo-url>
cd data-backend
```

### 2. Create and Activate a Virtual Environment
```sh
python -m venv .venv
.\.venv\Scripts\Activate  # On Windows
# source .venv/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory and add your Google API key:
```
GOOGLE_API_KEY=your_google_api_key_here
```

### 5. Run the Application
```sh
python run.py
```
The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### `POST /upload`
- **Description:** Upload a file (PDF, DOCX, etc.) for parsing.
- **Request:** Multipart form with a `file` field.
- **Response:**
  ```json
  { "parsed_text": "...extracted text..." }
  ```

### `POST /ask`
- **Description:** Ask a question to the LLM (Gemini) using the parsed/embedded data.
- **Request:** JSON body with a `question` field.
- **Response:**
  ```json
  { "response": "...LLM answer..." }
  ```

## Extending the Backend
- Add more file types in `file_parser.py`.
- Implement advanced vector search in `vector_store.py`.
- Integrate additional LLMs or embedding models as needed.

## Dependencies
See `requirements.txt` for all dependencies, including:
- Flask, flask-cors
- PyMuPDF, python-docx, chardet, python-magic
- langchain, langchain-google-genai, google-generativeai
- sentence-transformers, nltk, tiktoken
- faiss-cpu (or chromadb)
- python-dotenv, requests, pydantic


