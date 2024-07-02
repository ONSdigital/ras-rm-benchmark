# Dockerfile specifically for kubernetes
FROM python:3.11-slim

RUN pip install pipenv

COPY . .

RUN pipenv install
CMD ["./process-results.sh"]

