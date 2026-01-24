# Testing con Pytest

## Instalación

```bash
pip install pytest pytest-django pytest-cov
```

## Configuración `pytest.ini`

```bash
[pytest]
DJANGO_SETTINGS_MODULE=django_barbershop.settings
python_files=tests.py test_*.py *_tests.py
filterwarnings=ignore::DeprecationWarning
```

## Ejecución

```bash
pytest
```