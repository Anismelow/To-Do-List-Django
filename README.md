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
Docker
Configuración
Clona este repositorio en tu máquina local.
Navega hasta el directorio del proyecto.
Docker
Asegúrate de tener Docker instalado en tu máquina.

Construye y ejecuta los contenedores Docker con el siguiente comando en el directorio del proyecto:

bash
Copy code
docker-compose up --build
Abre tu navegador web y visita http://localhost:8000.

## Rutas

- `/registro/`: Ruta para registrar nuevos usuarios.
- `/login/`: Ruta para iniciar sesión.
- `/home/`: Ruta para acceder a la página principal una vez iniciada la sesión.
- `/completar_tarea/<int:task_id>/`: Ruta para marcar una tarea como completada. El parámetro `<int:task_id>` corresponde al ID de la tarea.
- `/borrar_tarea/<int:task_id>/`: Ruta para eliminar una tarea. El parámetro `<int:task_id>` corresponde al ID de la tarea.


Regístrate como nuevo usuario o inicia sesión si ya tienes una cuenta.

Una vez iniciado sesión, podrás crear nuevas tareas, editarlas o eliminarlas.

Las tareas solo serán visibles para el usuario que las creó.