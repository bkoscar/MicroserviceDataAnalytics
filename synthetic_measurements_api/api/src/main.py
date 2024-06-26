from fastapi import FastAPI, APIRouter, HTTPException, status
from fastapi.staticfiles import StaticFiles
from .services.generator import DataGenerator

app = FastAPI()

# Montar el directorio estático
app.mount("/static", StaticFiles(directory="src/static"), name="static")

router = APIRouter()

@router.get("/measurements/", status_code=status.HTTP_200_OK)
async def get_synthetic_measurements():
    try:
        data_points = DataGenerator.generate_data_points()
        if not data_points:
            raise HTTPException(status_code=404, detail="No data points generated")
        return {"status": "success", "data": data_points}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

app.include_router(router)

# Redirigir la raíz a la página de bienvenida
@app.get("/")
async def root():
    return {"message": "Welcome! Visit /static/index.html for the welcome page."}