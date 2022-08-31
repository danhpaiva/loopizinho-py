import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Welcome - Loopizinho @danhpaiva #


def clear():
    try:
        import os
        lines = os.get_terminal_size().lines
    except AttributeError:
        lines = 130
    print("\n" * lines)


def AcessGoogle(driver):
    driver.get('https://www.google.com')
    time.sleep(10)


def AcessAzure(driver):
    driver.get('https://docs.microsoft.com/pt-br/dotnet/azure/')
    time.sleep(10)


def GoToSearch(driver):
    inputButon = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    inputButon.send_keys("consumir api soap c#" + Keys.ENTER)
    time.sleep(10)


def RandomClick(driver):
    number = random.randint(1, 4)
    search = ''
    if (number == 1):
        search = 'performance net 7'
    elif (number == 2):
        search = 'kubernetes e docker com csharp'
    elif (number == 3):
        search = 'designe pattern c# guru'
    else:
        search = 'visual studio release notes'
    inputButon = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    inputButon.send_keys(search + Keys.ENTER)
    time.sleep(10)


# Let's Code #
pathSystem = '.\edgedriver_win64\msedgedriver.exe'
while (True):
    driver = webdriver.Edge(pathSystem)
    time.sleep(2)
    AcessGoogle(driver)
    randomNumber = random.randint(1, 4)
    if ((randomNumber % 2) == 0):
        GoToSearch(driver)
    else:
        RandomClick(driver)
    driver.back()
    time.sleep(5)
    driver.close()
    time.sleep(5)
    driver = webdriver.Edge(pathSystem)
    time.sleep(2)
    AcessAzure(driver)
    clear()
    driver.close()
    time.sleep(5)
