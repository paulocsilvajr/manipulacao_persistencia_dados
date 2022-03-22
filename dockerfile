FROM ubuntu
WORKDIR /code/
COPY ./src/requirements.txt /code/
RUN apt update && apt install -y python3-dev libpq-dev python3-pip
RUN pip install --no-cache-dir -r requirements.txt

