# Minimal Dockerfile for demo
FROM python:3.11-slim
WORKDIR /app
COPY . /app
CMD ["python3","main.py","encode","hello"]
