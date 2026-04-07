from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.notes.endpoints import router as notes_router

app = FastAPI()

#confiogurar CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], #TODO: cambiar a la urls de frontend para mejorar seguridad
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(notes_router)

#endpoint basico

@app.get('/')
def read_root():
    return {'message': 'hellow world!'}




