FROM python:3.10.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . app

EXPOSE 5000

ENTRYPOINT ["python","-u", "./app/app.py"]