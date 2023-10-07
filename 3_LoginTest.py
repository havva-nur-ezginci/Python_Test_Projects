from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

service = Service("./chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Login sayfasına git
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(1)

def login(_username,_password):
    global driver
    # kullanıcı adı gir
    username = driver.find_element(By.ID,"username")
    username.send_keys(_username)
    time.sleep(1)
    # kullanıcı şifresi gir
    password = driver.find_element(By.ID,"password")
    password.send_keys(_password)
    time.sleep(1)

    # login düğmesine tıkla
    login_button = driver.find_element(By.CSS_SELECTOR,"button.radius").click()
    time.sleep(1)

    # Alınan mesaj
    mesaj = driver.find_element(By.ID, "flash").text

    return mesaj

time.sleep(1)

# yanliş kullanıcı adı =>  Your username is invalid!
mesaj = login("hatali","SuperSecretPassword!")

if "Your username is invalid!" in mesaj:
    print("Yanlış kullanıcı ad testi doğru çalıştı.")
else:
    print("HATA: yanlış kullanıcı ad testi çalışmyor.")

time.sleep(1)

# yanliş kullanıcı şifresi => Your password is invalid!
mesaj = login("tomsmith","hatali")

if "Your password is invalid!" in mesaj:
    print("Yanlış kullanıcı şifre testi doğru çalıştı.")
else:
    print("HATA: yanlış kullanıcı şifre testi çalışmyor.")

time.sleep(1)

# ikisi de doğruysa => mesaj ;You logged into a secure area! , link secure içerecek , başlık Secure Area olmalıdır.
mesaj = login("tomsmith","SuperSecretPassword!")

if "You logged into a secure area!" in mesaj:
    print("OK, doğru kullanıcı adı ve şifre testi çalıştı.")
else:
    print("HATA: Doğru kullanıcı adı ve şifre testi çalışmıyor")

link = driver.current_url
if "secure" in link:
    print("OK link secure içeriyor.")
else:
    print("HATA: link secure içermiyor")

title_area = driver.find_element(By.CSS_SELECTOR, "h2").text

if "Secure Area" in title_area:
    print("OK, Sayfa başlığı doğru")
else:
    print("HATA: sayfa başlığı yanliş")

# logout düğmesine tıkla
driver.find_element(By.CSS_SELECTOR,"a[class='button secondary radius']").click()

#sayfa linkini doğrula
if "login" in driver.current_url:
    print("OK. Login sayfasına dönüldü.")
else:
    print("HATA: Login sayfasına donmedi")

time.sleep(1)

driver.quit() #seleniumun kullandığı tüm pencereleri kapatır.