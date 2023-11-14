# tests/test_snaildb.py
import unittest
from snaildb import SnailDB


class TestSnailDB(unittest.TestCase):
    def setUp(self):
        # Set up a test database
        self.db_file = 'test_db.json'
        self.db = SnailDB(self.db_file)

    def tearDown(self):
        # Remove the test database after the tests
        self.db.remove_all()

    def test_insert_document(self):
        document_id = self.db.insert({'name': 'John'})
        self.assertEqual(self.db.get_document_count(), 1)
        self.assertTrue(self.db.contains_document_with_id(document_id))

    def test_insert_multiple_documents(self):
        documents = [{'name': 'John'}, {'name': 'Jane'}]
        document_ids = self.db.insert_multiple(documents)
        self.assertEqual(self.db.get_document_count(), 2)
        self.assertTrue(all(self.db.contains_document_with_id(doc_id) for doc_id in document_ids))

    def test_get_all_documents(self):
        documents = [{'name': 'John'}, {'name': 'Jane'}]
        self.db.insert_multiple(documents)
        all_documents = self.db.get_all()
        self.assertEqual(len(all_documents), 2)

    def test_find_documents(self):
        documents = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}]
        self.db.insert_multiple(documents)
        found_documents = self.db.find({'age': 25})
        self.assertEqual(len(found_documents), 1)
        self.assertEqual(found_documents[0]['name'], 'John')

    def test_remove_document(self):
        document_id = self.db.insert({'name': 'John'})
        self.assertEqual(self.db.get_document_count(), 1)

        # Remove the document by ID
        self.db.remove({'_id': document_id})
        self.assertEqual(self.db.get_document_count(), 0)
        self.assertFalse(self.db.contains_document_with_id(document_id))

    # Modify the test_update_document test case in test_snaildb.py

def test_update_document(self):
    document_id = self.db.insert({'name': 'John', 'age': 25, 'city': 'New York'})
    
    # Update the document
    self.db.update({'_id': document_id}, {'name': 'update', 'age': 30})

    # Retrieve the updated document
    updated_document = self.db.find({'_id': document_id})[0]

    # Check if the 'name' field is updated
    self.assertEqual(updated_document['name'], 'update')
    
    # Check if other fields are updated as expected
    self.assertEqual(updated_document['age'], 30)
    self.assertEqual(updated_document['city'], 'New York')



if __name__ == '__main__':
    unittest.main()
