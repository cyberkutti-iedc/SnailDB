from snaildb import SnailDB

# Create a SnailDB instance with a file named 'example_db.json'
db = SnailDB('example_db.json')

# Insert a document into the default table
document_id = db.insert({'name': 'John', 'age': 25, 'city': 'New York'})
print(f"Inserted document with ID: {document_id}")

# Insert multiple documents into the default table
documents = [
    {'name': 'Alice', 'age': 30, 'city': 'London'},
    {'name': 'Bob', 'age': 28, 'city': 'Paris'},
]
document_ids = db.insert_multiple(documents)
print(f"Inserted multiple documents with IDs: {document_ids}")

# Retrieve all documents from the default table
all_documents = db.get_all()
print(f"All documents in the default table: {all_documents}")

# Find documents with a specific query
query = {'name': 'John', 'age': 25}
found_documents = db.find(query)
print(f"Found documents with query {query}: {found_documents}")

# Update a document with a specific ID
update_query = {'_id': document_id}
update_fields = {'name': 'Updated John', 'age': 26}
db.update(update_query, update_fields)
updated_document = db.find(update_query)[0]
print(f"Updated document: {updated_document}")

# Remove a document with a specific query
remove_query = {'name': 'Updated John', 'age': 26}
db.remove(remove_query)
print(f"Documents after removal: {db.get_all()}")

# Remove all documents from the default table
db.remove_all()
print(f"Documents after removing all: {db.get_all()}")
