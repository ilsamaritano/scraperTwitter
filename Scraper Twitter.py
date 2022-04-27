import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Edge
import time
import csv
import random

PATH = "C:\Drivers\msedgedriver.exe"
driver = Edge(PATH)

# Seleziono il sito da scansionare
driver.get('https://twitter.com/login')
driver.maximize_window()
print("Page title is: %s" % (driver.title))
# Aspetto il caricamento della pagina, trovo il bottone per accettare la policy dei cookie attraverso l'Xpath e lo clicco
time.sleep(3)

# try:
xpath_username = '//input[@name="username"]'
#WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, xpath_username)))
# time.sleep(5)
uid_input = driver.find_element("xpath", xpath_username)
uid_input.send_keys("3665409504")
# except:
#    print("Timeout while waiting for Login screen")


avanti = driver.find_element("xpath", '//span[contains(text(), "Avanti")]')
avanti.click()

time.sleep(2)

xpath_password = '//input[@name="password"]'
uid_input = driver.find_element("xpath", xpath_password)
uid_input.send_keys("orcone")

time.sleep(2)

accedi = driver.find_element("xpath", "// span[contains(text(), 'Accedi')]")
accedi.click()

time.sleep(3)

#driver.execute_script("window.scrollTo(0, 150)")
cookie = driver.find_element("xpath", "//span[contains(text(), 'Chiudi')]")
cookie.click()

time.sleep(3)

argomento = driver.find_element(
    "xpath", "// span[contains(text(), '#IlCollegio')]")
argomento.click()

time.sleep(3)

SCROLL_PAUSE_TIME = random.randint(3, 5)

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
testoelem = []
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    elementi = driver.find_elements(
        "xpath",  '//div[contains(@class, "css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0")]')
    for elem in elementi:
        try:
            testoelem.append(["0", "0", elem.__getattribute__("text")])
        except:
            print("errore")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


time.sleep(2)


# Clicca l'elemento per avanzare di pagina dopo aver atteso il caricamento (Se non trova più l'elemento mi fermo, significa che sono finite le pagine)


with open("C:\output.csv", 'w', encoding='utf-8') as data_file:
    writer = csv.writer(data_file, delimiter='\n', dialect='excel')
    writer.writerow(testoelem)

# Termina l'esecuzione
driver.quit()
