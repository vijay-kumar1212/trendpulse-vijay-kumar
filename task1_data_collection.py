import datetime
import json
import time
import os
import requests
import urllib3.exceptions

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


headers = {"User-Agent": "TrendPulse/1.0"}
# fetching ids from the provided hackers endpoint
resp = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json', headers=headers, verify=False)
top_stories_ids = resp.json()

# Storing categories and keywords for filtering the stories
categories = {
'technology' : ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
'worldnews' : ["war", "government", "country", "president", "election", "climate", "attack", "global"],
'sports' : ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
'science' : ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
'entertainment' : ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
}
records = []
# looping through all story ids to fetch story details.
for id in top_stories_ids:
    try:
        # performing get request to fetch story details
        resp_ = requests.get(url=f'https://hacker-news.firebaseio.com/v0/item/{id}.json',headers=headers,verify=False)
    # excepting Request exceptions to avoid crashing of the loop
    except requests.exceptions.RequestException as e:
        print(f"Request failed for story {id}: {e}")
        continue
    if resp_.status_code == 200:
        story_details = resp_.json()
    else:
        print(f"Failed to fetch story {id}: {resp_.status_code} \n  {resp_.text}")
        continue

    for category, keywords in categories.items():
        title = story_details['title'].lower()
        if any(keyword.lower() in title for keyword in keywords):
            records.append({'post_id': id,
                            'title': story_details.get('title', None),
                            'category': category,
                            'score': story_details.get('score', None),
                            'num_comments': story_details.get('descendants', None),
                            'author': story_details.get('by', None),
                            'url': story_details.get('url', None),
                            'collected_at': datetime.datetime.now().strftime("%Y%m%d")})
    time.sleep(2)

# creating a data directory if it's not created
os.makedirs('data', exist_ok = True)
# setting file path to store the stories data in JSON file
date_str = datetime.datetime.now().strftime("%Y%m%d")
file_path = f'data/trends_{date_str}.json'
# Opened file in write mode and updated the file with fetched story details
with open(file_path, 'w') as f:
    json.dump(records, f, indent = 2)
