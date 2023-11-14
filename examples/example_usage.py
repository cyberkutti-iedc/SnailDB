from snaildb import SnailDB


# Create a SnailDB instance
#db = SnailDB('snaildb.json')
#db.insert({'name': 'Sreeraj', 'age': 25, 'city': 'New York'})
# Insert a document
#document_id = db.insert({'name': 'John', 'age': 25, 'city': 'New York'})
#print("Inserted Document ID:", document_id)

# Get all documents
#all_documents = db.get_all()
#print("All Documents:", all_documents)

# Query documents
#query_result = db.find({'name': 'John'})
#print("Query Result:", query_result)

# Update documents
#db.update({'name': 'John'}, {'age': 26})

# Remove documents based on a query
#db.remove({'name': 'John'})

# Remove all documents
#db.remove_all()

# Create a new query object
#query_func = db.create_query('age', '>', 30)
#filtered_documents = [doc for doc in db.get_all() if query_func(doc)]
#print("Filtered Documents:", filtered_documents)

# Match any document with a key field value equal to 2
#match_result = db.match_any([('age', '==', 2)])
#print("Match Result:", match_result)



# Example Usage
#from snaildb import SnailDB
if __name__ == "__main__":
    db = SnailDB('snaildb.json')

    # Insert a document
    db.insert({'name': 'test', 'age': 25, 'city': 'New York'})

    # Get all documents
    all_documents = db.get_all()
    print("All Documents:", all_documents)

    # Query documents
    #query_result = db.find({'name': 'John'})
    #print("Query Result:", query_result)

    # Update documents
    db.update({'name': 'John'}, {'age': 26})

    # Remove documents based on a query
    db.remove({'name': 'John'})

    # Remove all documents
    #db.remove()

    # Create a new query object
   # query_func = db.create_query('age', '>', 30)
    #filtered_documents = [doc for doc in db.get_all() if query_func(doc)]
    #print("Filtered Documents:", filtered_documents)

    # Match any document with a key field value equal to 2
    #match_result = db.match_any([('age', '==', 2)])
    #print("Match Result:", match_result)
