
```markdown
# SnailDB Example Guide

This guide provides examples and use cases for SnailDB, a lightweight, non-SQL database for Python. 

## Table of Contents

1. [Basic Usage](#basic-usage)
2. [Inserting Documents](#inserting-documents)
3. [Querying Data](#querying-data)
4. [Updating Documents](#updating-documents)
5. [Deleting Documents](#deleting-documents)
6. [Advanced Features](#advanced-features)

## Basic Usage

### Creating a SnailDB Instance

```python
from snaildb import SnailDB

# Create a SnailDB instance with a specified database file path and name
db = SnailDB("my_database.json", "data")
```

### Getting the Database Name

```python
# Get the name of the current database
db_name = db.get_db_name()
print("Using database:", db_name)
```

## Inserting Documents

### Inserting a Single Document

```python
# Insert a single document into the database
db.insert({"key": "1", "name": "John", "age": 30})
```

### Inserting Multiple Documents

```python
# Insert multiple documents into the database
db.insert_all(
    {"key": "2", "name": "Alice", "age": 25},
    {"key": "3", "name": "Bob", "age": 35}
)
```

## Querying Data

### Basic Queries

```python
# Query documents where age is greater than 30
result = db.query("age", ">", 30)
print(result)
```

### Advanced Queries

```python
# Query documents where name is "Alice" and age is less than 30
result = db.query("name", "=", "Alice", "age", "<", 30, pretty=True)
print(result)
```

## Updating Documents

```python
# Update the age of a document with key "1"
db.update("1", {"age": 31})
```

## Deleting Documents

### Deleting a Single Document

```python
# Delete a document with key "2"
db.delete("2")
```

### Deleting the Entire Database

```python
# Delete the entire database
db.drop()
```

## Advanced Features

### Customizing SnailDB

```python
# Create a SnailDB instance with a different database file path and name
custom_db = SnailDB("custom_database.json", "custom_data")
```

### Version Information

```python
from snaildb import version

# Print the version of SnailDB
print("SnailDB Version:", version())
```

Feel free to copy and paste these examples into your own code or documentation. Modify them as needed based on your specific use cases and requirements.
```
