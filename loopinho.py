from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Welcome - Loopizinho #


def clear():
    try:
        import os
        lines = os.get_terminal_size().lines
    except AttributeError:
        lines = 130
    print("\n" * lines)


def AcessGoogle(driver):
    driver.get('https://www.google.com')
    time.sleep(3)


def AcessAzure(driver):
    driver.get('https://azure.microsoft.com/')
    time.sleep(3)


def GoToSearch(driver):
    inputButon = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    inputButon.send_keys("consumir api soap c#" + Keys.ENTER)
    time.sleep(5)


# Let's Code #
while (True):
    driver = webdriver.Edge('.\edgedriver_win64\msedgedriver.exe')
    AcessGoogle(driver)
    GoToSearch(driver)
    driver.back()
    time.sleep(2)
    driver.close()
    time.sleep(3)
    driver = webdriver.Edge('.\edgedriver_win64\msedgedriver.exe')
    AcessAzure(driver)
    time.sleep(5)
    clear()
    driver.close()
