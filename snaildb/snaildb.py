# snaildb/snaildb.py
import json
from pathlib import Path
from collections import OrderedDict, abc
from typing import List, Iterator, TypeVar, Generic, Union, Optional, Type, TYPE_CHECKING

K = TypeVar('K')
V = TypeVar('V')
D = TypeVar('D')
T = TypeVar('T')

__all__ = ('LRUCache', 'freeze', 'with_typehint', 'SnailDB')

def with_typehint(baseclass: Type[T]):
    if TYPE_CHECKING:
        return baseclass
    return object

class LRUCache(abc.MutableMapping, Generic[K, V]):
    def __init__(self, capacity=None) -> None:
        self.capacity = capacity
        self.cache: OrderedDict[K, V] = OrderedDict()

    @property
    def lru(self) -> List[K]:
        return list(self.cache.keys())

    @property
    def length(self) -> int:
        return len(self.cache)

    def clear(self) -> None:
        self.cache.clear()

    def __len__(self) -> int:
        return self.length

    def __contains__(self, key: object) -> bool:
        return key in self.cache

    def __setitem__(self, key: K, value: V) -> None:
        self.set(key, value)

    def __delitem__(self, key: K) -> None:
        del self.cache[key]

    def __getitem__(self, key) -> V:
        value = self.get(key)
        if value is None:
            raise KeyError(key)

        return value

    def __iter__(self) -> Iterator[K]:
        return iter(self.cache)

    def get(self, key: K, default: Optional[D] = None) -> Optional[Union[V, D]]:
        value = self.cache.get(key)

        if value is not None:
            self.cache.move_to_end(key, last=True)

            return value

        return default

    def set(self, key: K, value: V):
        if self.cache.get(key):
            self.cache.move_to_end(key, last=True)

        else:
            self.cache[key] = value

            if self.capacity is not None and self.length > self.capacity:
                self.cache.popitem(last=False)

class FrozenDict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))

    def _immutable(self, *args, **kws):
        raise TypeError('object is immutable')

    __setitem__ = _immutable
    __delitem__ = _immutable
    clear = _immutable
    setdefault = _immutable
    popitem = _immutable

    def update(self, e=None, **f):
        raise TypeError('object is immutable')

    def pop(self, k, d=None):
        raise TypeError('object is immutable')

def freeze(obj):
    if isinstance(obj, dict):
        return FrozenDict((k, freeze(v)) for k, v in obj.items())
    elif isinstance(obj, list):
        return tuple(freeze(el) for el in obj)
    elif isinstance(obj, set):
        return frozenset(obj)
    else:
        return obj

