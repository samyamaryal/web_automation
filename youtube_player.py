import time

from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox, Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.relative_locator import locate_with
# Take user input & play that video.
user_video = input("What video would you like to play?\n")

#path to the browser, used to initialize the webdriver
path = r"C:\Program Files\Mozilla Firefox"
options = Options()
options.set_preference('profile', path)
# specify the path to geckodriver, which is used to automate Firefox. This driver is different for different browsers, and must be added to PATH.
service = Service(r".\\geckodriver.exe")

# initialize the webdriver
driver = Firefox(service=service, options=options)

driver.get("http://www.youtube.com")
# find the search bar to insert the keyword
search_bar = driver.find_element(by=By.TAG_NAME, value="input")
search_bar.send_keys(user_video)
# There must be a certain delay between adding the user input to the search bar & hitting the enter key.
time.sleep(1)
search_bar.send_keys(Keys.RETURN)
# add delay between hitting search & playing the video.
time.sleep(2)

#locate the first video in the search results.
element_toplay = locate_with(By.CLASS_NAME, "ytd-video-renderer")

#find the first video & play it using click()
to_play = driver.find_element(element_toplay)
to_play.click()
