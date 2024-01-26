from snaildb.snaildb import SnailDB


# Example usage:
db = SnailDB("my_database.json","data")
print(db.get_db_name())
#db.drop()
# Insert data
#db.insert({"key":"1","name": "John", "age": 30})
#db.insert({"key":"2","name": "Alice", "age": 25})

#db.insert_all({"key":"3","name": "Jon", "age": 10},{"key":"4","name": "Ali", "age": 21})

# Update data
#db.update("1", {"name": "John", "age": 31})

# Get data#
#print("Key '1' data:", db.get("1"))

# Get all data
#print("All data:", db.get_all())

# Delete data
#db.delete("2")

# Get all data after deletion
#print("All data after deletion:", db.get_all())

#print("get data with pretty formatting:")
#print(db.get("1",pretty=True))


#print("get all data with pretty formatting:")
#print(db.get_all(pretty=True))

test=db.query("age","<",30,skip=1,limt=1,pretty=True)
print(test)

