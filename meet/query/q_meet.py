#coding:utf-8

from meet.lib.query_base import *
from meet.models import *
class QueryMeet(QueryBase):
	def __init__(self):
		super(QueryMeet,self).__init__(Meet)
	#用于封面展示的数据
	def _PackDict(self,query_get):
		return {
            "meet_id":query_get.id,
            "meet_name": query_get.name,
            "des": query_get.des,
            "status": query_get.status,
            "serial": query_get.serial,
            "address": query_get.address,
            "latitude": query_get.latitude,
            "longitude": query_get.longitude,
		}

if __name__ == "__main__":
	a = QueryMeet()
	print a.Filter()