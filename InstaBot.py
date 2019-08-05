# this file is the code for automating liking mutuals instagram posts

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        # Tells the browser to find the login button on the Instagram page
        login_button.click()
        # Browser takes 2 secs to load the login page
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        # If anything is in the username box prior to the program entering username,
        # the browser will clear the existing text
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(8)
        notif = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]")
        time.sleep(8)
        notif.click()


    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
        # Bot simulates scrolling through the webpage
        for i in range (1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight")
            time.sleep(2)


        # Searching for picture link

        hrefs = driver.find_element_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' photos: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_link_text("Like").click()
                time.sleep(20)
            except Exception as e:
                time.sleep(2)


austinIG = InstagramBot("instagram_username", "instagram_password")
austinIG.login()
austinIG.like_photo('fitness')
