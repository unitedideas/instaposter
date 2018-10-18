"""This script is automatically executed every 6h on my server via cron"""
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import secrets
import time
import os, sys, subprocess
import webbrowser

options = Options()
options.add_argument(
    '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
# options.add_argument("--headless")
session = webdriver.Chrome(options=options)
session.get('https://www.instagram.com/accounts/login/?source=mobile_nav_menu')

# login credentials
insta_username = secrets.insta_username
insta_password = secrets.insta_password

# if on insta home page
try:
    usr_login_button = session.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div/div/div/div[2]/button')
    usr_login_button.click()
    print('Login clicked')
except:
    print("at " + session.current_url)

# if on login page
WebDriverWait(session, 5).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
print("Username input loaded")
username_input = session.find_element_by_xpath("//input[@name='username']")
username_input.click()
username_input.send_keys(insta_username)
print("Username loaded")

time.sleep(2)

password_input = session.find_element_by_xpath("//input[@name='password']")
password_input.click()
password_input.send_keys(insta_password)
print('Passsword loaded')

time.sleep(2)

print('Trying to login')
login_button = session.find_element_by_xpath("//button[text()='Log in']")
login_button.click()

time.sleep(2)

print('Skip "save your login info"')
WebDriverWait(session, 5).until(
    EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']")))
not_now_btn = session.find_element_by_xpath("//button[text()='Not Now']")
not_now_btn.click()

print('Logged in')
time.sleep(2)

print('Clicking post button now')
WebDriverWait(session, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]/span')))
post_btn = session.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]/span')
post_btn.click()
# post_btn.send_keys(r'/Users/shanecheek/Desktop/projects/instaposter/autopost/1/fd3844becd196550329031b0c7afdb57.jpg')
# actions.send_keys('/Users/shanecheek/Desktop/projects/instagram_bot/autopost/fd3844becd196550329031b0c7afdb57.jpg')
print('found it, clicked post!!!')
time.sleep(2)

payload = session.file_detector.is_local_file(
    r"/Users/shanecheek/Desktop/projects/instaposter/autopost/1/fd3844becd196550329031b0c7afdb57.jpg")
print(payload)

alert = session.switch_to.alert()
alert.accept()
def openFolder(path):
    subprocess.Popen(['open', '--', path])


openFolder('/Users/shanecheek/Desktop/projects/instaposter/autopost/1/fd3844becd196550329031b0c7afdb57.jpg')

WebDriverWait(session, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//input[@type="file"]'))).send_keys(
    "/Users/shanecheek/Desktop/projects/instaposter/autopost/1/fd3844becd196550329031b0c7afdb57.jpg")
session.close()
session.quit()
