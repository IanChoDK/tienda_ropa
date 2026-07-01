# Tienda_ropa - Proyecto Django

Este es un proyecto de una tienda de ropa desarrollado con el framework **Django**.

## Miembros del grupo

* **Chena Martin** 
* **Ibañez Ian** 
* **Pereyra Franco** 
  
## Instalación y Configuración (Entorno Local)

Sigue estos pasos para ejecutar el proyecto en tu máquina local.

### 1. Requisitos previos
Asegúrate de tener instalado [Python](https://www.python.org/) (versión 3.8 o superior) y `pip` en tu sistema.

### 2. Clonar el repositorio
Abre tu terminal y clona este repositorio:

```bash
git clone git@github.com:IanChoDK/tienda_ropa.git
```

### 3. Crear y activar el entorno virtual (Recomendado)
Para mantener las dependencias aisladas, crea un entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

**4. Instalar las dependencias**

Con el entorno virtual activado, instala los paquetes necesarios:

```bash
pip install -r requirements.txt
```

**5. Configurar la Base de Datos (Migraciones)**

Ejecuta las migraciones para crear las tablas en la base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```


**6. Crear un Superusuario (Opcional pero recomendado)**

Para poder acceder al panel de administración de Django (/admin), crea un usuario administrador:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones en consola para establecer un nombre de usuario, email y contraseña.

**7. Levantar el servidor de desarrollo**

Finalmente, corre el servidor:

```bash
python manage.py runserver
```

El proyecto estará disponible en tu navegador ingresando a: http://127.0.0.1:8000/


## Proyecto en funcionamiento:

**HOME**
![home](https://github.com/IanChoDK/tienda_ropa/blob/5132d2380687e307effe8284f24d5b8755738dd0/media/ropa_images/home.png)
**CREAR PRODUCTO**
![crear](https://github.com/IanChoDK/tienda_ropa/blob/5132d2380687e307effe8284f24d5b8755738dd0/media/ropa_images/crear-producto.png)
**ADMIN PRODUCTO**
![admin-prendas](https://github.com/IanChoDK/tienda_ropa/blob/5132d2380687e307effe8284f24d5b8755738dd0/media/ropa_images/admin-prendas.png)
**PRODUCTOS**
![productos](https://github.com/IanChoDK/tienda_ropa/blob/5132d2380687e307effe8284f24d5b8755738dd0/media/ropa_images/productos.png)
**SUBIR-ROPA**
![subir-ropa](https://github.com/IanChoDK/tienda_ropa/blob/5132d2380687e307effe8284f24d5b8755738dd0/media/ropa_images/subiropa.png)
