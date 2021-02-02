from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os

# --------Constants-------
chrome_driver_path = "C:/Users/acipt/Desktop/PythonProjects/SeleniumDevelpment/chromedriver.exe"
FORM_URL = os.environ.get("FORM_URL")
# ---- link with specified find------
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56825484228516%2C%22east%22%3A-122.29840315771484%2C%22south%22%3A37.69120074057586%2C%22north%22%3A37.85928662873102%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
# --------Beautiful soup - Getting address, price and link-----------

# -------Getting HTML----------
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/87.0.4280.141 Safari/537.36", "Accept-Language": "en-US,en;q=0.9"}
response = requests.get(url=ZILLOW_URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# -------Links------------
articles = soup.find_all(name="a", class_="list-card-img")
article_links = [article.get("href") for article in articles]
# -------Addresses------------
address_list = soup.find_all(name="address")
addresses = [address.getText() for address in address_list]

# -------Prices----------------
price_list = soup.find_all(name="div", class_="list-card-price")
prices = [price.getText().replace("+", "") for price in price_list]

# ----------Fixing links ---------
changed_articles = []
for article in article_links:
    change = article.replace("https://www.zillow.com/homedetails", "")
    new_article = (f"https://www.zillow.com/homedetails{change}")

    changed_articles.append(new_article)
# ------- Selenium go to form--------
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(FORM_URL)

# -----Sending gathered into into a form-----
for (address, price, link) in zip (addresses,changed_articles,prices):
    time.sleep(2)
    inputs = driver.find_elements_by_css_selector("input.exportInput")
    inputs[0].send_keys(address)
    inputs[1].send_keys(link)
    inputs[2].send_keys(price)
    send = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    send.click()
    new = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    new.click()