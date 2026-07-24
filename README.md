# 🚗 AutoCare

AutoCare es una aplicación de consola desarrollada en **Python** para gestionar vehículos y su historial de mantenimientos. Permite registrar vehículos, controlar revisiones y consultar el estado de los mantenimientos más importantes para facilitar el seguimiento del mantenimiento del automóvil.

---

# 📋 Funcionalidades

## 🚘 Gestión de vehículos

- Registrar vehículos.
- Ver todos los vehículos registrados.
- Editar la información de un vehículo.
- Eliminar vehículos.
- Buscar vehículos por matrícula.

---

## 🔧 Gestión de mantenimientos

- Registrar mantenimientos.
- Consultar el historial de mantenimientos de un vehículo.
- Editar mantenimientos.
- Eliminar mantenimientos.

Los tipos de mantenimiento disponibles son:

- Cambio de aceite
- ITV
- Frenos
- Neumáticos
- Batería
- Filtros
- Otro

---

## 📊 Estadísticas

La aplicación permite consultar:

- Estadísticas generales.
- Estadísticas individuales de cada vehículo.

---

## ⚠️ Recordatorios automáticos

AutoCare calcula automáticamente el estado de distintos mantenimientos:

- Cambio de aceite.
- ITV.
- Frenos.
- Neumáticos.
- Batería.
- Filtros.

Los avisos tienen en cuenta los kilómetros recorridos y/o el tiempo transcurrido desde el último mantenimiento registrado.

---

# ✅ Validaciones

La aplicación incorpora diferentes validaciones para garantizar la integridad de los datos:

- Matrículas con formato español (1234ABC).
- Año del vehículo válido.
- Kilómetros no negativos.
- Fechas válidas y no posteriores a la fecha actual.
- Costes no negativos.
- Matrículas duplicadas.
- Los kilómetros de un mantenimiento no pueden superar los kilómetros actuales del vehículo.

---

# 🛠️ Tecnologías utilizadas

- Python 3
- SQLite
- Git
- GitHub

---

# 📁 Estructura del proyecto

```text
Autocare/
│
├── app.py
├── database.py
├── validators.py
├── constants.py
├── database.db
├── README.md
└── .gitignore
```

---

# ▶️ Instalación

Clona el repositorio:

```bash
git clone https://github.com/Aurelioortega7/Autocare.git
```

Accede al directorio del proyecto:

```bash
cd Autocare
```

Ejecuta la aplicación:

```bash
python app.py
```

---

# 💻 Menú principal

```
===== AutoCare =====

1. Registrar vehículo
2. Ver vehículos
3. Editar vehículo
4. Eliminar vehículo

5. Registrar mantenimiento
6. Ver historial de mantenimientos
7. Editar mantenimiento
8. Eliminar mantenimiento

9. Estadísticas generales
10. Estadísticas de un vehículo
11. Buscar vehículo por matrícula

12. Estado cambio de aceite
13. Estado ITV
14. Estado frenos
15. Estado neumáticos
16. Estado batería
17. Estado filtros

18. Salir
```

---

# 🚀 Mejoras futuras

- Interfaz gráfica.
- Aplicación Android.
- Aplicación web.
- Exportación de datos a PDF o Excel.
- Copias de seguridad automáticas.
- Gestión de usuarios.
- Notificaciones de mantenimientos.

---

# 👤 Autor

**Aurelio Ortega**

Proyecto desarrollado como práctica de programación en Python aplicando conceptos de:

- Programación modular.
- Persistencia de datos con SQLite.
- Validación de datos.
- Gestión mediante CRUD.
- Uso de Git y GitHub.