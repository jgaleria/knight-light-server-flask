FROM python:3.10.5-alpine3.16

COPY requirements.txt requirements.txt

WORKDIR /app
COPY . /app/

EXPOSE 5000

RUN pip install -r requirements.txt
CMD ["python3", "-m", "flask", "run", "--host", "0.0.0.0"]

