from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

service = Service("./chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Login sayfasına git
driver.get("https://www.dr.com.tr/")
time.sleep(1)

# webelement listesi

kitap_menusu = driver.find_element(By.CSS_SELECTOR,"a[href='/kategori/kitap'][class='pointer-events-auto']")

#Instantiating Actions class
actions = ActionChains(driver)

#hover over element - mouse ile üzerine gelme
actions.move_to_element(kitap_menusu).perform()

time.sleep(2)

# çok satanlar boulmune tıkladık
driver.find_element(By.XPATH,"(//li[@data-id='15715']/a)[1]").click()

# Tüm Kitapların ismini liste olarak alma
kitap_isimleri = driver.find_elements(By.XPATH,"//h3[@class='seo-heading']/a[starts-with(@href,'/kitap/')]")

number = 1
for i in kitap_isimleri:
    print(number,"- ",i.text)
    number+=1




time.sleep(1)

driver.quit() #seleniumun kullandığı tüm pencereleri kapatır.