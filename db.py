import pymongo
client = pymongo.MongoClient("mongodb+srv://eagle:LSfqsSNLjEtPE2Hm@cluster0.fhsrc.mongodb.net")
db = client['algorithmnet']
User = db['User']
data = db['data']
users_api = db['users_api']