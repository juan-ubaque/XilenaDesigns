PASOS PARA CREAR DE MANERA CORRECTA UN ENTORNO VIRTUAL EN PYTHON

1. Instalar virtualenv con el comando: python -m venv nombre_del_entorno

se recomienda crear el entorno con el nombre venv

2. Activar el entorno virtual con el comando: nombre_del_entorno\Scripts\activate

o para linux: source nombre_del_entorno/bin/activate

3. Instalar las librerias necesarias para el proyecto con el comando: pip install -r requirements.txt

ejecutar el comando pip install requirements.txt que es el archico .txt que contiene las librerias necesarias para el proyecto

revisar que se instalaron correctamente las librerias con el comando: pip freeze

ejecutar los comandos para arrancar el proyecto: python manage.py runserver
