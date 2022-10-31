<br />


# Car Service Administrador

Sistema de gestion para administrar ,personas,clientes,modulos ,planes y sus correspondientes bases de datos. 

<br />

> 🚀 Para su correcto funcionamiento se describiran sus dependencias como archivos externos.

<br />



## ✨ Instalaciones de dependencias

> **Step 1** - Instalacion de requirements 

```bash
pip install -r requirements.txt 
```
<br />

> **Step 2** - Instalacion del componente de formularios 

```bash
pip install django-crispy-forms 
```
<br />


> **Step 3** - Instalacion de conector MYSQL 

```bash
 pip install mysqlclient    
```
<br />

<br />

## ✨ Migracion de Base de Datos

> migrate

```bash
python manage.py migrate 
```



<br />

<br />

## ✨ Iniciar el servicio

> manage.py

```bash
python manage.py runserver
```

<br />


<br />

## ✨Crear el super usuario

> usuario con privilegios

```bash
python manage.py createsuperuser
```

<br />


<br />

## ✨Crear Grupos

> desde la admininistracion DJANGO Crear dos Grupos que corresponderan a 'administradores' y 'vendedores'
> Agregarles los permisos segun correspondan (vendedores solo veran facturacion y personas ,can view persons ,can view clientes)


<br />


<br />

<br />

### 👉 migracion de  `Datos` 

> En la siguinte ruta tenemos ciudades y provincias de ejemplo formato *.csv , se debera importar en la base de datos por default 

```
-> Provincias
->archivo-> provincias_id.csv en la tabla  service_provinces

-> Ciudades
->archivo-> ciudades.csv en la tabla  service_cities
```
- Repositorio [Drive](https://drive.google.com/drive/folders/1YO9oXgAVypCAEra9-MQqAoqETt1q4HyG?usp=sharing)
<br />

> Migracion de nuevos permisos

```bash
-> archivo -> auth_content.csv en la tabla django_content_type
-> archivo -> auth_permission.csv en la tabla auth_permission;

```
- Repositorio [Drive](https://drive.google.com/drive/folders/1YO9oXgAVypCAEra9-MQqAoqETt1q4HyG?usp=sharing)
<br />


>Importar la Base de datos TEMPLATE

```bash
Crear un nuevo esquema con el nombre  `template` , e importar el archivo *sql del repositorio 
```
- Repositorio [Drive](https://drive.google.com/drive/folders/1YO9oXgAVypCAEra9-MQqAoqETt1q4HyG?usp=sharing)
<br />

<br />



<br />

---


