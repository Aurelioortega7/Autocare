from pydantic import BaseModel


class MaintenanceCreate(BaseModel):
    vehicle_id: int
    maintenance_type: str
    date: str
    kilometers: int
    cost: float
    notes: str | None = None