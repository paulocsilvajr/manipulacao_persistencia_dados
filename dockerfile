FROM python:3.10.3-buster
WORKDIR /code/
COPY ./src/requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/

