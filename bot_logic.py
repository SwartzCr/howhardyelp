import json
import Twython
import yelp_search
import requests
from numpy import random

def auth():
    with open("access.json", 'r') as f:
        db = json.load(f)
    return Twython(db["API_Key"], db["API_Secret"], db["Access_Token"], db["Access_Token_Secret"])

def get_corpera():
    with open("us_cities.json", 'r') as f:
        cities = json.load(f)
    return cities["cities"]

def pick_loc(corpora):
    idx = random.randint(0,len(corpora)-1)
    loc = corpora[idx]
    return loc["city"], loc["state"]

def get_tweet_text(review_snippet):
    punc = [i for (i, x) in enumerate(review_snippet.splitlines()[0]) if x in ["!", ".", "?", "\n"]]
    for place in punc[::-1]:
        if place <= 139:
            return review_snippet[:place+1]
    return review_snippet[:140]

def prep_tweet():
# get city state
    corpora = get_corpera()
    city, state = pick_loc(corpora)
    loc_url = yelp_search.urlify_location(city, state)
    loc_resp = requests.get(loc_url)
    biz_snippet = yelp_search.get_biz_from_location_query(loc_resp)
    biz_url = yelp_search.urlify_biz(biz_snippet)
    biz_resp = requests.get(biz_url)
    review_snippet = yelp_search.get_review_snippet(biz_resp)
    return get_tweet_text(review_snippet)

def main():
    twitter = auth()
    tweet = ""
    while len(tweet) < 1:
        tweet = prep_tweet()
    twitter.update_status(status=tweet)
    #print tweet

main()
