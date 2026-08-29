FROM python:3.12-slim-bookworm

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        chromium \
        fonts-liberation \
        libasound2 \
        libatk-bridge2.0-0 \
        libdrm2 \
        libgbm1 \
        libnss3 \
        libxcomposite1 \
        libxdamage1 \
        libxrandr2 \
        xdg-utils && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install chromium && \
    playwright install-deps chromium

COPY . .

RUN ls -la /app/UI_TESTS/

RUN ls -la /app/API_TESTS/

RUN ls -la /app/HYBRID_TEST/

CMD ["pytest", "UI_TESTS/", "API_TESTS", "HYBRID_TEST", "-v", "--alluredir=allure-results", "--clean-alluredir"]