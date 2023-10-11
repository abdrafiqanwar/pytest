from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://pyapp.unhas.ac.id/laboratorium/")
time.sleep(3)
link_element = driver.find_element(By.ID, "headingFour")
button = link_element.find_element(By.TAG_NAME, "button")
driver.execute_script("arguments[0].scrollIntoView(true);", button)
driver.execute_script("arguments[0].click();", button)

time.sleep(3)

lab = driver.find_element(By.ID, 'collapseFour')
link_elements = lab.find_element(By.CLASS_NAME, 'list-group')
elements = link_elements.find_elements(By.TAG_NAME, 'a')

for link in elements:
    #link.click()
    driver.execute_script("arguments[0].click();", link)
    time.sleep(3)

    list = driver.find_element(By.CLASS_NAME, 'list-group-item')

    driver.execute_script("arguments[0].scrollIntoView(true);", list)

    fa = list.find_element(By.CLASS_NAME, 'fa fa-globe')
    assert fa is not None, "Elemen tidak ditemukan."


time.sleep(3)

driver.close()