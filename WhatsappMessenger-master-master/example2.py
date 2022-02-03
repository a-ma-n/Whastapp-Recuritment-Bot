from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
from urllib.parse import quote

options = Options()

message='''
🔵🔵🔵🔵🔵🔵🔵🔵                                                                                                                                           Student Technical Community (STC-VIT) is thrilled and excited to announce the core committee selections for the year 2020 🎉 starting 12th December.                                                                                                                          STC-VIT is a joyous group of talented developers and tech enthusiasts.                                                                        With Microsoft Student Learn Ambassadors, Snapchat representatives and Alexa Student Influencers, the chapter provides excellent mentorship and opportunities to young and enthusiastic students.                                              STC-VIT is known to conduct successful events like BREW'19 and Craft-404                                                                 Steps to register                                                                                                                                                              👉 Open register.stcvit.in                                                                                                                                                👉 Enter Your Details                                                                                                                                                         👉 Select Date for first round of selection according to your choice (12/13/14/15)                                                                                                                                                                      👉 Select a time slot for the first round (9:30a.m,3:30p.m,7:00p.m)                                                                               ⏰Wait for us to get back at you!                                                                                                                                  Know more about us :                                                                                                                                                  Website: stcvit.in                                                                                                                                                          Instagram : instagram.com/mstcvit                                                                                                                              Facebook : fb.com/mstcvit                                                                                                                                           LinkedIn: linkedin.com/company/micvitvellore                                                                                                                🔵🔵🔵🔵🔵🔵🔵🔵
'''

numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
	if line != "":
		numbers.append(line)
f.close()
TRIES = 20

driver = webdriver.Chrome("drivers\\chromedriver.exe", options=options)
driver.get('https://web.whatsapp.com')
input()
for number in numbers:
	if number == "":
		continue
	print('Number: ' + number)
	try:
		url = 'https://web.whatsapp.com/send?phone=91' + number + '&text=' + message
		driver.get(url)
		click_btn = WebDriverWait(driver, TRIES).until(EC.presence_of_element_located((By.CLASS_NAME , '_3M-N-')))
		click_btn.click()
		sleep(1)
		print('Message sent to: ' + number)
	except Exception:
		print('Failed to send message to ' + number)
driver.quit()