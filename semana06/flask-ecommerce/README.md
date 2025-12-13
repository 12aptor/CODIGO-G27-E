# Flask Ecommerce

## Configuración

### Instalación de dependencias
```bash
pip install -r requirements.txt
```

### Base de datos y migraciones

```bash
flask db init
flask db migrate
flask db upgrade
```

### Variables de entorno

```bash
DATABASE_URI=''
SECRET_KEY=''
FERNET_SECRET_KEY=''
CLOUDINARY_API_KEY=''
CLOUDINARY_CLOUD_NAME=''
CLOUDINARY_API_SECRET=''
```

### Iniciar el servidor

```bash
python run.py
```