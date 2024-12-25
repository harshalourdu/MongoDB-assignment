# Q1. What is MongoDB? Explain non-relational databases in short. In which scenarios is it preferred to use MongoDB over SQL databases?

MongoDB is an open-source, NoSQL, document-oriented database that stores data in a flexible, JSON-like format called BSON (Binary JSON). It allows for the storage and retrieval of data without the rigid schema constraints typical of relational databases. MongoDB is highly scalable, supports horizontal scaling through sharding, and provides high performance for large-scale data storage.

Non-relational databases (NoSQL) are databases that do not use the traditional table-based relational model for storing data. They are designed to handle large volumes of unstructured, semi-structured, or rapidly changing data. Common types of NoSQL databases include document databases (like MongoDB), key-value stores, column-family stores, and graph databases.

Scenarios where MongoDB is preferred over SQL databases:

Handling large-scale, unstructured, or semi-structured data: MongoDB is well-suited for applications with dynamic or unstructured data like social media apps, content management systems, and IoT systems.
Horizontal scalability: MongoDB is designed for horizontal scaling, meaning it can scale across multiple servers to handle growing datasets.
Flexible schema: Unlike SQL databases, MongoDB doesn’t require a fixed schema, making it more adaptable to changes in data structure without needing database migrations.
Real-time analytics: MongoDB is ideal for handling real-time data, including rapidly changing data from sources like logs, social media feeds, or sensors.



# Q2. State and explain the features of MongoDB.
MongoDB offers several key features that make it suitable for modern applications:

Document-Oriented: MongoDB stores data as documents (in BSON format), which can be nested and contain arrays, allowing for flexible and hierarchical data representation.

Schema-less: MongoDB does not require a predefined schema, allowing data to be stored in any structure without the need for altering the database schema as the data evolves.

High Performance: MongoDB provides high performance for both reads and writes. It supports indexing and various query types to optimize performance.

Scalability: MongoDB supports horizontal scaling using sharding, where data is distributed across multiple machines, enabling the database to handle large amounts of data and high traffic.

Replication: MongoDB supports replication, ensuring data availability and fault tolerance. With replica sets, multiple copies of data are stored, providing automatic failover if a primary server fails.

Aggregation Framework: MongoDB has a powerful aggregation framework that supports data processing, transformation, and summarization, similar to SQL GROUP BY and JOIN operations.

Flexible Querying: MongoDB allows a rich query language with support for ad-hoc queries, range queries, regular expression searches, and more.

Indexing: MongoDB supports a variety of index types to improve query performance, including compound, geospatial, and text indexes.



# Q3. Write a code to connect MongoDB to Python. Also, create a database and a collection in MongoDB.

import pymongo

# Connect to MongoDB server (localhost by default)
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a new database
db = client["mydatabase"]

# Create a new collection in the database
collection = db["mycollection"]

print("Database and collection created successfully.")



# Q4. Using the database and collection created in question number 3, write a code to insert one record and insert many records. Use the find() and find_one() methods to print the inserted record.

import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Insert one record
collection.insert_one({"name": "Alice", "age": 25})

# Insert many records
collection.insert_many([
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 40}
])

# Find one record
print(collection.find_one({"name": "Alice"}))

# Find all records
for record in collection.find():
    print(record)


# Q5. Explain how you can use the find() method to query the MongoDB database. Write a simple code to demonstrate this.

import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Query to find documents where age is greater than 30
query = {"age": {"$gt": 30}}
for document in collection.find(query):
    print(document)


# Q6. Explain the sort() method. Give an example to demonstrate sorting in MongoDB.

import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Sort documents by age in descending order
for document in collection.find().sort("age", -1):
    print(document)



# Q7. Explain why delete_one(), delete_many(), and drop() are used.


delete_one(): This method is used to delete a single document from a collection that matches the specified query. If multiple documents match the query, only the first one is deleted.

Example:

python

collection.delete_one({"name": "Alice"})
delete_many(): This method is used to delete all documents that match a given query. It removes multiple documents from the collection.

Example:

python

collection.delete_many({"age": {"$gt": 30}})
drop(): This method is used to remove an entire collection from the database, including all the documents and indexes associated with the collection.

Example:

python

collection.drop()
These methods are used for data removal. delete_one() and delete_many() remove specific documents, while drop() removes the entire collection.