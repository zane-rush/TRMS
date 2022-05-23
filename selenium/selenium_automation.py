from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By

serv = Service(
    "C:/Users/zcrus/Desktop/geckodriver.exe")
driver: WebDriver = webdriver.Firefox(sevice=serv)