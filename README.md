# Gestor_de_tareas
## Table of Contents
$git remote add origin https://github.com/Sebas0529/Gestor_de_tareas.git
$git pull origin main 
$pip install virtualenv 
$virtualenv -p python env 
$source env/bin/activate
$pip install requirements
$python manage.py runserver 

### crear en postman la collection de Gestor_de_tareas
***
agregar las siguientes request

## POST
***
login --> http://127.0.0.1:8000/login-register/login/
{
    "email" : "sebas@gmail.com",
    "password" : "12345678"
}
create_user --> http://127.0.0.1:8000/login-register/create/
{
    "username" : "david",
    "email" : "david@gmail.com",
    "first_name": "",
    "last_name" : "",
    "password" : "12345678"
}

create_task --> http://127.0.0.1:8000/tasks/create_task/
{
    "name" : "nombre tarea",
    "description" : "descripcion tarea",
    "assigned_to" : "llave foranea del usuario encargado"
}
## GET
***
list_users --> http://127.0.0.1:8000/login-register/list/
list_task --> http://127.0.0.1:8000/tasks/list_task/
filter_status --> http://127.0.0.1:8000/tasks/filter_status_task/?status=to_do
```
$ git clone https://example.com
$ cd ../path/to/the/file
$ npm install
$ npm start
### PUT
***
update_task --> http://127.0.0.1:8000/tasks/update_task/
{
    "name" : "nombre tarea",
    "assigned_to" : "llave foranea del usuario encargado",
    "status" : "done"
}
## DELETE
***
delete_task --> http://127.0.0.1:8000/tasks/delete_task/
delete_user --> http://127.0.0.1:8000/login_register/delete_user/
