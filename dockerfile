FROM python:3.9-alpine
WORKDIR /app
COPY python_script.py .
CMD ["python", "python_script.py", "example"]