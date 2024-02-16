from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://books.toscrape.com/index.html"

#Opening up connection, grabbing the page
uClient = uReq(my_url)

page_html = uClient.read()

#Close the connection
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#Find all containers of class "item-container"
containers = page_soup.findAll("article", {"class":"product_pod"})

for container in containers:
    book_title = container.div.a.img["alt"]

