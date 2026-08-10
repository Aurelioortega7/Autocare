from fastapi import APIRouter

from database import (
    get_maintenances_by_vehicle,
    add_maintenance,
    update_maintenance,
    delete_maintenance_db
)

from schemas.maintenance import MaintenanceCreate


router = APIRouter(
    tags=["Mantenimientos"]
)


@router.get(
    "/maintenances/{vehicle_id}",
    summary="Obtiene los mantenimientos de un vehículo"
)
def get_maintenances(vehicle_id: int):

    maintenances = get_maintenances_by_vehicle(vehicle_id)

    return [dict(maintenance) for maintenance in maintenances]


@router.post(
    "/maintenances",
    summary="Añade un nuevo mantenimiento"
)
def create_maintenance(maintenance: MaintenanceCreate):

    add_maintenance(
        maintenance.vehicle_id,
        maintenance.maintenance_type,
        maintenance.date,
        maintenance.kilometers,
        maintenance.cost,
        maintenance.notes
    )

    return {
        "message": "Mantenimiento añadido correctamente"
    }

@router.put(
    "/maintenances/{maintenance_id}",
    summary="Actualiza un mantenimiento"
)
def update_maintenance_endpoint(
    maintenance_id: int,
    maintenance: MaintenanceCreate
):
    update_maintenance(
        maintenance_id,
        maintenance.maintenance_type,
        maintenance.date,
        maintenance.kilometers,
        maintenance.cost,
        maintenance.notes
    )

    return {
        "message": "Mantenimiento actualizado correctamente"
    }

@router.delete(
    "/maintenances/{maintenance_id}",
    summary="Elimina un mantenimiento"
)
def delete_maintenance_endpoint(maintenance_id: int):

    delete_maintenance_db(maintenance_id)

    return {
        "message": "Mantenimiento eliminado correctamente"
    }