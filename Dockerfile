FROM python:3.12-slim-bookworm

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl gnupg && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

ENV PLAYWRIGHT_BROWSERS_PATH=/opt/allure-browsers

RUN playwright install chromium && \
    playwright install-deps chromium && \
    chmod -R 755 /opt/allure-browsers # Даем права на чтение/запуск всем пользователям

RUN useradd -m -u 1001 testuser && \
    mkdir -p /app/allure-results && \
    chown -R testuser:testuser /app

USER testuser

COPY --chown=testuser:testuser . .

ENV QT_QPA_PLATFORM=offscreen

CMD ["pytest", "UI_TESTS/", "API_TESTS/", "-v", "--alluredir=allure-results"]
