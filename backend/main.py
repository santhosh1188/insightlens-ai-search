from fastapi import FastAPI, UploadFile
import chromadb
from openai import OpenAI
import PyPDF2
import docx

app = FastAPI()
client = OpenAI()

chroma_client = chromadb.Client()
collection = chroma_client.create_collection("documents")

def extract_text(file: UploadFile):
    if file.filename.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file.file)
        return "\n".join([p.extract_text() for p in reader.pages])

    if file.filename.endswith(".docx"):
        doc = docx.Document(file.file)
        return "\n".join([p.text for p in doc.paragraphs])

    return file.file.read().decode()

@app.post("/upload")
async def upload_file(file: UploadFile):
    text = extract_text(file)

    embedding = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    ).data[0].embedding

    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[file.filename]
    )

    return {"message": "Uploaded successfully!"}
