FROM python:3.12-slim AS builder

WORKDIR /build
COPY app/requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_NAME=devops-starter-app

WORKDIR /app
COPY --from=builder /install /usr/local
COPY app/ .

RUN useradd --create-home appuser
USER appuser

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]

