FROM python:3.10.3-buster
WORKDIR /code/
COPY ./src/requirements.txt /code/
RUN apt update && apt install -y python3-dev libpq-dev
RUN pip install --no-cache-dir -r requirements.txt

