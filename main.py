import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

email = input("Enter your email: ")
password = input("Enter your password: ")

PROMISED_UP = 150
PROMISED_DOWN = 10
TWITTER_EMAIL = email
TWITTER_PASSWORD = password

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.speedtest.net/")
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        safe_button = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
        button = self.driver.find_element(By.CLASS_NAME, value="start-text")
        safe_button.click()
        button.click()

        time.sleep(45)
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                             '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                             '1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                           '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                           '2]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        # login credentials
        # email
        email_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="text"]'))
        )
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.ENTER)

        # password
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="password"]'))
        )
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)

        # compose the tweet

        compose = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                                  '3]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                  '1]/div/div/div/div/div/div/div/div/div/div/label/div['
                                                  '1]/div/div/div/div/div/div[2]/div/div/div'))
        )
        compose.send_keys(
            f"Hey ISP, my current internet speed is download: {self.down} and upload {self.up}. Please improve it.")
        time.sleep(3)

        # post
        post = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                                  '3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div['
                                                  '2]/div[3]/div/span/span'))
        )
        post.click()

        time.sleep(5)
        self.driver.quit()


ip = InternetSpeedTwitterBot()
ip.get_internet_speed()

print(f"Download Speed: {ip.down}\n Upload Speed: {ip.up}")
ip.tweet_at_provider()
