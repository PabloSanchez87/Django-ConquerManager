# Creamos el entorno virtual
    python3 -m venv vDjango

# Activamos el entorno virtual
    source vDjango/bin/activate

# Creación del proyecto
    django-admin startproject conquermanager .

# Instalamos las dependencias
    pip3 install -r requirements.txt

# Arrancar el servidor.
    python3 manage.py runserver

    - Starting development server at http://127.0.0.1:8000/

# Crear aplicacion
    python3 manage.py startapp todos