# 🧠 PokedexIA

Una **Pokédex full-stack** creada con Python, HTML/CSS y JavaScript, que permite explorar datos de Pokémon desde una base de datos local.  
Este proyecto incluye backend, frontend, base de datos y soporte para Docker 🐳.

---

## 🚀 Descripción

PokedexIA es una aplicación web que muestra información de Pokémon de forma interactiva.  
Cuenta con una **API backend en Python** que sirve datos desde una base de datos SQLite y un **frontend moderno** que consume esa API para mostrar los detalles de cada Pokémon en la UI.

---

## 🧱 Estructura del proyecto

PokedexIA/
├── backend/ # Código Python para servir la API
├── frontend/ # UI (HTML, CSS, JS)
├── .gitignore
├── Dockerfile # Para construir y ejecutar con Docker
├── README.md
├── esquema.sql # Esquema de la base de datos SQLite
├── requirements.txt # Dependencias de Python


## 🧠 Tecnologías utilizadas

- 🐍 **Python** para el backend
- 🗄️ **SQLite** como base de datos (`pokedex.db`)
- 🌐 **HTML, CSS, JavaScript** para el frontend
- 🐳 **Docker** para contenerizar la aplicación
- 📦 Librerías listadas en `requirements.txt` :contentReference[oaicite:1]{index=1}

---

## 💻 Instalación y ejecución local

### 1️⃣ Clonar el repositorio

git clone https://github.com/davidlajas/PokedexIA.git
cd PokedexIA
2️⃣ Crear entorno virtual e instalar dependencias
bash
Copiar código
python3 -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

pip install -r requirements.txt
3️⃣ Ejecutar el backend
bash
Copiar código
cd backend
python app.py    # o el script principal de tu API
Asegúrate de que la ruta de pokedex.db coincida con la configuración de tu servidor.

4️⃣ Abrir el frontend
Abre frontend/index.html en tu navegador o sirve el frontend desde un servidor estático (por ejemplo con Live Server).

🐳 Uso con Docker (opcional)
Si tienes Docker instalado:

bash
Copiar código
docker build -t pokedexia .
docker run -p 5000:5000 pokedexia
Accede luego a http://localhost:5000 en tu navegador.

📦 Contenido de la Base de Datos
La base de datos pokedex.db contiene tablas con información de Pokémon, que probablemente cubran:

Nombre

Tipos

Estadísticas (ataque, defensa, etc.)

Habilidades

Otra metadata relevante

Puedes ver la estructura de la base de datos en el archivo esquema.sql. 
GitHub

📝 Uso
Una vez todo funcionando:

Visita la UI desde tu navegador.

Usa la interfaz para buscar y ver Pokémon por nombre o ID.

Interactúa con la API desde el frontend para mostrar información detallada.

🛠️ Posibles mejoras
✨ Agregar autenticación
✨ Paginación y búsqueda avanzada
✨ Integración con PokéAPI si falta información
✨ Tests automatizados
✨ Mejora de UI/UX


📌 Autor
davidlajas (creador del proyecto)

¡Gracias por revisar PokedexIA! 🐾
Explora Pokémon con estilo 🚀
