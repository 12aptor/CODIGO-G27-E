# 🏷️ Introducción a las Clases en Python

Las clases en Python permiten implementar el **paradigma de Programación Orientada a Objetos (POO)**. Con ellas puedes crear tus propios tipos de datos, encapsular atributos y comportamientos, y organizar código de forma modular y reutilizable.

---

## 🔶 Definir una clase

Usamos la palabra clave `class`:

```python
class Persona:
    pass  # Clase vacía
```

---

## 📦 Constructor `__init__`

Se ejecuta al crear una instancia. Sirve para inicializar atributos:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre   # Atributo de instancia
        self.edad = edad

# Crear objeto
p = Persona("Ana", 30)
```

---

## 🔸 Atributos y métodos

- **Atributos**: variables asociadas a la clase o instancia.
- **Métodos**: funciones definidas dentro de la clase.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

p = Persona("Ana", 30)
p.saludar()  # Hola, soy Ana y tengo 30 años.
```

---

## 💡 Métodos de clase y estáticos

### Método de clase (`@classmethod`)

Recibe `cls` en lugar de `self`:

```python
class Circulo:
    pi = 3.1416

    def __init__(self, radio):
        self.radio = radio

    @classmethod
    def info_pi(cls):
        print(f"Valor de pi: {cls.pi}")

Circulo.info_pi()  # Valor de pi: 3.1416
```

### Método estático (`@staticmethod`)

No recibe `self` ni `cls`:

```python
class Matematica:
    @staticmethod
    def sumar(a, b):
        return a + b

print(Matematica.sumar(3, 4))  # 7
```

---

## 🌱 Herencia

Permite crear clases derivadas que heredan atributos y métodos:

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice ¡Guau!")

perro = Perro("Rex")
perro.hablar()  # Rex dice ¡Guau!
```

---

## 🔐 Encapsulación

Convención de atributos “privados” con guion bajo:

```python
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo protegido

    def mostrar_saldo(self):
        print(f"Saldo: {self._saldo}")
```

---

## ✨ Métodos mágicos

Permiten personalizar comportamiento:

- `__str__`: representación legible
- `__repr__`: representación sin ambigüedades
- `__add__`, `__len__`, etc.

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punto({self.x}, {self.y})"

    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

p1 = Punto(1, 2)
p2 = Punto(3, 4)
print(p1)           # Punto(1, 2)
print(p1 + p2)     # Punto(4, 6)
```

---

## 🧪 Ejercicios

1. **Gestión de contactos**: crea una clase `Contacto` con atributos `nombre` y `teléfono`, y método `mostrar()`.  
2. **Cuenta de ahorro**: crea `Cuenta` con atributos `titular` y `saldo`. Implementa métodos `depositar(monto)` y `retirar(monto)`.  
3. **Inventario**: crea clase `Producto` con `nombre`, `cantidad` y `precio`. Añade método `valor_total()` que devuelva `cantidad * precio`.  
4. **Jerarquía de vehículos**: crea clase base `Vehiculo` y clases derivadas `Coche` y `Moto`, definiendo un método `desplazarse()`.  

---

## ✅ Conclusión

Las clases son la base de la POO en Python. Te permiten modelar conceptos del mundo real en tu código, facilitando organización, legibilidad y reutilización.