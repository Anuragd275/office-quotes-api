# Import necessary libraries and functions
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://admin:root-admin@first.cndzcil.mongodb.net/?retryWrites=true&w=majority")

# Select Database
db = client.get_database('first')

#Select collection
collection = db.office_quotes

def quote_fetcher():
    # Fetch quotes from MongoDB
    quotes = collection.find({},{
        'quote': 1,
        'author':1
    })
    return(list(quotes))
