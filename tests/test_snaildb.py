import unittest
import tempfile
import json
from snaildb import SnailDB

class TestSnailDB(unittest.TestCase):
    def setUp(self):
        self.db_file = tempfile.NamedTemporaryFile(delete=False).name
        self.db = SnailDB(self.db_file)

    def tearDown(self):
        pass

    def test_insert_single_document(self):
        document = {"_id": 1, "name": "Alice", "age": 30, "city": "Wonderland"}
        document_id = self.db.insert(document)
        self.assertEqual(document_id, 1)

        retrieved_document = self.db.find({"_id": 1})[0]
        self.assertEqual(retrieved_document, document)

    def test_insert_multiple_documents(self):
        documents = [
            {"name": "Bob", "age": 25, "city": "Dreamland"},
            {"name": "Charlie", "age": 28, "city": "Fantasyville"},
        ]
        document_ids = self.db.insert_multiple(documents)
        self.assertEqual(document_ids, [2, 3])

        retrieved_documents = self.db.find({"age": 25})
        self.assertEqual(len(retrieved_documents), 1)
        self.assertEqual(retrieved_documents[0]["name"], "Bob")

    def test_update_document(self):
        document = {"_id": 1, "name": "Alice", "age": 30, "city": "Wonderland"}
        self.db.insert(document)

        update_query = {"name": "Alice"}
        update_fields = {"age": 31, "city": "Updated Wonderland"}
        self.db.update(update_query, update_fields)

        updated_document = self.db.find(update_query)[0]
        self.assertEqual(updated_document["age"], 31)
        self.assertEqual(updated_document["city"], "Updated Wonderland")

    def test_remove_document(self):
        document = {"_id": 1, "name": "Alice", "age": 30, "city": "Wonderland"}
        self.db.insert(document)

        remove_query = {"name": "Alice"}
        self.db.remove(remove_query)

        remaining_documents = self.db.find()
        self.assertEqual(len(remaining_documents), 0)

    def test_create_index_and_find_with_index(self):
        documents = [
            {"name": "Alice", "city": "Wonderland"},
            {"name": "Bob", "city": "Dreamland"},
            {"name": "Charlie", "city": "Fantasyville"},
        ]
        self.db.insert_multiple(documents)

        index_fields = ["name", "city"]
        index_name = "name_city_index"
        self.db.create_index(index_name, index_fields)

        query_values = ["Alice", "Wonderland"]
        found_with_index = self.db.find_with_index(index_name, query_values)
        self.assertEqual(len(found_with_index), 1)
        self.assertEqual(found_with_index[0]["name"], "Alice")

        self.db.remove_index(index_name)

    def test_remove_all_documents(self):
        documents = [
            {"name": "Alice", "age": 30, "city": "Wonderland"},
            {"name": "Bob", "age": 25, "city": "Dreamland"},
        ]
        self.db.insert_multiple(documents)

        self.db.remove_all()

        remaining_documents = self.db.find()
        self.assertEqual(len(remaining_documents), 0)

    def test_query_documents(self):
        documents = [
            {"name": "Alice", "age": 30, "city": "Wonderland"},
            {"name": "Bob", "age": 25, "city": "Dreamland"},
            {"name": "Charlie", "age": 28, "city": "Fantasyville"},
        ]
        self.db.insert_multiple(documents)

        result = self.db.query(lambda doc: doc['name'] == 'Alice')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "Alice")

    def test_match_any_documents(self):
        documents = [
            {"name": "Alice", "age": 30, "city": "Wonderland"},
            {"name": "Bob", "age": 25, "city": "Dreamland"},
            {"name": "Charlie", "age": 28, "city": "Fantasyville"},
        ]
        self.db.insert_multiple(documents)

        query = [("age", ">", 25), ("city", "==", "Fantasyville")]
        result = self.db.match_any(query)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["name"], "Bob")
        self.assertEqual(result[1]["name"], "Charlie")

if __name__ == '__main__':
    unittest.main()
