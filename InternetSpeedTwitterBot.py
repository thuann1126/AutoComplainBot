import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class InternetSpeedTwitterBot():
    def __init__(self, driver_path, expected_up, expected_down):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = down
        self.up = up
        self.expected_up = expected_up
        self.expected_down = expected_down
        self.username = 'anhthuanzw@gmail.com'
        self.password = 'Tracyluxe2002!'
    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(4)
        go_button = self.driver.find_element(by.CSS_SELECTOR,'#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.start-button > a > span.start-text')
        go_button.click()

        time.sleep(60)
        self.down = self.driver.find_element(by.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.up = self.driver.find_element(by.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')

    def twitter_complain_post(self):
        if self.up < self.expected_up or self.down < self.expected_down:

            #Login into Twitter
            self.driver.get('https://twitter.com/login')

            email_input = self.driver.find_element(by.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
            email_input.send_keys(self.username)
            next_button = self.driver.find_element(by.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
            next_button.click()
            time.sleep(5)

            password_button = self.driver.find_element(by.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password_button.send_keys(self.password)
            logging_button = self.driver.find_element(by.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
            logging_button.click()
            time.sleep(5)

            tweet_post_compose = self.driver.find_element(by.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            tweet_post_compose.send_keys(f'Hey Internet Provider, why I get {self.up} upload speed and {self.down} download speed while I purchased for {self.expected_up} upload speed and {self.expected_down} download speed')

            tweet_button = self.driver.find_element(by.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
            tweet_button.click()

            time.sleep(10)
            self.driver.close()
            self.driver.quit()
        else:
            print("Everything is fine")





