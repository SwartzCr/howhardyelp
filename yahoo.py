from splinter import Browser
import json
from xvfbwrapper import Xvfb

def get_cookies():
    with open("cookies.json", 'r') as f:
        cookies = f.load()
    return cookies

def post(question):
    vdisplay = Xvfb()
    vdisplay.start()
    browser = Browser()
    browser.cookies(get_cookies())
    browser.visit("http://answers.yahoo.com")
    browser.find_by_name("title")[0].fill(question)
    browser.find_by_value("Submit")[0].click()
    url = browser.url
    browser.quit()
    vdisplay.stop()
    return url
