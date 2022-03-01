import pickle
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import tools
#datetime, requests, colorama, selenium

def cookieCheck(driver, email, verbose):
    if verbose == True: print(tools.log() + "Checking for previous session...")
    try:
        loadCookies(driver, email, verbose)
        if verbose == True: print(tools.log() + "Cookies loaded...")
        driver.get("https://gmail.com")
        if verbose == True: print(tools.log() + "URL cookie check (inbox is good): " + driver.current_url)
        if "about" in driver.current_url:
            return False
        else:
            return True
    except FileNotFoundError as err:
        if verbose == True: print(tools.log() + "No previous session found.")
        return False

def saveCookies(driver, file, verbose):
    if verbose == True: print(tools.log() + "Saving cookie set 1 of 3...")
    driver.get("https://google.com")
    fileName = file + "Google"
    pickle.dump(driver.get_cookies(), open(fileName,"wb"))

    if verbose == True: print(tools.log() + "Saving cookie set 2 of 3...")
    driver.get("https://youtube.com")
    fileName = file + "YouTube"
    pickle.dump(driver.get_cookies(), open(fileName,"wb"))

    if verbose == True: print(tools.log() + "Saving cookie set 3 of 3...")
    driver.get("https://gmail.com")
    fileName = file + "Gmail"
    pickle.dump(driver.get_cookies(), open(fileName,"wb"))

    driver.refresh()

def loadCookies(driver, file, verbose):
    driver.get("https://google.com")
    fileName = file + "Google"
    cookies = pickle.load(open(fileName, "rb"))
    if verbose == True: print(tools.log() + "Loading cookie set 1 of 3...")
    for cookie in cookies:
        driver.add_cookie(cookie)

    if verbose == True: print(tools.log() + "Loading cookie set 2 of 3...")
    driver.get("https://youtube.com")
    fileName = file + "YouTube"
    cookies = pickle.load(open(fileName, "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    if verbose == True: print(tools.log() + "Loading cookie set 3 of 3...")
    driver.get("https://gmail.com")
    fileName = file + "Gmail"
    cookies = pickle.load(open(fileName, "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()
