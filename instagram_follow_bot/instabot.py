from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# --------Constants------
DRIVER_PATH = "chromedriver.exe"


class InstaBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        self.driver.find_element_by_css_selector("div.mt3GC button").click()

    def login(self, username, password):
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password, Keys.ENTER)

    def find_followers(self, insta_acc):
        self.driver.get(f"https://www.instagram.com/{insta_acc}")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        followers = self.driver.find_elements_by_css_selector("li button")
        for follower in followers:
            follower.click()
            time.sleep(2)
