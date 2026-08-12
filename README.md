# 🚗 AutoCare

AutoCare es una aplicación para la gestión de vehículos y sus mantenimientos.

El proyecto comenzó como una aplicación de consola desarrollada en Python y ha evolucionado hasta incorporar una aplicación web con frontend y API REST desarrollada con FastAPI.

---

# ✨ Funcionalidades

## 🚗 Gestión de vehículos

- Registrar vehículos.
- Consultar vehículos registrados.
- Editar vehículos.
- Eliminar vehículos.
- Mostrar marca, modelo, año, matrícula y kilómetros.

## 🔧 Gestión de mantenimientos

- Añadir mantenimientos a cada vehículo.
- Consultar el historial de mantenimientos.
- Editar mantenimientos.
- Eliminar mantenimientos.
- Registrar tipo de mantenimiento, fecha, kilómetros, coste y notas.

## 📊 Estadísticas

Cada vehículo dispone de estadísticas de mantenimiento:

- Gasto total.
- Gasto del año actual.
- Media mensual del año actual.
- Número de mantenimientos.

---

# 🌐 Aplicación web

La aplicación web está formada por:

- Frontend desarrollado con HTML, CSS y JavaScript.
- API REST desarrollada con FastAPI.
- Base de datos SQLite.

La interfaz permite gestionar los vehículos y mantenimientos desde el navegador.

La aplicación permite consultar los mantenimientos asociados a cada vehículo y visualizar sus estadísticas de gasto.

---

# 🛠️ Tecnologías utilizadas

- Python
- FastAPI
- SQLite
- HTML5
- CSS3
- JavaScript
- Uvicorn
- Pydantic
- Git
- GitHub

---

▶️ Instalación

Clona el repositorio:

git clone https://github.com/Aurelioortega7/Autocare.git

Accede al directorio del proyecto:

cd Autocare

Crea el entorno virtual:

python -m venv .venv

Activa el entorno virtual en Windows:

.venv\Scripts\activate

Instala las dependencias:

pip install -r requirements.txt

---

🚀 Ejecutar la API

Desde la carpeta principal del proyecto ejecuta:

uvicorn main:app --reload

La API estará disponible en:

http://127.0.0.1:8000

La documentación interactiva de FastAPI estará disponible en:

http://127.0.0.1:8000/docs

---

💻 Ejecutar la aplicación web

La aplicación web se encuentra dentro de la carpeta:

frontend/

Para utilizarla en local puedes abrir index.html mediante un servidor local, por ejemplo utilizando Live Server desde Visual Studio Code.

La API debe estar ejecutándose al mismo tiempo para que la aplicación web pueda consultar y modificar los datos.

---

🗄️ Base de datos

AutoCare utiliza SQLite como sistema de almacenamiento.

Actualmente la base de datos contiene información sobre:

Vehículos.
Mantenimientos.
Relación entre vehículos y sus mantenimientos.

Las tablas se crean automáticamente mediante el sistema de inicialización de la base de datos.

---

📊 Estadísticas de mantenimiento

AutoCare permite consultar diferentes estadísticas para cada vehículo.

Gasto total

Muestra el coste acumulado de todos los mantenimientos registrados para el vehículo.

Gasto del año actual

Muestra únicamente el gasto correspondiente al año actual.

Media mensual

Calcula la media mensual del gasto correspondiente al año actual.

Número de mantenimientos

Muestra la cantidad total de mantenimientos registrados para el vehículo.

---

🔄 Evolución del proyecto

AutoCare comenzó como una aplicación de consola desarrollada en Python.

La versión inicial permitía gestionar vehículos, mantenimientos, estadísticas y diferentes estados de mantenimiento.

Posteriormente el proyecto evolucionó hacia una arquitectura basada en una API REST y una aplicación web.

La versión actual se centra en la gestión de vehículos, mantenimientos y estadísticas mediante una interfaz web.

---

🚀 Mejoras futuras

Algunas de las mejoras previstas para futuras versiones son:

Aplicación móvil.
Notificaciones de mantenimiento.
Recordatorios de cambio de aceite.
Recordatorios de ITV.
Recordatorios de neumáticos.
Recordatorios de frenos.
Recordatorios de batería.
Recordatorios de filtros.
Avisos basados en kilómetros.
Avisos basados en fechas.
Exportación de datos a PDF o Excel.
Copias de seguridad automáticas.
Gestión de usuarios.
Sincronización entre dispositivos.
Estadísticas más avanzadas.

---

👤 Autor

Aurelio Ortega

Proyecto personal de programación y evolución progresiva de una aplicación de gestión de vehículos.

Conceptos y tecnologías utilizados:

Programación modular.
Desarrollo de API REST.
FastAPI.
Persistencia de datos con SQLite.
Validación de datos.
Operaciones CRUD.
HTML.
CSS.
JavaScript.
Git.
GitHub.

---

