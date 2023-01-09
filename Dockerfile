#DEV: docker run -dp 5000:5005 -w /app -v "C:\Users\josel\Documents\Personal\FlaskApp:/app" flask-smorest-api
#PROD: docker run -dp 5000:5005 flask-smorest-api
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:creat_app()"]