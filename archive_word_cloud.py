#!/usr/bin/env python
import os
import mysql.connector
from wordcloud import WordCloud, STOPWORDS
from dotenv import load_dotenv


load_dotenv()

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password=os.environ.get("db_password"),
  database="archive_no_stopwords"
)
cursor = mydb.cursor()

cursor.execute("""SELECT word, SUM(occurences) as total_occurences 
FROM words
GROUP BY word 
ORDER BY total_occurences
DESC LIMIT 200""")
result = cursor.fetchall()
cursor.close()
mydb.close()

frequencies = {}
for i, row in enumerate(result):
    frequencies[row[0]] = int(row[1])

wordcloud = WordCloud(width=1400, height=700, stopwords=STOPWORDS).generate_from_frequencies(frequencies)
wordcloud.to_file("archiveworldcloud.png")