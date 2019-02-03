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
soup
body_tag = soup.body
head_tag = soup.head

head_tag

for i in body_tag.children:
    print(i)

for i in body_tag.desendence:
        print(i)

#.parent
#.desecndent

head_tag = soup.title
head_tag.title = soup.title
head_tag

head_tag = soup.head
head_tag.title
head_tag.title.string
head_tag
head_tag.string
head_tag.title.parent
soup.parent
BeautifulSoup.parent

head_tag = soup.head
head_tag.title
head_tag.title.string
head_tag

