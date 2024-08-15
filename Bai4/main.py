from appium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

desired_cap = {"deviceName": "emulator-5554",
               "udid": "emulator-5554",
               "platformName": "Android",
               "newCommandTimeout": 600,
               "systemPort": 8000}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)

