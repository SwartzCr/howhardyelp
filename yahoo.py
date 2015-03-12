from splinter import Browser
import json
from xvfbwrapper import Xvfb
import time

def get_cookies():
    with open("cookies.json", 'r') as f:
        cookies = json.load(f)
    return cookies

def post(question):
    vdisplay = Xvfb()
    vdisplay.start()
    browser = Browser()
    cookies = get_cookies()
    browser.cookies.add(cookies)
    browser.visit("http://answers.yahoo.com")
    # what is this shit
    browser.cookies.add(cookies)
    browser.reload()
    browser.find_by_name("title")[0].fill(question)
    browser.find_by_value("Submit")[0].click()
    time.sleep(10)
    url = browser.url
    browser.quit()
    vdisplay.stop()
    return url
