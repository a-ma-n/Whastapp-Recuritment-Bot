from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote  

from time import sleep
css_selector = "#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text"

msg = '''
🔵🔵🔵🔵🔵🔵🔵🔵

Student Technical Community (STC-VIT) is thrilled and excited to announce the core committee selections for the year 2020 🎉 starting 12th December.

STC-VIT is a joyous group of talented developers and tech enthusiasts. With Microsoft Student Learn Ambassadors, Snapchat representatives and Alexa Student Influencers, the chapter provides excellent mentorship and opportunities to young and enthusiastic students.

STC-VIT is known to conduct successful events like BREW'19 and Craft-404 

 Steps to register 
👉 Open register.stcvit.in
👉 Enter Your Details
👉 Select Date for first round of selection according to your choice (12/13/14/15)
👉 Select a time slot for the first round (9:30a.m,3:30p.m,7:00p.m)

⏰Wait for us to get back at you!

 Know more about us :
Website: stcvit.in
Instagram : instagram.com/mstcvit
Facebook : fb.com/mstcvit
LinkedIn: linkedin.com/company/micvitvellore


🔵🔵🔵🔵🔵🔵🔵🔵
'''     

driver = webdriver.Chrome("drivers\\chromedriver.exe")

phone = []                                                     
with open ('numbers.txt') as numbers_file:                 
    for line in numbers_file:
    	line=line.strip()
    	if len (line)==10:								   	
    		phone.append(str(line))

msg = quote(msg)  
driver.get("https://web.whatsapp.com")  
sleep(2)
failed_list = []
for index, number in enumerate(phone, 1):
    url = "https://web.whatsapp.com/send?phone=91" + number + "&text=" + msg
    driver.get(url)
    TRIES = 50

    sleep(3)  
    for i in range(TRIES):
        try:
            driver.find_element_by_css_selector(css_selector).send_keys(Keys.RETURN)
            driver.execute_script("window.onbeforeunload = function() {};")
            print (f'Sent to {index} : {number}')
            break
        except:
            sleep(1)
        
    else:
        failed_list.append(number)
    
print ("Done")
driver.quit() 