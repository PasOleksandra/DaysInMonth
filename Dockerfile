
FROM python:3.12-alpine


WORKDIR /app


COPY . .


CMD ["python", "eks.py"]
