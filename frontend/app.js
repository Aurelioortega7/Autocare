const API_URL = "http://127.0.0.1:8000";


async function loadVehicles() {

    const container =
        document.getElementById("vehicles-container");

    try {

        const response =
            await fetch(`${API_URL}/vehicles`);

        if (!response.ok) {
            throw new Error();
        }

        const vehicles =
            await response.json();

        if (vehicles.length === 0) {

            container.innerHTML = `
                <p>
                    No hay vehículos registrados.
                </p>
            `;

            return;
        }

        container.innerHTML = "";

        vehicles.forEach(vehicle => {

            const element =
                document.createElement("div");

            element.className =
                "vehicle-card";

            element.innerHTML = `

                <h3>
                    ${escapeHtml(vehicle.brand)}
                    ${escapeHtml(vehicle.model)}
                </h3>

                <p>
                    <strong>Año:</strong>
                    ${vehicle.year}
                </p>

                <p>
                    <strong>Matrícula:</strong>
                    ${escapeHtml(vehicle.license_plate)}
                </p>

                <p>
                    <strong>Kilómetros:</strong>
                    ${vehicle.kilometers}
                </p>

                <div class="vehicle-actions">

                    <button
                        onclick="viewMaintenances(${vehicle.id})"
                    >
                        Ver mantenimientos
                    </button>

                    <button
                        onclick="addMaintenance(${vehicle.id})"
                    >
                        Añadir mantenimiento
                    </button>

                    <button
                        onclick="editVehicle(${vehicle.id})"
                    >
                        Editar
                    </button>

                    <button
                        onclick="deleteVehicle(${vehicle.id})"
                    >
                        Eliminar
                    </button>

                </div>
            `;

            container.appendChild(element);
        });

    } catch (error) {

        console.error(error);

        container.innerHTML = `
            <p>
                Error al cargar los vehículos.
            </p>
        `;
    }
}


function openVehicleForm() {

    const section =
        document.getElementById(
            "vehicle-form-section"
        );

    section.classList.remove("hidden");

    section.scrollIntoView({
        behavior: "smooth"
    });
}


function closeVehicleForm() {

    const section =
        document.getElementById(
            "vehicle-form-section"
        );

    const form =
        document.getElementById(
            "vehicle-form"
        );

    form.reset();

    section.classList.add("hidden");
}


document
    .getElementById("vehicle-form")
    .addEventListener(
        "submit",
        async function(event) {

            event.preventDefault();

            const brand =
                document.getElementById(
                    "vehicle-brand"
                ).value.trim();

            const model =
                document.getElementById(
                    "vehicle-model"
                ).value.trim();

            const year =
                Number(
                    document.getElementById(
                        "vehicle-year"
                    ).value
                );

            const licensePlate =
                document.getElementById(
                    "vehicle-license-plate"
                ).value.trim();

            const kilometers =
                Number(
                    document.getElementById(
                        "vehicle-kilometers"
                    ).value
                );

            try {

                const response =
                    await fetch(
                        `${API_URL}/vehicles`,
                        {
                            method: "POST",

                            headers: {
                                "Content-Type":
                                    "application/json"
                            },

                            body: JSON.stringify({
                                brand: brand,
                                model: model,
                                year: year,
                                license_plate:
                                    licensePlate,
                                kilometers:
                                    kilometers
                            })
                        }
                    );

                const result =
                    await response.json();

                if (!response.ok) {

                    alert(
                        result.detail ||
                        "No se pudo añadir el vehículo."
                    );

                    return;
                }

                alert(
                    "Vehículo añadido correctamente."
                );

                closeVehicleForm();

                loadVehicles();

            } catch (error) {

                console.error(error);

                alert(
                    "Error al conectar con la API."
                );
            }
        }
    );


async function editVehicle(vehicleId) {

    try {

        const response =
            await fetch(
                `${API_URL}/vehicles/${vehicleId}`
            );

        const vehicle =
            await response.json();

        if (!response.ok) {

            alert(
                vehicle.detail ||
                "No se pudo obtener el vehículo."
            );

            return;
        }

        document.getElementById(
            "edit-vehicle-id"
        ).value = vehicle.id;

        document.getElementById(
            "edit-vehicle-brand"
        ).value = vehicle.brand;

        document.getElementById(
            "edit-vehicle-model"
        ).value = vehicle.model;

        document.getElementById(
            "edit-vehicle-year"
        ).value = vehicle.year;

        document.getElementById(
            "edit-vehicle-license-plate"
        ).value =
            vehicle.license_plate;

        document.getElementById(
            "edit-vehicle-kilometers"
        ).value = vehicle.kilometers;

        const section =
            document.getElementById(
                "edit-vehicle-form-section"
            );

        section.classList.remove("hidden");

        section.scrollIntoView({
            behavior: "smooth"
        });

    } catch (error) {

        console.error(error);

        alert(
            "Error al conectar con la API."
        );
    }
}


