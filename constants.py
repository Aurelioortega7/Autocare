MAINTENANCE_TYPES = [
    "Cambio de aceite",
    "ITV",
    "Frenos",
    "Neumáticos",
    "Batería",
    "Filtros",
    "Otro"
]

MAINTENANCE_LIMITS = {
    "Cambio de aceite": {
        "max_km": 10000,
        "max_days": 365
    },
    "Frenos": {
        "max_km": 30000,
        "max_days": 730
    },
    "Neumáticos": {
        "max_km": 40000,
        "max_days": 1825
    },
    "Batería": {
        "max_km": None,
        "max_days": 1825
    },
    "Filtros": {
        "max_km": 20000,
        "max_days": 365
    }
}

ITV_VALIDITY_DAYS = 365