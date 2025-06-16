from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import time
class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def init_browser(self):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--incognito")
        chrome_driver = os.getcwd() + "\\chromedriver"
        browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
        return browser

    def login_mfb(browser,username,password):
        self.browser = browser
        self.username - username
        self.password = password
        browser.get("https://m.facebook.com/login.php")
        # browser.get("https://www.messenger.com/")
        time.sleep(2)
        # browser.find_element_by_css_selector("m_login_email").send_keys(
        #     username)
        browser.find_element_by_css_selector("._56bg._4u9z._5ruq").send_keys(
            username)
        browser.find_element_by_css_selector("._56bg._4u9z._27z2").send_keys(
            password + Keys.RETURN)   
        time.sleep(3)
        # bypass dang nhap bang click hinh anh
        # browser.get(
        #     "https://m.facebook.com/login/save-device/cancel/?flow=interstitial_nux&nux_source=regular_login")
        browser.find_element_by_css_selector("._54k8._52jg._56bs._26vk._56b_._56bw._56bu").click()
        browser.find_element_by_css_selector("._59tf._2ftq").click()
        return browser

    def send_message(browser, fbid, messages):
        self.browser = browser
        self.fbid = fbid
        self.messages = messages
        browser.get("https://m.facebook.com/messages/thread/"+fbid)
        browser.find_element_by_css_selector("textarea").send_keys(messages)
        browser.find_element_by_name("send").click()
        return browser

if __name__ == '__main__':
    username = ""
    password = ""'
    browser = Login(username, password)
    Login.init_browser()
    browser.login_mfb(browser,username,password)
    # 100003113987409 fb id nhung
    # 100004498980211 fb id hùng
    login_sucess.send_message(browser,"100004498980211","Chay duoc roi")
    # lucky_button = driver.find_element_by_css_selector("[name=btnI]")
    lucky_button.click()
    driver.quit()
    # capture the screen
    # driver.get_screenshot_as_file("capture.png")