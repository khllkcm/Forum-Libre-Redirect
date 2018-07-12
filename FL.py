import requests
import re
import os

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"}

response = requests.get(
    "https://reddit.com/r/france/search?sort=new&q=flair%3AForum%2BLibre&restrict_sr=on&t=day",
    headers=headers,
)
result = re.search(
    r"https://www.reddit.com/r/france/comments/?.{6}/forum_libre_20.+?/", str(response.content)
)
if result:
    link = result.group(0)
    os.system(f'echo "Redirect /FL/ {link}?sort=new" > /srv/kacem.xyz/.htaccess')
else:
    os.system("rm /srv/kacem.xyz/.htaccess")
