#!/usr/bin/env python
import requests
import re
import sys
from wordcloud import WordCloud

def getWords(com):
    return com.split()

# Cleaning is a bit gross because comments from the api include html
def cleanComment(com):
    # removing urls
    com = re.sub(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\/=]*)|(\<wbr\>[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)', '', com)

    # replacing html tags with spaces because comments like: 
    # <br>take<br>on<br>meeeee 
    # will get mashed together into one word when it should be 'take on me'
    com = re.sub(r'(<[^>]*>)', ' ', com)
    
    # removing html entites and non letters(numbers, punctuation)
    return re.sub(r'(&#?[\w|\d]+;)|([^a-zA-Z ])', '', com).strip()

thread = sys.argv[1]
r = requests.get(f'https://a.4cdn.org/mu/thread/{thread}.json')

if r.status_code != requests.codes.ok:
    raise RuntimeError(f"Request failed. Recievied {r.status_code} status code. Check thread number")
print("Thread found")

posts = r.json()['posts']
threadComs = ''
for post in posts:
    if 'com' in post:
        cleanCom = cleanComment(post['com'])
        threadComs += cleanCom + '\n'

wordcloud = WordCloud(width=1400, height=700).generate(threadComs)
wordcloud.to_file(f"{thread} world cloud.png")