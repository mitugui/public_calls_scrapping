FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl

COPY requirements.txt .

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "main.py"]
