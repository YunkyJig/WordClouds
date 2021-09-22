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

f = open("data.txt", "r")
coms = f.read()
coms = coms.split('\n')

for com in coms:
    cleanCom = cleanComment(com)
    # print(cleanCom)
    # print(getWords(cleanCom))
    with open('cleanData.txt', 'a') as the_file:
        the_file.write(cleanCom +'\n')

cleanData = open("cleanData.txt", "r")
cleanData = cleanData.read()

wordcloud = WordCloud(width=1400, height=700).generate(cleanData)
wordcloud.to_file("world cloud.png")