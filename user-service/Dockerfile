FROM python:3.13-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 8080
CMD ["python", "app.py"]
