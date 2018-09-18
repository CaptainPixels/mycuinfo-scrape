from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException

import json
import time

driver = webdriver.Chrome(executable_path=r'/Users/captainpixels/Desktop/selenium/chromedriver')
driver.get("https://classes.colorado.edu/")

dropdown = driver.find_element_by_xpath("//select[@id='crit-course_level']")
button_search = driver.find_element_by_xpath("//button[@id='search-button']")

courseLevel_list = dropdown.find_elements_by_xpath(".//*")
courseLevel_list = courseLevel_list[1:]

dropdown.click()
courseLevel_list[0].click()
button_search.click()
time.sleep(2)
x = driver.find_elements_by_xpath("//div[@class='panel__body']//div[@class='result result--group-start']//a[@href='#']")

y=0
while y < len(x):
    try:
        x[y].click()
    except WebDriverException as Exception:
        pass
    time.sleep(.1)
    try:
        header = driver.find_element_by_xpath("//div[@class='panel__body']//div[@class='cols pad--tlr-default']")
        code = header.find_element_by_xpath("//div[@class='dtl-course-code']").get_attribute('innerHTML')
        name = header.find_element_by_xpath("//div[@class='text col-8 detail-title text--huge']").get_attribute('innerHTML')

        seats = driver.find_element_by_xpath("//div[@class='panel__body']//div[@class='row pad--lr-default']").get_attribute('innerHTML')
        
        print(code + " / " + name)
        y+=1
    except StaleElementReferenceException as Exception:
        pass
