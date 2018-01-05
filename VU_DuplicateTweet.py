def deleteDuplicate(tweets):
    cursor = tweets.aggregate(
        [
            {"$group": {"_id": "$id", "unique_ids": {"$addToSet": "$_id"}, "count": {"$sum": 1}}},
            {"$match": {"count": { "$gte": 2 }}}
        ],
        allowDiskUse=True
        
    )

    response = []
    for doc in cursor:
        del doc["unique_ids"][0]
        for id in doc["unique_ids"]:
            response.append(id)

    tweets.remove({"_id": {"$in": response}})
    return tweets
