import nose
import logging
import os
from pymongo import MongoClient

#https://rusa.org/cgi-bin/octime.pl

def test_mongodb():
	client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
	db = client.brevetsdb