function closeEditVehicleForm() {

    const section =
        document.getElementById(
            "edit-vehicle-form-section"
        );

    const form =
        document.getElementById(
            "edit-vehicle-form"
        );

    form.reset();

    section.classList.add("hidden");
}


document
    .getElementById("edit-vehicle-form")
    .addEventListener(
        "submit",
        async function(event) {

            event.preventDefault();

            const vehicleId =
                Number(
                    document.getElementById(
                        "edit-vehicle-id"
                    ).value
                );

            const brand =
                document.getElementById(
                    "edit-vehicle-brand"
                ).value.trim();

            const model =
                document.getElementById(
                    "edit-vehicle-model"
                ).value.trim();

            const year =
                Number(
                    document.getElementById(
                        "edit-vehicle-year"
                    ).value
                );

            const licensePlate =
                document.getElementById(
                    "edit-vehicle-license-plate"
                ).value.trim();

            const kilometers =
                Number(
                    document.getElementById(
                        "edit-vehicle-kilometers"
                    ).value
                );

            try {

                const response =
                    await fetch(
                        `${API_URL}/vehicles/${vehicleId}`,
                        {
                            method: "PUT",

                            headers: {
                                "Content-Type":
                                    "application/json"
                            },

                            body: JSON.stringify({
                                brand: brand,
                                model: model,
                                year: year,
                                license_plate:
                                    licensePlate,
                                kilometers:
                                    kilometers
                            })
                        }
                    );

                const result =
                    await response.json();

                if (!response.ok) {

                    alert(
                        result.detail ||
                        "No se pudo actualizar el vehículo."
                    );

                    return;
                }

                alert(
                    "Vehículo actualizado correctamente."
                );

                closeEditVehicleForm();

                loadVehicles();

            } catch (error) {

                console.error(error);

                alert(
                    "Error al conectar con la API."
                );
            }
        }
    );


async function viewMaintenances(vehicleId) {

    const section =
        document.getElementById(
            "maintenances-section"
        );

    const container =
        document.getElementById(
            "maintenances-container"
        );

    try {

        const vehicleResponse =
            await fetch(
                `${API_URL}/vehicles/${vehicleId}`
            );

        const vehicle =
            await vehicleResponse.json();

        if (!vehicleResponse.ok) {

            alert(
                vehicle.detail ||
                "No se pudo obtener el vehículo."
            );

            return;
        }

        const response =
            await fetch(
                `${API_URL}/maintenances/${vehicleId}`
            );

        const maintenances =
            await response.json();

        if (!response.ok) {

            alert(
                maintenances.detail ||
                "No se pudieron obtener los mantenimientos."
            );

            return;
        }

        const statisticsResponse =
            await fetch(
                `${API_URL}/maintenances/${vehicleId}/statistics`
            );

        const statistics =
            await statisticsResponse.json();

        if (!statisticsResponse.ok) {

            alert(
                statistics.detail ||
                "No se pudieron obtener las estadísticas."
            );

            return;
        }

        document.getElementById(
            "maintenance-vehicle-title"
        ).textContent =
            `Mantenimientos de ${vehicle.brand} ${vehicle.model}`;

        document.getElementById(
            "maintenance-vehicle-info"
        ).textContent =
            `Matrícula: ${vehicle.license_plate} · ${vehicle.kilometers} km`;

        document.getElementById(
            "stat-total-cost"
        ).textContent =
            `${Number(statistics.total_cost).toFixed(2)} €`;

        document.getElementById(
            "stat-current-year-cost"
        ).textContent =
            `${Number(statistics.current_year_cost).toFixed(2)} €`;

        document.getElementById(
            "stat-monthly-average"
        ).textContent =
            `${Number(statistics.monthly_average).toFixed(2)} €`;

        document.getElementById(
            "stat-maintenance-count"
        ).textContent =
            statistics.maintenance_count;

        section.classList.remove("hidden");

        if (maintenances.length === 0) {

            container.innerHTML = `
                <p>
                    Este vehículo no tiene
                    mantenimientos registrados.
                </p>
            `;

            section.scrollIntoView({
                behavior: "smooth"
            });

            return;
        }

        container.innerHTML = "";

        maintenances.forEach(
            maintenance => {

                const element =
                    document.createElement("div");

                element.className =
                    "maintenance-card";

                element.innerHTML = `

                    <h3>
                        ${escapeHtml(
                            maintenance.maintenance_type
                        )}
                    </h3>

                    <p>
                        <strong>Fecha:</strong>
                        ${escapeHtml(
                            maintenance.date
                        )}
                    </p>

                    <p>
                        <strong>Kilómetros:</strong>
                        ${maintenance.kilometers}
                    </p>

                    <p>
                        <strong>Coste:</strong>
                        ${Number(
                            maintenance.cost
                        ).toFixed(2)} €
                    </p>

                    <p>
                        <strong>Notas:</strong>
                        ${
                            maintenance.notes
                                ? escapeHtml(
                                    maintenance.notes
                                  )
                                : "Sin notas"
                        }
                    </p>

                    <div class="maintenance-actions">

                        <button
                            onclick="editMaintenance(
                                ${maintenance.id},
                                ${vehicleId}
                            )"
                        >
                            Editar
                        </button>

                        <button
                            onclick="deleteMaintenance(
                                ${maintenance.id},
                                ${vehicleId}
                            )"
                        >
                            Eliminar
                        </button>

                    </div>
                `;

                container.appendChild(element);
            }
        );

        section.scrollIntoView({
            behavior: "smooth"
        });

    } catch (error) {

        console.error(error);

        alert(
            "Error al conectar con la API."
        );
    }
}


