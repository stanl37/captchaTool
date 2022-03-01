import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import tools
import time
import requests
#datetime, requests, colorama, selenium

def clickLink(driver, verbose):
    i = 0
    while i <= 3:
        try:
            links = driver.find_elements_by_partial_link_text('')
            l = links[random.randint(0, len(links)-1)]
            l.click()
            i = i + 1
        except:
            if verbose == True: print(tools.log() + "Error clicking.")
            time.sleep(1)


def search(driver, verbose):
    driver.get("https://google.com")

    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    wordString = WORDS[random.randint(0,len(WORDS))].decode() + " " + WORDS[random.randint(0,len(WORDS))].decode() + " " + WORDS[random.randint(0,len(WORDS))].decode()

    if verbose == True: print(tools.log() + "Running search on: " + wordString)
    js = "document.getElementsByName('q')[0].value = '" + wordString + "';"
    driver.execute_script(js)
    driver.find_element_by_id('tsf').submit()
    time.sleep(5)
    clickLink(driver, verbose)



def youtube(driver, verbose):
    driver.get("https://youtube.com")

    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()

    query = 'https://www.youtube.com/results?search_query={}+{}'.format(WORDS[random.randint(0,len(WORDS))].decode(), WORDS[random.randint(0,len(WORDS))].decode())

    driver.get(query)
    clickLink(driver, verbose)
    if verbose == True: print(tools.log() + "YouTube on: " + query)

    try:
        element = driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > paper-button')
        label = element.get_attribute("aria-label")
        if 'Subscribe' in label:
            element.click()
        label = element.get_attribute("aria-label")
        if 'Unsubscribe' in label and verbose == True:
            print(tools.log() + "Subscribed to current video artist.")
    except:
        print("error but idk how you got here")

#site is down atm so just browsing randomly on basic pages, not much else possible
def pooky(driver, verbose):
    driver.get("https://supremenewyork.com")
    element = driver.find_element_by_class_name('shop_link').click()
    time.sleep(3)
    clickLink(driver, verbose)
