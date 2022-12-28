#DEV: docker run -dp 5000:5005 -w /app -v "C:\Users\josel\Documents\Personal\FlaskApp:/app" flask-smorest-api
#PROD: docker run -dp 5000:5005 flask-smorest-api
FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]