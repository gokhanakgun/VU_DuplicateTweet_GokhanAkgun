from pymongo import MongoClient
from VU_DuplicateTweet import deleteDuplicate
connection=MongoClient("mongodb://127.0.0.1:27017")
db=connection.test
deleteDuplicate(db.tweets)
