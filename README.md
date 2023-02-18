# key_storechallenge backend

Se desarrollo la api de acuerdo al challenge de Pabex.

El framework de desarrollo fue Django Rest Framework y la version de python 3.10

Para probarlo se debe:
- Configurar el entorno virtual.
- Instalar los requerimientos. `$ pip install -r requirements.txt`
- Configurar un .env con los valores de variables de entorno a la altura de settings.py o exportarlas.
    Estas son: EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD. (ADVERTENCIA de seguridad) generar clave de app si se usa gmail para no exponer la clave original.
- Ejecutar las migraciones con makemigrations y migrate. `$ python manage.py makemigrations` y `$ python manage.py migrate`
- Por ultimo ejecutar el servidor de desarrollo. `$ python manage.py runserver`

# key_storechallenge frontend

El front fue desarrollado con angular 15
El repositorio esta disponible en el siguiente link: https://github.com/Juerodriguez/key_storage_frontend

