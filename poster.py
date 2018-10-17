"""This script is automatically executed every 6h on my server via cron"""
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0

# from instapy import InstaPy
# from instapy.util import smart_run
options = Options()
options.add_argument(
    '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
# options.add_argument("--headless")
session = webdriver.Chrome(options=options)
session.get('https://www.instagram.com/accounts/login/')
from . import secrets

# login credentials
insta_username = secrets.insta_username
insta_password = secrets.insta_password

print('2')
try:
    login_button = session.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[2]/button')
    login_button.click()
    print('login clicked')
except:
    print("at " + session.current_url)
try:
    username_input = WebDriverWait(session, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@role,'menuitem')]")))
    print("made it to xpath")
except:
    pass
# except:
#     print('failed the selector')
# try:
#     username_input = WebDriverWait(session, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="fb2316e2f4a1d"]')))
#     print('got the xpath')
# except:
#     print('failed the xpath')
# try:
#     username_input = session.find_element_by_id('fb2316e2f4a1d').text
#     print('got the id')
# except:
#     print('failed the id')

# try:
#     post_it = session.find_element_by_class_name("q02Nz _0TPg").text
# except:
#     print('fail 1')
# try:
#     post_it = session.find_element_by_xpath("//div[contains(@class,'q02Nz _0TPg')]").text
# except:
#     print('fail 2')
# try:
#     post_it = session.find_element_by_xpath("//div[contains(@class,'0TPg')]").text
# except:
#     print('fail 3')
# try:
#     post_it = session.find_element_by_xpath("//div[contains(@role,'menuitem')]").text
# except:
#     print('fail 4')
# try:
#     post_it = session.find_element_by_xpath("//div[contains(@tabindex,'0')]").text
# except:
#     print('fail 5')
# try:
#     post_it = session.find_element_by_xpath("//div[@tabindex='0']").text
# except:
#     print('fail 6')
# try:
#     post_it = session.find_element_by_xpath("//span[@class='glyphsSpriteNew_post__outline__24__grey_9 u-__7']").text
# except:
#     print('fail 7')
# try:
#     post_it = session.find_element_by_xpath("//span[@class='glyphsSpriteNew_post__outline__24__grey_9 u-__7']").text
# except:
#     print('fail 8')
# try:
#     post_it = session.find_element_by_xpath("//span[contains(@aria-label,'New Post')]").text
# except:
#     print('fail 9')
# try:
#     post_it = session.find_element_by_xpath("//span[@aria-label='New Post']").text
# except:
#     print('fail 10')
# try:
#     post_it = session.find_element_by_css_selector("div.q02Nz:nth-child(3)").text
# except:
#     print('fail 11')
# print(post_it)
print('made it')

session.close()
session.quit()
