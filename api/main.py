from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.vehicles import router as vehicles_router
from api.maintenances import router as maintenances_router


app = FastAPI(
    title="AutoCare API",
    description="API para la gestión de vehículos y mantenimientos.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Bienvenido a AutoCare API"}


app.include_router(vehicles_router)
app.include_router(maintenances_router)