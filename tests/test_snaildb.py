from snaildb import SnailDB, version

# Create a SnailDB instance
db = SnailDB("test_database.json", "test_data")

# Display SnailDB version
version()

# Insert data
db.insert({"key": "1", "name": "John", "age": 30})
db.insert({"key": "2", "name": "Alice", "age": 25})

# Get database name
print("Using database:", db.get_db_name())

# Query data
print("Query data where age is greater than 25:")
query_result = db.query("age", ">", 25, pretty=True)
print(query_result)

# Update data
print("Update age for key '1' to 31:")
db.update("1", {"age": 31})

# View updated data
print("View updated data for key '1':")
print(db.get("1", pretty=True))

# Insert multiple documents
db.insert_all(
    {"key": "3", "name": "Bob", "age": 35},
    {"key": "4", "name": "Eve", "age": 28}
)

# View all data
print("View all data:")
print(db.get_all(pretty=True))

# Delete a document
print("Delete document with key '2':")
db.delete("2")

# View all data after deletion
print("View all data after deletion:")
print(db.get_all(pretty=True))

# Delete the entire database
print("Delete the entire database:")
db.drop()

# Attempt to view data after dropping the database
print("Attempt to view data after dropping the database:")
print(db.get_all(pretty=True))
