"""Web scraper practice"""

from urllib.request import urlopen
import requests
import re

url = "https://wcvaughan.github.io/wdd130/wwr/"
response = requests.get(url)

if response.status_code == 200:
    
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")