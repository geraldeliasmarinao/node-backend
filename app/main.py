from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
