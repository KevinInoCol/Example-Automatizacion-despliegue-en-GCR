from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# Endpoint raíz
@app.get("/")
def read_root():
    return {"mensaje": "¡Bienvenido a mi API con FastAPI!"}

# Endpoint GET adicional
@app.get("/mensaje")
def obtener_mensaje():
    return JSONResponse(content={"mensaje": "Este es otro mensaje desde el endpoint /mensaje"})
