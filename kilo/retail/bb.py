import urllib
import json
import sys

products = "http://api.remix.bestbuy.com/v1/products(%(SEARCH)s)?show=name,sku&pageSize=100&page=1&apiKey=xsq2hy53xq74mhrrkt7ex6s5&format=json"

a = sys.argv[1]

get = lambda x : urllib.urlopen(x).read()

url = products % {'SEARCH':a}
print url

b = get( url)
print b
c = json.loads(b)
print len(c)

for i in c['products']:
	for j in i.keys():
		print i[j]

