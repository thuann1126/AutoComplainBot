from InternetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISE_DOWN = 70
PROMISE_UP = 1.5
CHROME_DRIVER_PATH = 'C:\Development\chromedriver.exe'
SPEED_TEST_URL

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH, PROMISE_UP, PROMISE_DOWN)
bot.get_internet_speed()
bot.twitter_complain_post()


