FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 80

CMD ["uvicorn", "app:app", "--host", "0.0.0.0". "--port", "80"]
