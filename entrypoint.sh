#!/bin/bash

# Останавливаем выполнение при ошибке
set -e

echo "🚀 Applying database migrations..."
alembic upgrade head

echo "✅ Starting FastAPI server..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
