from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {
        "matricula": "2024118ISINF0001",
        "nome": "HELLEN CRISTINA DE CASTRO SOUSA"
    }
