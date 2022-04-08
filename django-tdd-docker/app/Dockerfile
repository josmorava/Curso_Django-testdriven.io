#imagen base
FROM python:3.10.1-slim-buster

#directorio de trabajo
WORKDIR /usr/src/app

#Variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Instalando las dependencias
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Proyecto
COPY . .
