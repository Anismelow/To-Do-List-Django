To-Do List con Django

Este proyecto es un simple To-Do list desarrollado utilizando Django, un framework de desarrollo web en Python. Permite a los usuarios registrados crear y gestionar sus tareas personales de manera segura.
Características

    Registro de usuarios utilizando la tabla interna de usuarios de Django.
    Inicio de sesión seguro para acceder a las tareas personales.
    Cada usuario puede crear, editar y eliminar sus propias tareas.
    Las tareas son privadas y solo son visibles para el usuario que las creó.

Requisitos

    Python 3.x
    Django
    Instalar los requisitos del archivo requirements.txt mediante el comando pip install -r requirements.txt.

Configuración

    Clona este repositorio en tu máquina local.
    Navega hasta el directorio del proyecto.
    Crea un entorno virtual para el proyecto:

    bash

python -m venv venv

Activa el entorno virtual:

    En Windows:

    bash

myenv\Scripts\activate

En macOS/Linux:

bash

    source myenv/bin/activate

Instala las dependencias del proyecto:

bash

pip install -r requirements.txt

Realiza las migraciones de la base de datos:

bash

    python manage.py migrate

Uso

    Inicia el servidor de desarrollo:

    bash

python manage.py runserver

Abre tu navegador web y visita http://localhost:8000.
Regístrate como nuevo usuario o inicia sesión si ya tienes una cuenta.
Una vez iniciado sesión, podrás crear nuevas tareas, editarlas o eliminarlas.
Las tareas solo serán visibles para el usuario que las creó.
