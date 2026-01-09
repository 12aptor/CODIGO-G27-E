# Django Intro

### Entorno virtual

```bash
python -m venv venv
venv\Scripts\activate # Windows
source venv/Scripts/activate # Gitbash
source venv/bin/activate # MacOS/Linux
```

### Instalación

```bash
pip install django
```

### Crear proyecto

```bash
django-admin startproject django_intro .
```

### Iniciar el proyecto

```bash
python manage.py runserver
```

### Migraciones

```bash
# Generar los documentos de migraciones
python manage.py makemigrations

# Ejecutar las migraciones
python manage.py migrate

# Ver el estado de los documentos de migraciones
python manage.py showmigrations
```

### Crear superusuario

```bash
python manage.py createsuperuser
```

### Crear aplicación

```bash
python manage.py startapp almacen
```