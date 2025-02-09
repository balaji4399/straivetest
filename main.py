# from fastapi import FastAPI, HTTPException, Query
# from fastapi.middleware.cors import CORSMiddleware
# import json

# app = FastAPI()

# # CORS setup
# origins = ["*"]  # Allow all origins
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],  # Only allow GET requests
#     allow_headers=["*"],
# )
# file_path = 'q-vercel-python.json'
# with open(file_path, 'r') as f:
#     students_marks_list = json.load(f)

# # Convert the list of dictionaries to a dictionary
# students_marks = {student['name']: student['marks'] for student in students_marks_list}
# # Load student data (replace with your actual file loading)
# # Handle the case where the file isn't found.  Provide some default data if needed.

# @app.get("/api")
# async def get_marks(name: list[str] = Query(None)): # Allows for multiple name parameters
#     if name is None:
#         raise HTTPException(status_code=400, detail="At least one name must be provided.")

#     marks = []
#     not_found = []
#     for n in name:
#       if n in students_marks:
#         marks.append(students_marks[n])
#       else:
#         not_found.append(n)

#     if not_found:
#       error_message = f"Names not found: {', '.join(not_found)}"
#       if marks: # some names were found
#           return {"marks": marks, "message": error_message}
#       else: # no names were found
#           raise HTTPException(status_code=404, detail=error_message)

#     return {"marks": marks}
# # import base64

# # # Basic encoding/decoding
# # text = "Hello, World!"
# # # Convert text to base64
# # encoded = base64.b64encode(text.encode()).decode()  # SGVsbG8sIFdvcmxkIQ==
# # # Convert base64 back to text
# # decoded = base64.b64decode(encoded).decode()        # Hello, World!
# # # Convert to URL-safe base64
# # url_safe = base64.urlsafe_b64encode(text.encode()).decode()  # SGVsbG8sIFdvcmxkIQ==

# # # Working with binary files (e.g., images)
# # with open('download.png', 'rb') as f:
# #     binary_data = f.read()
# #     image_b64 = base64.b64encode(binary_data).decode()

# # # Data URI example (embed images in HTML/CSS)
# # data_uri = f"data:image/png;base64,{image_b64}"
# # print(data_uri)

# {
#   "model": "gpt-4o-mini",
#   "messages": [
#     {
#       "role": "user",
#       "content": [
#         {
#           "type": "text",
#           "text": "Extract text from this image."
#         },
#         {
#           "type": "image_url",
#           "image_url": {
#             "url": "data:image/png;base64,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"
#           }
#         }
#       ]
#     }
#   ]
# }

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import openai
import numpy as np

# Initialize FastAPI app
app = FastAPI()

# Enable CORS (allow all origins, methods, and headers)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["OPTIONS", "POST"],
    allow_headers=["*"],
)

# OpenAI API Key (ensure you set this in your environment)
openai.api_key = "your_openai_api_key"

# Request model
class SimilarityRequest(BaseModel):
    docs: List[str]
    query: str

# Function to generate embeddings
def get_embedding(text: str):
    response = openai.Embedding.create(
        input=text, model="text-embedding-3-small"
    )
    return np.array(response["data"][0]["embedding"])

# Function to compute cosine similarity
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

@app.post("/similarity")
async def find_similar_docs(request: SimilarityRequest):
    try:
        # Generate embedding for query
        query_embedding = get_embedding(request.query)

        # Generate embeddings for documents
        doc_embeddings = [get_embedding(doc) for doc in request.docs]

        # Compute cosine similarity
        similarities = [cosine_similarity(query_embedding, doc_emb) for doc_emb in doc_embeddings]

        # Get top 3 matching documents
        top_indices = np.argsort(similarities)[-3:][::-1]  # Get indices of top 3 matches
        top_matches = [request.docs[i] for i in top_indices]

        return {"matches": top_matches}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
