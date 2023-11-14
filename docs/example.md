
```markdown
# SnailDB Examples

Explore practical examples of using SnailDB in various scenarios.

## Table of Contents

1. [Inserting and Querying](#1-inserting-and-querying)
2. [Indexing and Querying with Index](#2-indexing-and-querying-with-index)

## 1. Inserting and Querying

### Example:

```python
from snaildb import SnailDB

# Create a SnailDB instance
db = SnailDB('my_database.json')

# Insert a document
document = {'_id': 1, 'name': 'Alice'}
db.insert(document)

# Query documents
result = db.query(lambda doc: doc['name'] == 'Alice')
print(result)
```

## 2. Indexing and Querying with Index

### Example:

```python
from snaildb import SnailDB

# Create a SnailDB instance
db = SnailDB('my_database.json')

# Create an index for a field in a table
db.create_index('my_table', 'my_field')

# Query using the index
result = db.query_with_index('my_table', 'my_field', 'desired_value')
print(result)
```
