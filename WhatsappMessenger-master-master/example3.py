# -- coding: utf-8 --
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
from urllib.parse import quote

options = Options()
# options.add_argument("user-data-dir=/Users/vaibhavchopra/Library/Application Support/Google/Chrome/Default")

message = """abcd"""

numbers = []
f = open("main.txt", "r")
for line in f.read().splitlines():
    if line != "":
        numbers.append(line)
f.close()
# numbers.reverse()
TRIES = 30

driver = webdriver.Chrome("drivers/chromedriver", options=options)
# driver.get('https://web.whatsapp.com')
# input()
c=0
for number in numbers[0:5]:
    c+=1
    print(c)
    if number == "":
        continue
    print("Number: " + number)
    try:
        url = "https://web.whatsapp.com/send?phone=91" + number + "&text=" + message
        #print(url)
        driver.get(url)
        sleep(5)
        # click_btn = driver.find_elements(By.CSS_SELECTOR,"footer > div.copyable-area  div:nth-child(3) > button").get(0)
        click_btn = WebDriverWait(driver, TRIES).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_4sWnG"))
        )
        click_btn.click()
        sleep(5)
        print("Message sent to: " + number)
    except Exception:
        print("Failed to send message to " + number)
        # append these number to failed.txt
        f = open("failed.txt", "a")
        f.write(number + "\n")
        f.close()
driver.quit()
