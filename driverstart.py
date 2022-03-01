from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tools
import cookies
import signin

def driverStart(email, password, proxy, verbose):
    driver = headless()
    manual = False
    try:
        signinAttempt = signin.signin(driver, email, password, verbose)
        return driver
    except ValueError as err:
        print(err.args)
        if verbose == True: print(tools.log() + "You'll need to manually sign in.")
        driver.quit()
        manual = True

    if manual == True:

        driver = head()

        try:
            signinAttempt = signin.manual(driver, email, password, verbose)
            return driver
        except ValueError as err:
            print(err.args)
            print("idk how you got here. congratz, you've fucked it.")

def headless():
    options = Options()
    prefs = {'profile.managed_default_content_settings.images':2}
    options.add_experimental_option("prefs", prefs)
    options.headless = True
    driver = webdriver.Chrome(options=options)
    return driver

def head():
    options = Options()
    prefs = {'profile.managed_default_content_settings.images':2}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    return driver
