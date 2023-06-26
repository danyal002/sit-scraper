import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import discord
from dotenv import load_dotenv

def check_website():
    options = Options()
    options.add_argument("--headless")
    service = Service('/usr/local/bin/chromedriver')  
    # service = Service('/usr/lib/chromium-browser/chromedriver')  
    driver = webdriver.Chrome(service=service, options=options)
    
    url = 'https://bolig.sit.no/en/' 
    
    driver.get(url)
    
    label = driver.find_element(By.CSS_SELECTOR, 'label[for="Trondheim"].checkbox__StyledLabel-sc-1371sdl-2.gkAgbU')
    
    if not label:
        notifyDiscordBot("An apartment has been found. Go book it!!")
    
    driver.quit()

def notifyMacOS(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

def notifyDiscordBot(text):
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")
    
    bot = discord.Client(intents=discord.Intents.default())
    
    @bot.event
    async def on_ready():
        await bot.guilds[0].text_channels[0].send(text)
        await bot.close()
    
    bot.run(token)

check_website()
