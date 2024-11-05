FROM python:3.13-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 8081
CMD ["python", "app.py"]
