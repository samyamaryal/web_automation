import time

from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox, Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.relative_locator import locate_with

user_video = input("What video would you like to play?\n")

path = r"C:\Program Files\Mozilla Firefox"
options = Options()
options.set_preference('profile', path)
service = Service(r".\\geckodriver.exe")

driver = Firefox(service=service, options=options)

driver.get("http://www.youtube.com")
search_bar = driver.find_element(by=By.TAG_NAME, value="input")
search_bar.send_keys(user_video)
time.sleep(1)
search_bar.send_keys(Keys.RETURN)
time.sleep(2)

element_toplay = locate_with(By.CLASS_NAME, "ytd-video-renderer")

to_play = driver.find_element(element_toplay)
to_play.click()
