"""Web scraper practice"""

from urllib.request import urlopen
import requests
import re

url = "https://wcvaughan.github.io/wdd130/wwr/"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text

    color_regex = re.compile(r'#(?:[0-9a-fA-F]{3}){1,2}\b')

    color_matches = color_regex.findall(html_content)

    color_list = []

    for color_match in color_matches:
        color_list.append(color_match)

    print(color_list)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")