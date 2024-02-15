# Guardar un texto con todos los paquetes instalados y sus versiones
pip freeze > requirements.txt

# Instalar todos los paquetes y versiones desde el listado
pip install -r .\requirements.txt

# Crear entorno de django 
django-admin startproject reservation

# Instalar base de datos mysql

# Definir base de datos 
DATABASES = {
    'default':{
        'ENGINE': 'django.bd.backends.mysql',
        'NAME': 'mybd',
        'USER': '',
        'ENGINE': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Iniciar 
code .
