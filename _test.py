import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    
def test_web_able(browser):
    browser.get("https://pyapp.unhas.ac.id/laboratorium/")
    link_element = browser.find_element(By.ID, "headingFour")
    button = link_element.find_element(By.TAG_NAME, "button")
    browser.execute_script("arguments[0].scrollIntoView(true);", button)
    browser.execute_script("arguments[0].click();", button)
    lab = browser.find_element(By.ID, 'collapseFour')
    link_elements = lab.find_element(By.CLASS_NAME, 'list-group')
    elements = link_elements.find_elements(By.TAG_NAME, 'a')

    for link in elements:
    #link.click()
        browser.execute_script("arguments[0].click();", link)
    
    assert 'Web Able' in browser.title