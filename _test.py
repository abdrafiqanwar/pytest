import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
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
    time.sleep(3)
    
    browser.execute_script("arguments[0].click();", button)
    
    data = browser.find_element(By.ID, 'collapseFour')
    list = data.find_element(By.CLASS_NAME, 'list-group')
    labs = list.find_elements(By.TAG_NAME, 'a')
    
    exists = 0
    nothing = 0
    
    for lab in labs:
        browser.execute_script("arguments[0].click();", lab)
        time.sleep(3)

        name = lab.text
        info = browser.find_element(By.CLASS_NAME, 'list-group-item')

        browser.execute_script("arguments[0].scrollIntoView(true);", info)
        time.sleep(3)

        string = "http"
        script = f'return document.body.innerText.includes("{string}");'
        text_found = browser.execute_script(script)

        if(text_found):
            print(name, "mempunyai alamat website")
            exists += 1
        else:
            print(name, "belum mempunyai alamat website")
            nothing += 1
            
    print("Ada", exists, "lab yang mempunyai alamat website")
    print("Ada", nothing, "lab yang tidak mempunyai alamat website")




        
            

    
    