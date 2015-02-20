from numpy import random
from bs4 import BeautifulSoup

def urlify_location(city, state):
    return "http://www.yelp.com/search/snippet?find_desc=%22how%20hard%20is%20it%20to%22&find_loc=" + city.replace(" ","%20") + "%2C%20" + state.replace(" ","%20")

def get_biz_from_location_query(response):
    response = response.json()
    end = len(response["search_map"]["markers"].keys()) - 1
    biz = random.randint(1,end)
    return response["search_map"]["markers"][str(biz)]["url"]

def urlify_biz(biz_snippet):
    return "http://www.yelp.com"+ biz_snippet + "/review_feed/?start=0&sort_by=relevance_desc&q=how%20hard%20is%20it"

def get_review_snippet(response):
    response = response.json()
    soup = BeautifulSoup(response["review_list"])
    text = soup.get_text()
    location = text.lower().find("how hard is it to")
    return text[location:location+200]
