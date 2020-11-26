from pymongo import MongoClient
import pymongo
from PIL import Image
import io
import base64
class myMongo(object):

    conn = MongoClient(host='127.0.0.1',port=27017,username='admin',password='123456')
    db = conn['gameInfo']
    
    @classmethod
    def get_state(cls):
        return cls.conn is not None and cls.db is not None    
    
    @classmethod
    def insertOne(cls, collection, data):
        if cls.get_state():
            cls.db[collection].insert_one(data)
        else:
            return ""
    
    @classmethod
    def insertMany(cls, collection, data):
        if cls.get_state():
            cls.db[collection].insert_many(data)
        else:
            return ""

    @classmethod
    def findOne(cls, collection):
        if cls.get_state():
            return cls.db[collection].find_one()
        else:
            return ""
    
    @classmethod
    def findAll(cls, collection):
        if cls.get_state():
           return cls.db[collection].find().sort('id',pymongo.DESCENDING)
        else:
            return ""

    @classmethod
    def findMany(cls,collection,page):
        if cls.get_state():
            return cls.db[collection].find().sort('id',pymongo.DESCENDING).skip(12*(page-1)).limit(12)
        else:
            return ""

