# WordCloud
Some scripts that create world clouds

## worldCloud.py
Generates a world cloud from an <strong>active</strong> 4chan /mu/ thread.

Usage:
```
chmod +x wordCloud.py # only have to do this once
./wordCloud.py <thread id>
```

## worldCloud2.py
Generates a world cloud from raw 4chan comments put into a txt file called 'data'. It also cleans the data and places it into a txt file called 'cleanData'.

Usage:
```
chmod +x wordCloud2.py # only have to do this once
./wordCloud2.py
```

## archive_word_cloud
Generates a world cloud from database data generated from the kpg miner.

Usage:
```
chmod +x archive_word_cloud.py # only have to do this once
./archive_word_cloud.py
```