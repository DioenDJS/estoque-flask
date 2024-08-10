FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt

ENV TZ=America/Sao_Paulo

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE ${API_PORT}

CMD ["python", "run.py"]
