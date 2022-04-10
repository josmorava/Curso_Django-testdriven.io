#imagen base
FROM python:3.10.1-slim-buster

#directorio de trabajo
WORKDIR /usr/src/app

#Variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Instalando las dependencias del sistema
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

#Instalando las dependencias
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#Copiando el entryponit.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Proyecto
COPY . .

#Corriendo el entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
