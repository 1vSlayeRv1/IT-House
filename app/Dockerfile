FROM python:3.9.4
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /urs/src/app
RUN pip install --upgrade pip
RUN apt install libpq-dev
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .