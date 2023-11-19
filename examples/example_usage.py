from snaildb import SnailDB

db = SnailDB("example_db.json")
# Example 0: Insert a document
document1 = {"_id": "1", "name": "Alice", "age": 30, "city": "Wonderland"}
document_id = db.insert(document1)
print(f"\nDocument ID after insertion: {document_id}")

# Example 1: Insert a document without id
document1 = {"name": "Alice", "age": 30, "city": "Wonderland"}
document_id = db.insert(document1)
print(f"\nDocument ID after insertion: {document_id}")


# Example 2: Insert multiple documents
documents_to_insert = [
    {"name": "Bob", "age": 25, "city": "Dreamland"},
    {"name": "Charlie", "age": 28, "city": "Fantasyville"},
]
documents_ids = db.insert_multiple(documents_to_insert)
print("\nDocument IDs after multiple insertions:", documents_ids)
# Example 3: Get all documents in the default table
all_documents = db.get_all()
print("\nAll Documents:")
print(all_documents)

# Example 4: Find documents based on a query
query = {"city": "Wonderland"}
found_documents = db.find(query)
print("\nFound Documents:")
print(found_documents)

# Example 5: Update documents based on a query
update_query = {"name": "Alice"}
update_fields = {"age": 31, "city": "Updated Wonderland"}
db.update(update_query, update_fields)
updated_document = db.find(update_query)[0]
print("\nUpdated Document:")
print(updated_document)

# Example 6: Remove documents based on a query
remove_query = {"name": "Bob"}
db.remove(remove_query)
print("\nDocuments after removal:")
print(db.get_all())


# Example 7: Create an index for faster querying
index_fields = ["name", "city"]
db.create_index("name_city_index", index_fields)


# Example 8: Find documents using an index
index_query_values = ["Alice", "Updated Wonderland"]
found_with_index = db.find_with_index("name_city_index", index_query_values)
print("\nFound with Index:")
print(found_with_index)

# Example 9: Remove an index
db.remove_index("name_city_index")

# Example 10: Remove all
db.remove_all()
print("\nDocuments after removing all:")
print(db.get_all())
