import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import tools
import cookies
#datetime, requests, colorama, selenium

def signin(driver, email, password, verbose): #headless, v1 signin
    cookiesPresent = cookies.cookieCheck(driver, email, verbose)
    if cookiesPresent == True:
        return True
    else:
        if verbose == True: print(tools.log() + "Getting login page...")
        driver.get("https://accounts.google.com/ServiceLogin")
        js = "document.getElementById('Email').value = '" + str(email) + "';"
        driver.execute_script(js)
        element = driver.find_element_by_id('Email')
        if verbose == True: print(tools.log() + "Submitting email...")
        element.send_keys(Keys.ENTER)
        try:
            if verbose == True: print(tools.log() + "Waiting for page load...")
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "link-forgot-passwd")))
        except:
            raise ValueError("Email is wrong.", email)

        #entering password
        if verbose == True: print(tools.log() + "Password page loaded...")
        js = "document.getElementById('Passwd').value = '" + str(password) + "';"
        driver.execute_script(js)
        element = driver.find_element_by_id('Passwd')
        element.send_keys(Keys.ENTER)
        if verbose == True: print(tools.log() + "Submitting password...")

        time.sleep(2)

        #verify it worked. if so, returns true. otherwise throws a ValueError
        if verbose == True: print(tools.log() + "Starting login verification...")
        driver.get("https://myaccount.google.com/")
        time.sleep(2)
        text = "Manage your info, privacy, and security to make Google work better for you"
        if (text in driver.page_source):
            cookies.saveCookies(driver, email, verbose)
            if verbose == True: print(tools.log() + "Session saved to: " + email)
            return True
        else:
            raise ValueError("shit didn't work lol", email, password)

def manual(driver, email, password, verbose): #non-headless, v2 signin
    cookiesPresent = cookies.cookieCheck(driver, email, verbose)
    if cookiesPresent == True:
        return True
    else:
        if verbose == True: print(tools.log() + "Getting login page...")
        driver.get("https://accounts.google.com/ServiceLogin")
        js = "document.getElementById('identifierId').value = '" + str(email) + "';"
        driver.execute_script(js)
        element = driver.find_element_by_id('identifierId')
        if verbose == True: print(tools.log() + "Submitting email...")
        element.send_keys(Keys.ENTER)
        try:
            if verbose == True: print(tools.log() + "Waiting for page load...")
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "forgotPassword")))
        except:
            raise ValueError("Email is wrong.", email)

        #entering password
        if verbose == True: print(tools.log() + "Password page loaded...")
        js = "document.getElementsByName('password')[0].value = '" + str(password) + "';"
        driver.execute_script(js)
        element = driver.find_element_by_name('password')
        element.send_keys(Keys.ENTER)
        if verbose == True: print(tools.log() + "Submitting password...")

        time.sleep(2)

        #verify it worked. if so, returns true. otherwise throws a ValueError
        if verbose == True: print(tools.log() + "Starting login verification...")
        time.sleep(2)
        text = "Manage your info, privacy, and security to make Google work better for you"
        worked = False
        while worked == False:
            if (text in driver.page_source):
                cookies.saveCookies(driver, email, verbose)
                if verbose == True: print(tools.log() + "Session saved to: " + email)
                worked = True
                return True
            else:
                if verbose == True: print(tools.log() + "Waiting for manual signin...")
                time.sleep(2)
