FROM python:3-alpine

COPY server /app/server
COPY credentials.json /app/credentials.json
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

CMD [ "gunicorn", "--config", "server/gunicorn_config.py", "server.app:create_app()" ]