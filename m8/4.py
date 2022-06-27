from bs4 import BeautifulSoup

html = open('index.html')
soup = BeautifulSoup( html, 'html.parser')

print("Title of html document:",soup.find("title").get_text())