function addMaintenance(vehicleId) {

    const section =
        document.getElementById(
            "maintenance-form-section"
        );

    document.getElementById(
        "maintenance-vehicle-id"
    ).value = vehicleId;

    section.classList.remove("hidden");

    section.scrollIntoView({
        behavior: "smooth"
    });
}


function closeMaintenanceForm() {

    const section =
        document.getElementById(
            "maintenance-form-section"
        );

    const form =
        document.getElementById(
            "maintenance-form"
        );

    form.reset();

    section.classList.add("hidden");
}


document
    .getElementById("maintenance-form")
    .addEventListener(
        "submit",
        async function(event) {

            event.preventDefault();

            const vehicleId =
                Number(
                    document.getElementById(
                        "maintenance-vehicle-id"
                    ).value
                );

            const maintenanceType =
                document.getElementById(
                    "maintenance-type"
                ).value.trim();

            const date =
                document.getElementById(
                    "maintenance-date"
                ).value.trim();

            const kilometers =
                Number(
                    document.getElementById(
                        "maintenance-kilometers"
                    ).value
                );

            const cost =
                Number(
                    document.getElementById(
                        "maintenance-cost"
                    ).value
                );

            const notes =
                document.getElementById(
                    "maintenance-notes"
                ).value.trim();

            try {

                const response =
                    await fetch(
                        `${API_URL}/maintenances`,
                        {
                            method: "POST",

                            headers: {
                                "Content-Type":
                                    "application/json"
                            },

                            body: JSON.stringify({
                                vehicle_id:
                                    vehicleId,
                                maintenance_type:
                                    maintenanceType,
                                date: date,
                                kilometers:
                                    kilometers,
                                cost: cost,
                                notes: notes
                            })
                        }
                    );

                const result =
                    await response.json();

                if (!response.ok) {

                    alert(
                        result.detail ||
                        "No se pudo añadir el mantenimiento."
                    );

                    return;
                }

                alert(
                    "Mantenimiento añadido correctamente."
                );

                closeMaintenanceForm();

                viewMaintenances(
                    vehicleId
                );

            } catch (error) {

                console.error(error);

                alert(
                    "Error al conectar con la API."
                );
            }
        }
    );


async function editMaintenance(
    maintenanceId,
    vehicleId
) {

    try {

        const response =
            await fetch(
                `${API_URL}/maintenances/${vehicleId}`
            );

        const maintenances =
            await response.json();

        if (!response.ok) {

            alert(
                maintenances.detail ||
                "No se pudieron obtener los mantenimientos."
            );

            return;
        }

        const maintenance =
            maintenances.find(
                item =>
                    item.id === maintenanceId
            );

        if (!maintenance) {

            alert(
                "El mantenimiento no existe."
            );

            return;
        }

        document.getElementById(
            "edit-maintenance-id"
        ).value =
            maintenance.id;

        document.getElementById(
            "edit-maintenance-vehicle-id"
        ).value =
            vehicleId;

        document.getElementById(
            "edit-maintenance-type"
        ).value =
            maintenance.maintenance_type;

        document.getElementById(
            "edit-maintenance-date"
        ).value =
            maintenance.date;

        document.getElementById(
            "edit-maintenance-kilometers"
        ).value =
            maintenance.kilometers;

        document.getElementById(
            "edit-maintenance-cost"
        ).value =
            maintenance.cost;

        document.getElementById(
            "edit-maintenance-notes"
        ).value =
            maintenance.notes || "";

        const section =
            document.getElementById(
                "edit-maintenance-form-section"
            );

        section.classList.remove("hidden");

        section.scrollIntoView({
            behavior: "smooth"
        });

    } catch (error) {

        console.error(error);

        alert(
            "Error al conectar con la API."
        );
    }
}


