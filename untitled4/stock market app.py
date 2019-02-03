import urllib
url = "https://www.google.com/search?tbm=fin&q="
StockName = str(input("Enter stock name"))
stockSearch = url + StockName
print(stockSearch)
data = urllib.request.urlopen(stockSearch).read()
data1 = data.decode("utf-8")
print(data1)

