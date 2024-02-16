from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import re

# Replace 'your_url_here' with the actual URL of the web page you want to analyze
url = 'https://wcvaughan.github.io/wdd130/'

# Fetch the HTML content of the webpage
response = uReq(url)
html_content = response.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all style tags in the HTML
style_tags = soup.find_all('style')

# Extract CSS from style tags
css_content = ''
for style_tag in style_tags:
    css_content += style_tag.get_text()

# Use regex to find color values in the CSS content
color_names = re.findall(r'color:\s*(.*?);', css_content)

# Print the color names
print(color_names)