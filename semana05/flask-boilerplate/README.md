# Flask Migrate

## Instalación

```bash
pip install flask flask-sqlalchemy python-dotenv psycopg2-binary
pip install flask-migrate
```

## Uso

```bash
# Inicializa las migraciones
# Se ejecuta una sola vez
flask db init

# Genera los scripts de migraciones
flask db migrate -m "Create users table"

# Aplicar las migraciones generadas
flask db upgrade
```