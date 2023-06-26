import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def check_website():
    options = Options()
    options.add_argument("--headless")
    service = Service('/usr/local/bin/chromedriver')  
    driver = webdriver.Chrome(service=service, options=options)
    
    url = 'https://bolig.sit.no/en/' 
    
    driver.get(url)
    
    label = driver.find_element(By.CSS_SELECTOR, 'label[for="Trondheim"].checkbox__StyledLabel-sc-1371sdl-2.gkAgbU')
    
    if not label:
        notify("Apartment Found", "Book your fucking room right now!!")
    
    driver.quit()


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


check_website()
