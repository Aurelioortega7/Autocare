from pydantic import BaseModel


class VehicleCreate(BaseModel):
    brand: str
    model: str
    year: int
    license_plate: str
    kilometers: int