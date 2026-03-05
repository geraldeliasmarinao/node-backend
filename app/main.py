from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.client.firestore import get_firestore_client

app = FastAPI()

#confiogurar CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], #TODO: cambiar a la urls de frontend para mejorar seguridad
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

#endpoint basico

@app.get('/')
def read_root():
    return {'message': 'hellow world!'}


@app.get("/notes")
async def get_notes():
    db = get_firestore_client()
    collection_ref = db.collection("test-notes")
    
    notes = []
    
    docs = collection_ref.stream()
    for doc in docs:
        note_data = doc.to_dict()
        notes.append(note_data)
        
        return {"notes": notes }
