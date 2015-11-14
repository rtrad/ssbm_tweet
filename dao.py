import config
import pymongo



class MongoDao():

    def __init__(self, mongo_client=None):
        if mongo_client:
            self.db = mongo_client
        else:
            self.db = pymongo.MongoClient(config.DB_URI)[config.DB_NAME][config.DB_COLLECTION]

    def insert(self, content):
        return self.db.find_one_and_replace({'id':content['id']}, content, 
                                            upsert=True)

    def fetch(self, pipeline):
        return self.db.aggregate(pipeline)