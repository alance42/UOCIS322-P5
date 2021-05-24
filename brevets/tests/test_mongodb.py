import nose
import logging
import os
from pymongo import MongoClient

TestData = [{'brevetDist':'200','startDate':'2021-01-01T00:00','index':1,'miles':'9.320565','km':'15','startTime':'2021-01-01T00:26','closeTime':'2021-01-01T00:26'},{'brevetDist':'200','startDate':'2021-01-01T00:00','index':2,'miles':'21.747985','km':'35','startTime':'2021-01-01T01:02','closeTime':'2021-01-01T01:02'}]
#https://rusa.org/cgi-bin/octime.pl

def test_mongodb():
	client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
	db = client.test
	db.test.insert(TestData)

	success = db.test.find_one({'km': '36'}) == None
	assert success

	success = db.test.find_one({'km': '35'}) != None
	assert success

	success = db.test.find_one({'km':'15'}) != None
	assert success

	success = db.test.find_one({'closeTime':'2021-01-01T01:02'}) != None
	assert success

	db.test.drop()

	success = db.test.find_one({'brevetDist':'200'}) == None
	assert success

