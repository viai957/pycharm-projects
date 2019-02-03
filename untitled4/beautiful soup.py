
html_doc = """
<html><head><title>The DOrmouse's story</title></head>
<body>
<p class = "title"><b>the Dormous's story</b><p>
<p class = 'story">Once upon a time there were three little sisters; and their names were
<a herf = "http://example.com/elsie" class="sister" id="link1">elsie</a>
<a herf = "http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a herf = 'http://example.com/elsie" class='sister" id="link3">Tillie</a>
and they lived at the bottom of a well.</p>

<p class= "story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,"html.parser")
print(soup)
print(soup.prettify())
print(soup.title)
#to  get boald tags
soup.body.b
soup.body.a
soup.find_all("a")
array =[0]
array =[1]
soup.body.b

soup.body.a
soup.find_all("a")
array = [0]
array = [1]
array = [2]







