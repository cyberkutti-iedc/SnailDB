Certainly! Below is an enhanced version of your README.md for SnailDB:

```markdown
# SnailDB

SnailDB is a lightweight, non-SQL database for Python, designed for simplicity and ease of use.

## Table of Contents

- [Installation](#installation)
- [Version](#version)
- [Quick Start](#quick-start)
- [Examples](#examples)
- [Delete](#delete)
- [Query](#query)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

```bash
pip install snailDB
```

## Version

```python
from snaildb import version

# To check which version of SnailDB is installed
print(version())
```

## Quick Start

```python
from snaildb import SnailDB

# Create a SnailDB instance
db = SnailDB("database.json", "data")

# Get the name of the database
print("Using database:", db.get_db_name())

# Insert data
db.insert({"key": "1", "name": "John", "age": 30})
db.insert({"key": "2", "name": "Alice", "age": 25})

# Get data
print("Key '1' data:", db.get("1"))
```

## Examples

```python
# Setup the database on db
db = SnailDB("my_database.json", "data")

# Example 1: Insert a document using insert() function
db.insert({"key": "1", "name": "Akhil", "age": 20})

# Example 2: Insert multiple documents using insert_all() function
db.insert_all({"key": "3", "name": "Jon", "age": 10}, {"key": "4", "name": "Ali", "age": 21})
```

```python
# Example 3: Update the database
# For updating the database, use the key value.
db.update("1", {"name": "John", "age": 31})

# Example 4: View the database
# Print data without pretty formatting:
print(db.get("1"))

# Print data with pretty formatting:
print(db.get("1", pretty=True))
```

```python
# Example 5: View all the database
# Print all data without pretty formatting:
print(db.get_all())

# Print all data with pretty formatting:
print(db.get_all(pretty=True))
```

## Delete

```python
# Example 6: Delete data
# For deleting data, enter the key
db.delete("2")

# Example 7: Delete the entire database
# The db database will be deleted
db.drop()
```

## Query

```python
# Query Function without pretty formatting
test = db.query("age", "<", 30)
print(test)

# Query Function with pretty formatting
test = db.query("age", "<", 30, pretty=True)
print(test)

# We can use all operators

#Greater Operator

test = db.query("age", ">", 30, pretty=True)
print(test)

#Lesser Operator
test = db.query("age", "<", 30, pretty=True)
print(test)

#Equal to operator
test = db.query("name", "=", "Ali", pretty=True)
print(test)

# Lesser and Equal to operator
test = db.query("age", "<=", 29, pretty=True)
print(test)

# Greater and Equal to operator
test = db.query("age", ">=", 29, pretty=True)
print(test)

# Not Equal to operator
test = db.query("age", "!=", 29, pretty=True)
print(test)

# Query Method with Skip Method
test = db.query("age", "<", 30, skip=1, pretty=True)
print(test)

# Query Method with Limt method
test = db.query("age", "<", 30, limt=1, pretty=True)
print(test)

# Query Method with Limt method and skip method
test = db.query("age", "<", 30, skip=1, limt=1, pretty=True)
print(test)
```

## Features

- **Lightweight:** SnailDB is designed to be a lightweight database, providing basic functionalities without unnecessary complexities.
- **Simple API:** The API is easy to use, making it suitable for small to medium-sized projects.
- **Persistent Storage:** Data is stored in a JSON file, ensuring persistence across sessions.
- **Basic CRUD Operations:** SnailDB supports basic Create, Read, Update, and Delete operations.
- **Query Functionality:** Perform simple queries based on field name, operator, and target value.

## Contributing

Contributions are welcome! If you'd like to contribute to SnailDB, please check the [Contributing Guide](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
