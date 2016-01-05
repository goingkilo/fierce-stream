from django.db import models


# Create your models here.
class SearsLaptop(models.Model):
	imgurl = models.CharField(max_length=100)
	brand = models.CharField(max_length=100)
	desc = models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	store  = models.CharField(max_length=100)
	partnumber = models.CharField(max_length=100)
	online = models.CharField(max_length=100)

	##[{ 'img':img,'brand':brand,'name':name,'price':price,'partnumber':id,'online':online,'store':store}
	def to_map(self):
		ret = {}
		ret['img'] = self.imgurl
		ret['brand'] = self.brand
		ret['name'] = self.desc
		ret['price'] = self.price
		ret['store'] = self.store
		ret['partnumber'] = self.partnumber
		ret['online'] = self.online
		
		return ret
	