function closeEditMaintenanceForm() {

    const section =
        document.getElementById(
            "edit-maintenance-form-section"
        );

    const form =
        document.getElementById(
            "edit-maintenance-form"
        );

    form.reset();

    section.classList.add("hidden");
}


document
    .getElementById("edit-maintenance-form")
    .addEventListener(
        "submit",
        async function(event) {

            event.preventDefault();

            const maintenanceId =
                Number(
                    document.getElementById(
                        "edit-maintenance-id"
                    ).value
                );

            const vehicleId =
                Number(
                    document.getElementById(
                        "edit-maintenance-vehicle-id"
                    ).value
                );

            const maintenanceType =
                document.getElementById(
                    "edit-maintenance-type"
                ).value.trim();

            const date =
                document.getElementById(
                    "edit-maintenance-date"
                ).value.trim();

            const kilometers =
                Number(
                    document.getElementById(
                        "edit-maintenance-kilometers"
                    ).value
                );

            const cost =
                Number(
                    document.getElementById(
                        "edit-maintenance-cost"
                    ).value
                );

            const notes =
                document.getElementById(
                    "edit-maintenance-notes"
                ).value.trim();

            try {

                const response =
                    await fetch(
                        `${API_URL}/maintenances/${maintenanceId}`,
                        {
                            method: "PUT",

                            headers: {
                                "Content-Type":
                                    "application/json"
                            },

                            body: JSON.stringify({
                                vehicle_id:
                                    vehicleId,
                                maintenance_type:
                                    maintenanceType,
                                date: date,
                                kilometers:
                                    kilometers,
                                cost: cost,
                                notes: notes
                            })
                        }
                    );

                const result =
                    await response.json();

                if (!response.ok) {

                    alert(
                        result.detail ||
                        "No se pudo actualizar el mantenimiento."
                    );

                    return;
                }

                alert(
                    "Mantenimiento actualizado correctamente."
                );

                closeEditMaintenanceForm();

                viewMaintenances(
                    vehicleId
                );

            } catch (error) {

                console.error(error);

                alert(
                    "Error al conectar con la API."
                );
            }
        }
    );


async function deleteMaintenance(
    maintenanceId,
    vehicleId
) {

    const confirmed =
        confirm(
            "¿Seguro que quieres eliminar este mantenimiento?"
        );

    if (!confirmed) {
        return;
    }

    try {

        const response =
            await fetch(
                `${API_URL}/maintenances/${maintenanceId}`,
                {
                    method: "DELETE"
                }
            );

        if (!response.ok) {

            const error =
                await response.json();

            alert(
                error.detail ||
                "No se pudo eliminar el mantenimiento."
            );

            return;
        }

        alert(
            "Mantenimiento eliminado correctamente."
        );

        viewMaintenances(
            vehicleId
        );

    } catch (error) {

        console.error(error);

        alert(
            "Error al conectar con la API."
        );
    }
}


async function deleteVehicle(
    vehicleId
) {

    const confirmed =
        confirm(
            "¿Seguro que quieres eliminar este vehículo?"
        );

    if (!confirmed) {
        return;
    }

    try {

        const response =
            await fetch(
                `${API_URL}/vehicles/${vehicleId}`,
                {
                    method: "DELETE"
                }
            );

        if (!response.ok) {

            const error =
                await response.json();

            alert(
                error.detail ||
                "No se pudo eliminar el vehículo."
            );

            return;
        }

        alert(
            "Vehículo eliminado correctamente."
        );

        document
            .getElementById(
                "maintenances-section"
            )
            .classList.add("hidden");

        loadVehicles();

    } catch (error) {

        console.error(error);

        alert(
            "Error al conectar con la API."
        );
    }
}


function escapeHtml(value) {

    const div =
        document.createElement("div");

    div.textContent =
        value ?? "";

    return div.innerHTML;
}


loadVehicles();