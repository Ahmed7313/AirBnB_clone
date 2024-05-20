#!/usr/bin/python3
"""
Unittests for FileStorage class
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()

    def test_save(self):
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key].id, self.model.id)

    def test_all(self):
        self.storage.new(self.model)
        all_objs = self.storage.all()
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.assertIn(key, all_objs)

    def test_new(self):
        key = "{}.{}".format(self.model.__class__.__name__, self.model.id)
        self.storage.new(self.model)
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
