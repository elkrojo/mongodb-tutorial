import pymongo
import os
if os.path.exists("env.py"):
    import env

MONGODB_URI = os.environ.get("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

print(MONGODB_URI)


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to mongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

# new_doc = {'first': 'chuck', 'last': 'palahniuk', 'dob': '21/02/1962', 'hair_colour': 'brown', 'occupation': 'writer', 'nationality': 'american'}
# coll.insert_one(new_doc)

# new_docs = [{'first': 'kevin', 'last': 'barry', 'dob': '09/01/1970', 'hair_colour': 'brown', 'occupation': 'writer', 'nationality': 'irish'},
#             {'first': 'jamil', 'last': 'zainasheff', 'dob': '19/04/1975', 'hair_colour': 'brown', 'occupation': 'writer', 'nationality': 'american'}]

# coll.insert_many(new_docs)
# documents = coll.find({'first': 'chuck'})
# coll.remove({'first': 'martha'})
coll.update_many({'nationality': 'american'},
                 {'$set': {'hair_colour': 'maroon'}})
documents = coll.find({'nationality': 'american'})
# documents = coll.find()

for doc in documents:
    print(doc)
