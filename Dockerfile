FROM python:3.10.5-alpine3.16

WORKDIR /app
COPY . /app/

EXPOSE 5000

RUN pip install flask
CMD ["python3", "-m", "flask", "run", "--host", "0.0.0.0"]

