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

data = driver.find_element(By.ID, 'collapseFour')
list = data.find_element(By.CLASS_NAME, 'list-group')
labs = list.find_elements(By.TAG_NAME, 'a')

exists = 0
nothing = 0
    
for lab in labs:
    driver.execute_script("arguments[0].click();", lab)
    time.sleep(3)

    name = lab.text
    info = driver.find_element(By.CLASS_NAME, 'list-group-item')

    driver.execute_script("arguments[0].scrollIntoView(true);", info)
    time.sleep(3)

    string = "http"
    script = f'return document.body.innerText.includes("{string}");'
    text_found = driver.execute_script(script)

    if(text_found):
        print(name, "mempunyai alamat website")
        exists += 1
    else:
        print(name, "belum mempunyai alamat website")
        nothing += 1
            
    print("Ada", exists, "lab yang mempunyai alamat website")
    print("Ada", nothing, "lab yang tidak mempunyai alamat website")