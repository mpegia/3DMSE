import numpy as np
from utils import getResultsNum
from mongo_funcs import connect_mongo, disconnect_mongo


def test_model(image_id, collection, collectionName, resultsNum):
    # Define the fields you want to extract
    selected_fields = {"file_name": 1, "metadata": 1}

    # Query the collection and extract the selected fields
    records = collection.find({}, selected_fields)
    filenames_all = []
    ft_all = []
    for record in records:
        filenames_all.append(record["file_name"])
        # print(record["file_name"])
        # ft_all.append(np.array(record["metadata"]["mesh_feature"]))
        ft_all.append(np.array(record["metadata"]["mesh_hash_code"]))
    ft_all = np.array(ft_all)

    query = {"file_name": image_id}
    projection = {"metadata": 1}
    records1 = collection.find(query, projection)
    ft_query = []
    for record in records1:
        # ft_query.append(np.array(record["metadata"]["mesh_feature"]))
        ft_query.append(np.array(record["metadata"]["mesh_hash_code"]))
    ft_query = np.array(ft_query)

    tot, out = getResultsNum(ft_query, ft_all, 
    filenames_all, resultsNum)
    # foo(collectionName, image_id, out)

    return tot, out


def test(image_id, collection, collectionName, resultsNum):
    query = {"file_name": image_id}
    projection = {"metadata": 1, 'category_id': 1}
    records1 = collection.find(query, projection)
    ft_query = []
    for record in records1:
        # ft_query.append(np.array(record["metadata"]["mesh_feature"]))
        ft_query.append(np.array(record["metadata"]["mesh_hash_code"]))
        category_id = record["category_id"]
    ft_query = np.array(ft_query)
    
    # Query the collection and extract the selected fields
    # Define the fields you want to extract
    # Define the fields you want to extract
    selected_fields = {"file_name": 1, "metadata": 1, "category_id": 1}
    # Filter documents where "category_id" is in the specified values
    query = {"file_name": {"$ne": image_id}, "category_id": {"$in": [category_id, category_id+1]}}    
    records = collection.find(query, selected_fields)
    filenames_all = []
    ft_all = []
    for record in records:
        filenames_all.append(record["file_name"])
        # print(record["file_name"])
        # ft_all.append(np.array(record["metadata"]["mesh_feature"]))
        ft_all.append(np.array(record["metadata"]["mesh_hash_code"]))
    ft_all = np.array(ft_all)

    tot, out = getResultsNum(ft_query, ft_all, filenames_all, resultsNum)
    # foo(collectionName, image_id, out)

    return tot, out


def searchBy3DMeshQuery(image_id, collectionName, resultsNum):
    # Connect to Mongo
    client, database = connect_mongo()
    collection = database[collectionName]
    print(client)
    print(database)

    # Query to Mongo. Find resultsNum relevant to query documents
    tot, results = test(image_id, collection, collectionName, resultsNum)

    # Diconnect Mongo
    disconnect_mongo(client)

    return results


if __name__ == '__main__':
    queryId = 'xbox_0094'
    collection = 'ModelNet40'
    resultsNum = 100
    results = searchBy3DMeshQuery(queryId, collection, resultsNum)
