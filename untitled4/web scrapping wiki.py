import urllib5
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urllib5.connection_from_url(wiki)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page)

