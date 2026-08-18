import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL")
    PAGE_LOAD_TIMEOUT = 30000
    TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD") # docker run --rm -e BASE_URL="https://automationexercise.com" -e TEST_USER_PASSWORD="any password" allure-tests