class SnailDB:
    default_table_name = 'SnailDB_default'

    def __init__(self, db_file, capacity=None):
        self.db_file = Path(db_file)
        self.tables = self.load_data()  # Load data during initialization
        self.default_table = self.get_table(self.default_table_name)
        self.cache = LRUCache(capacity)

    def get_table(self, table_name):
        if table_name not in self.tables:
            self.tables[table_name] = []
        return self.tables[table_name]

    def load_data(self):
        if not self.db_file.exists():
            return {}
        try:
            with open(self.db_file, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}

    def save_data(self, data):
        try:
            with open(self.db_file, 'w') as file:
                json.dump(data, file, indent=2)
        except IOError as e:
            raise RuntimeError(f"Error saving data to {self.db_file}: {e}")

    def insert(self, document, table_name=None):
        try:
            table = self.get_table(table_name or self.default_table_name)
            table.append(document)
            self.save_data({table_name: table for table_name, table in self.tables.items()})
            self.cache.clear()
            return document.get('_id')
        except Exception as e:
            raise RuntimeError(f"Error inserting document: {e}")

    def insert_multiple(self, documents, table_name=None):
        try:
            table = self.get_table(table_name or self.default_table_name)
            for doc in documents:
                table.append(doc)
            self.save_data({table_name: table for table_name, table in self.tables.items()})
            self.cache.clear()
            return [doc.get('_id') for doc in documents]
        except Exception as e:
            raise RuntimeError(f"Error inserting multiple documents: {e}")

    def get_all(self, table_name=None):
        try:
            table = self.get_table(table_name or self.default_table_name)
            return table
        except Exception as e:
            raise RuntimeError(f"Error retrieving all documents: {e}")

    def find(self, query, table_name=None):
        try:
            table = self.get_table(table_name or self.default_table_name)
            result = [doc for doc in table if all(doc.get(key) == value for key, value in query.items())]
            return result
        except Exception as e:
            raise RuntimeError(f"Error finding documents: {e}")

    def update(self, query, update_fields, multi=False):
        for table_name, table in self.tables.items():
            updated_indices = []
            for i, doc in enumerate(table):
                if all(doc.get(key) == value for key, value in query.items()):
                    print(f"Updating document in table {table_name}: {doc}")
                    updated_indices.append(i)
                    for field, value in update_fields.items():
                        doc[field] = value
                        print(f"Updated field '{field}': {value}")

            if not multi and updated_indices:
                # Break if not updating all documents and at least one is updated
                break

            # Remove the updated documents from the table
            for index in reversed(updated_indices):
                table.pop(index)

            # Append the updated documents back to the end of the table
            for index in updated_indices:
                table.append(table.pop(index))

        self.save_data({table_name: table for table_name, table in self.tables.items()})
        self.cache.clear()

    def remove(self, query=None, multi=False):
        for table_name, table in self.tables.items():
            if query:
                if multi:
                    self.tables[table_name] = [doc for doc in table if not all(doc.get(key) == value for key, value in query.items())]
                else:
                    self.tables[table_name] = [doc for doc in table if not all(doc.get(key) == value for key, value in query.items())][0:1]
            else:
                self.tables[table_name] = []
        self.save_data({table_name: table for table_name, table in self.tables.items()})
        self.cache.clear()

    def create_index(self, index_name, fields, table_name=None):
     table = self.get_table(table_name or self.default_table_name)
     index = {str(tuple(doc.get(field) for field in fields)): doc for doc in table}
     updated_tables = self.tables.copy()
     updated_tables[index_name] = index
     self.save_data(updated_tables)
     self.cache.clear()




    def find_with_index(self, index_name, query_values):
    # Query using an index
     index = self.tables.get(index_name)
     if index:
        key = str(tuple(query_values))
        if key in index:
            return [index[key]]
        else:
            return []
     else:
        raise ValueError(f"Index {index_name} not found.")


    def remove_index(self, index_name):
    # Remove an index
     if index_name in self.tables:
        del self.tables[index_name]
        self.save_data({table_name: table for table_name, table in self.tables.items()})
     else:
        raise ValueError(f"Index {index_name} not found.")



    
    def remove_all(self):
        for table_name, table in self.tables.items():
            self.tables[table_name] = []
        self.save_data({table_name: table for table_name, table in self.tables.items()})
        self.cache.clear()

    def create_query(self, key, operator, value):
        operators_mapping = {
            '==': lambda x, y: x == y,
            '!=': lambda x, y: x != y,
            '>': lambda x, y: x > y,
            '>=': lambda x, y: x >= y,
            '<': lambda x, y: x < y,
            '<=': lambda x, y: x <= y,
        }
        return lambda doc: operators_mapping[operator](doc.get(key), value)

    def match_any(self, query, table_name=None):
        table = self.get_table(table_name or self.default_table_name)
        return [doc for doc in table if any(self.create_query(key, operator, value)(doc) for key, operator, value in query)]

    def query(self, query_func, table_name=None):
        table = self.get_table(table_name or self.default_table_name)
        return [doc for doc in table if query_func(doc)]

    def match_field_exists(self, field):
        return [doc for doc in self.data if field in doc]

    def match_regex(self, field, regex):
        import re
        return [doc for doc in self.data if re.match(regex, doc.get(field, ''))]

    def match_function(self, func):
        return [doc for doc in self.data if func(doc)]

    def match_all_list(self, field, query):
        return [doc for doc in self.data if all(self.create_query(key, operator, value)(doc) for key, operator, value in query)]

    def match_list_membership(self, field, values):
        return [doc for doc in self.data if all(value in doc.get(field, []) for value in values)]

    def match_any_list(self, field, query):
        return [doc for doc in self.data if any(self.create_query(key, operator, value)(doc) for key, operator, value in query)]

    def match_list_membership_any(self, field, values):
        return [doc for doc in self.data if any(value in doc.get(field, []) for value in values)]

    def match_field_in_list(self, field, values):
        return [doc for doc in self.data if doc.get(field) in values]

    def not_match_query(self, query):
        return [doc for doc in self.data if not all(doc.get(key) == value for key, value in query.items())]

    def match_both_queries(self, query1, query2):
        return [doc for doc in self.data if all(doc.get(key) == value for key, value in query1.items())
                and all(doc.get(key) == value for key, value in query2.items())]

    def get_document_count(self):
        return sum(len(table) for table in self.tables.values())

    def get_one_matching_document(self, query):
        try:
            matches = self.find(query)
            return matches[0] if matches else None
        except Exception as e:
            raise RuntimeError(f"Error retrieving matching document: {e}")

    def contains_matching_document(self, query):
        return any(self.find(query))

    def get_matching_document_count(self, query):
        return len(self.find(query))

    def get_document_id(self, document):
        return document.get('_id')

    def get_document_by_id(self, document_id):
        for table in self.tables.values():
            for doc in table:
                if doc.get('_id') == document_id:
                    return doc
        return None

    def contains_document_with_id(self, document_id):
        return any(doc.get('_id') == document_id for table in self.tables.values() for doc in table)





