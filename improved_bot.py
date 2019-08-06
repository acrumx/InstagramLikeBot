from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC # Waits until specified element is available

browser = webdriver.Firefox()
browser.get('https://instagram.com/')

login = browser.find_element_by_link_text('Log in')
login.click()

username = browser.find_element_by_xpath('/html/body/span/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
username.send_keys('username')

password = browser.find_element_by_xpath('/html/body/span/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
password.send_keys('password')
password.send_keys(Keys.ENTER)

not_now = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
not_now.click()

search_bar = browser.find_element_by_xpath('/html/body/span/section/nav/div[2]/div/div/div[2]/div/div/span[2]')
search_bar.click()

search_term = browser.find_element_by_xpath('/html/body/span/section/nav/div[2]/div/div/div[2]/input')
search_term.send_keys('#dogstagram')

search_click = browser.find_element_by_xpath('//a[@href="/explore/tags/dogstagram/"]')
search_click.click()




