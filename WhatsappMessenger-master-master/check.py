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

message = """*Recruitments for First Year Students are now live*🪄
%0d%0a%0d%0a
Join the *Student Technical Community* to connect and collaborate with individuals who share your interests. Gather experience from seniors who have won multiple *hackathons*, worked on a wide range of *projects* and are currently interning at various *MNCs*.🏆
%0d%0a%0d%0a
*STC* will assist you in all aspects of your college life and treasure you with memories that you will cherish for the rest of your life.💯
%0d%0a%0d%0a
📍 Link for registration: https://recruitments.stcvit.in/
%0d%0a%0d%0a
⭕⭕⭕⭕⭕⭕⭕⭕⭕
%0d%0a%0d%0a
💫 Follow us on *Instagram*, for more updates: https://www.instagram.com/stcvit/
%0d%0a%0d%0a
💫 For all your queries and announcements join our *Discord* server: https://discord.gg/tJQ4AzQeaa
%0d%0a%0d%0a
✨✨✨✨✨✨✨✨✨"""

numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
    if line != "":
        numbers.append(line)
f.close()
# numbers.reverse()
TRIES = 30

driver = webdriver.Chrome("drivers/chromedriver.exe", options=options)
# driver.get('https://web.whatsapp.com')
# input()

for number in numbers:
    if number == "":
        continue
    print("Number: " + number)
    try:
        url = (
            "https://web.whatsapp.com/send?phone=91"
            + "9766646882"
            + "&phone=917704004066"
            + "&text="
            + message
        )
        print(url)
        driver.get(url)
        sleep(10)
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
