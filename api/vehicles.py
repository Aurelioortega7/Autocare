from fastapi import APIRouter, HTTPException
import sqlite3

from database import (
    add_vehicle,
    get_all_vehicles,
    get_vehicle_by_id,
    update_vehicle,
    delete_vehicle
)

from schemas.vehicle import VehicleCreate

router = APIRouter(
    tags=["Vehículos"]
)


@router.get(
    "/vehicles",
    summary="Obtiene todos los vehículos registrados"
)
def get_vehicles():

    vehicles = get_all_vehicles()

    return [dict(vehicle) for vehicle in vehicles]


@router.get(
    "/vehicles/{vehicle_id}",
    summary="Obtiene un vehículo por su ID"
)
def get_vehicle(vehicle_id: int):

    vehicle = get_vehicle_by_id(vehicle_id)

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehículo no encontrado."
        )

    return dict(vehicle)


@router.post(
    "/vehicles",
    summary="Añade un nuevo vehículo"
)
def create_vehicle(vehicle: VehicleCreate):

    try:
        add_vehicle(
            vehicle.brand,
            vehicle.model,
            vehicle.year,
            vehicle.license_plate,
            vehicle.kilometers
        )

        return {
            "message": "Vehículo añadido correctamente"
        }

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Ya existe un vehículo con esa matrícula."
        )


@router.put(
    "/vehicles/{vehicle_id}",
    summary="Actualiza un vehículo"
)
def update_vehicle_endpoint(
    vehicle_id: int,
    vehicle: VehicleCreate
):

    existing_vehicle = get_vehicle_by_id(vehicle_id)

    if existing_vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehículo no encontrado."
        )

    try:
        update_vehicle(
            vehicle_id,
            vehicle.brand,
            vehicle.model,
            vehicle.year,
            vehicle.license_plate,
            vehicle.kilometers
        )

        return {
            "message": "Vehículo actualizado correctamente"
        }

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Ya existe un vehículo con esa matrícula."
        )

@router.delete(
    "/vehicles/{vehicle_id}",
    summary="Elimina un vehículo"
)
def delete_vehicle_endpoint(vehicle_id: int):

    vehicle = get_vehicle_by_id(vehicle_id)

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehículo no encontrado."
        )

    delete_vehicle(vehicle_id)

    return {
        "message": "Vehículo eliminado correctamente"
    }