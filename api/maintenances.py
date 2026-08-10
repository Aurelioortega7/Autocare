from fastapi import APIRouter, HTTPException

from database import (
    get_maintenances_by_vehicle,
    add_maintenance,
    update_maintenance,
    delete_maintenance_db,
    get_vehicle_by_id
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

    vehicle = get_vehicle_by_id(vehicle_id)

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="El vehículo no existe."
        )

    maintenances = get_maintenances_by_vehicle(vehicle_id)

    return [dict(maintenance) for maintenance in maintenances]


@router.post(
    "/maintenances",
    summary="Añade un nuevo mantenimiento"
)
def create_maintenance(maintenance: MaintenanceCreate):

    vehicle = get_vehicle_by_id(maintenance.vehicle_id)

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="El vehículo no existe."
        )

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
    rows_updated = update_maintenance(
        maintenance_id,
        maintenance.maintenance_type,
        maintenance.date,
        maintenance.kilometers,
        maintenance.cost,
        maintenance.notes
    )

    if rows_updated == 0:
        raise HTTPException(
            status_code=404,
            detail="El mantenimiento no existe."
        )

    return {
        "message": "Mantenimiento actualizado correctamente"
    }

@router.delete(
    "/maintenances/{maintenance_id}",
    summary="Elimina un mantenimiento"
)
def delete_maintenance_endpoint(maintenance_id: int):

    rows_deleted = delete_maintenance_db(maintenance_id)

    if rows_deleted == 0:
        raise HTTPException(
            status_code=404,
            detail="El mantenimiento no existe."
        )

    return {
        "message": "Mantenimiento eliminado correctamente"
    }