import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    chrome_options = Options()

    # REQUIRED for GitHub Actions / CI
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service()  # Selenium Manager (no webdriver-manager needed)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver
    driver.quit()
