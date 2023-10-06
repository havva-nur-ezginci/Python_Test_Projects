from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("./chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

"""Internet browser functions"""

driver.get("http://www.apple.com")
link = driver.current_url
print("mevcut başlık: "+link) # https://www.apple.com/

driver.maximize_window()

driver.get("http://www.turkcell.com") # istenilen sayfaya git
link = driver.current_url
baslik = driver.title

if "turkcell.com" in link:
    print("True: "+link)
    print("Title : "+baslik)

driver.back() # önceki sayfaya gitmek için
link = driver.current_url
if "apple.com" in link:
    print("Önceki sayfaya geçtin: "+link)

driver.forward() # sonraki sayfaya gitmek için
link = driver.current_url
if "hatali_icerik" in link:
    print("Sonraki sayfaya geçtin: "+link)
else:
    driver.save_screenshot("./ekrangoruntusu.png")


# driver.refresh() # sayfa yenileme


# driver.close() #şuanki pencereyi kapatır.

driver.quit() #seleniumun kullandığı tüm pencereleri kapatır.
