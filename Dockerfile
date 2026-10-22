# 1. Берем готовый образ от Microsoft, где уже зашиты Python, Playwright и все зависимости
FROM ://microsoft.com

# 2. Указываем рабочую директорию
WORKDIR /app

# 3. Устанавливаем зависимости из requirements.txt (pytest, allure и т.д.)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Копируем проект в контейнер
COPY . .

# 5. Запускаем тесты
CMD ["pytest", "UI_TESTS/", "API_TESTS", "HYBRID_TEST", "-v", "--alluredir=allure-results", "--clean-alluredir"]
