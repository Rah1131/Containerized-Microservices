FROM python:3.13-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 8082
CMD ["python", "app.py"]
