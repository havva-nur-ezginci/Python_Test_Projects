from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

service = Service("./chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()


driver.get("https://duckduckgo.com")
#webelement id ile bulundu
aramakutusu = driver.find_element(By.ID, "searchbox_input")
aramakutusu.send_keys("yazılım")
time.sleep(2)
aramakutusu.send_keys(Keys.ENTER)
time.sleep(2)
#----------------------------------------------
driver.get("https://pypi.org")
time.sleep(1)
#webelement name ile bulundu
aramakutusu = driver.find_element(By.NAME, "q")
aramakutusu.send_keys("drivers")
time.sleep(2)
aramakutusu.send_keys(Keys.ENTER) #tıklama ile arama
time.sleep(2)

#---------------------------------------------
# Tıklama
driver.get("https://pypi.org")
time.sleep(1)
#webelement name ile bulundu
aramakutusu = driver.find_element(By.NAME, "q")
aramakutusu.send_keys("drivers")
# büyüteç arama simgesiyle click
driver.find_element(By.CSS_SELECTOR, ".search-form__button[type='submit']").click()
time.sleep(2)


#tıklanacak linkin locator ı => .package-snippet[href="/project/gtt-drivers/"]
driver.find_element(By.CSS_SELECTOR, '.package-snippet[href="/project/gtt-drivers/"]').click()
time.sleep(2)
#------------------------------------------------
# Metin/yazı okuma

driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
time.sleep(1)
haftanin_seckin_alani = driver.find_element(By.ID,"mp-tfa")
haftanin_seckin_metni = haftanin_seckin_alani.text
print(haftanin_seckin_metni)

haftanin_seckin_konusu = haftanin_seckin_metni.split(",")[0]#return list
print("haftanin seckin konusu : "+haftanin_seckin_konusu)

gunun_kaliteli_konusu= driver.find_element(By.ID,"mf-tfp").text.split(",")[0]
print("gunun_kaliteli_konusu : "+gunun_kaliteli_konusu)



driver.quit() #seleniumun kullandığı tüm pencereleri kapatır.