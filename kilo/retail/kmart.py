
import urllib
import json
import sys

query = 'http://api.developer.sears.com/v2.1/products/search/{store}/json/keyword/{keyword}?apikey=LjGNA2aTh0dWGVdGQOGSzIUYS6hAqDnS'

store_lookup = {'K':'Kmart','k':'Kmart','S':'Sears','s':'Sears'}

sears_info = """

Description
	ImageURL : http://c.shld.net/rpx/i/s/i/spin/image/spin_prod_1141003512
	BrandName : HP
	PbType : NONVARIATION
	Name : Stream 11-d010nr 11.6" Notebook with Intel Celeron N2840 Processor & Windows 8.1
	ReviewRating : {u'Rating': u'2', u'NumReview': u'1'}
OtherInfo
	NewBundleExperience : No
	AutomotiveDivision : false
Price
	ShowAKHIMessage : true
	DisplayPrice : 237.29
	ClearanceIndicator : 0
	IsZipCodeRequired : false
	CutPrice : 271.00
SellerInfo
	StoreOrigin : BeachCamera
	SellerCount : 1
Fulfillment
	DefaultFullfillment : VD
Id
	PartNumber : 00350425000P
Availability
	Source : online
	StockIndicator : 1

"""

def get_from_internet( store, keyword):
	url =  query.replace( '{keyword}', keyword)
	url =  url.replace( '{store}', store)
	#print url

	a = urllib.urlopen( url )
	b = a.read()
	a.close()

	c = json.loads(b)
	products = c['SearchResults']['Products']

	ret = []
	for i in products:
		try:
			desc= i['Description']
			img = desc['ImageURL']
			brand = desc['BrandName']
			name = desc['Name']
			name = ' '.join( name.split('/'))
			a = name.split()
                        if a[0].lower() == a[1].lower() and a[0].lower() in ['hp','lenovo','dell']:
                                a.pop(0)
                                name = ' '.join(a)
                                print 'doing hte duplicate destroy'
			price = i['Price']['DisplayPrice']
			id = i['Id']['PartNumber']
			online = i['Availability']['Source']
			store = i['SellerInfo']['StoreOrigin']
		except:
			pass

		ret.append({ 'img':img,'brand':brand,'name':name,'price':price,'partnumber':id,'online':online,'store':store})
	return ret
		
cell1 = """
	<div class="ad">
		<div class="left">
 			<div class='brand-name'>
                       		%(brand)s
			</div>
			<div>
                       		<span>%(store)s</span>
                        </div>
                       	<div class='price'>
                       		<a href='%(cjpn)s' id='%(uniqid)s' target="_blank">
                              		<button type="button" data-toggle="tooltip" title="Buy from Sears.com">$%(price)s</button>
                               </a>
                        </div>
                        <div>
				<a href='%(cjpn)s' target="_blank">
					       <img src="%(link)s"/>
				</a>
                        </div>
                        <div>
		</div>
		<div>
                        <div class='title'>
                                %(name)s
                        </div>
			
		</div>
	</div>
"""

cell0 = """
	<div class='cell'>
		<div id='unit'>
			<div class='brand'>
				<div class='brand-name'>
					%(brand)s
				</div>
			</div>
			<a href='%(cjpn)s' target="_blank">
					<img src="%(link)s"/>
			</a>
			<div class='title'> 
				%(name)s
			</div>
			<div>
				<span class="label label-success">%(store)s</span>
			</div>
			<div>
				<div class='price'>
					<a href='%(cjpn)s' id='%(uniqid)s' target="_blank">
						<button type="button" data-toggle="tooltip" title="Buy from kmart.com"
							 class="btn btn-warning btn-sm">$%(price)s 
						</button>
					</a>
				</div>
			</div>
		</div>
	</div>
"""
cell = """
	<div class='cell'>
		<div id='unit'>
			<a href='%(cjpn)s' target="_blank">
				<img src="%(link)s"/>
			</a>
			<div class='title'>%(name)s</div>
		</div>
		<div class='brand'>%(brand)s</div>
		<div class='price'>$%(price)s</div>
	</div>
"""
#<span style="background:orange;color:blue;font-size:18pt;font-family:Arial;">BUY</span>

def get_store_name(x):
	if store_lookup.has_key(x):
		return store_lookup[x]
	else:
		return x

def get_cells( f, sears_laptop_objects):
	cell = f
	ret = []
	for x in range( len( sears_laptop_objects)):
		i  = sears_laptop_objects[x]

		url = """http://www.jdoqocy.com/click-%(pid)s-11515703?url=http://www.kmart.com/s/p-%(partnumber)s"""
		url = url % { 'pid': '7904552', 'partnumber':i['partnumber']}

		i['cjpn'] = url
		i['link'] = i['img']
		i['uniqid'] = i['partnumber']
			
		
		a = cell % i

		ret.append(a)
	return ret
		
row = """
<div class="row"> 
	col 
</div>
"""

col = """
<div class="col-md-3 a2">  data
</div>
"""

def make_rows(cells):
	ret = []
	count = 0 
	for i in range(len(cells)/4):
		cols = ''
		for j in range(4):
			a = cells.pop()
			cols += col.replace('data',a)
		ret.append( row.replace('col', cols))
	
	cols = ''
	for i in cells:
		cols += col.replace('data',i)
	ret.append( row.replace('col',cols))
	return ret

def pp(x):
	import json
	a = json.loads(x)
	print json.dumps(a)

