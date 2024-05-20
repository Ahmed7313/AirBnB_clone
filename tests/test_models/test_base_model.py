#!/usr/bin/python3
"""
Unittest module for BaseModel class
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class."""

    def test_id_is_unique(self):
        """Test that id is a unique string."""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)
        self.assertIsInstance(model1.id, str)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object."""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object."""
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_method(self):
        """Test the __str__ method."""
        model = BaseModel()
        self.assertIn(f"[{model.__class__.__name__}] ({model.id})", str(model))

    def test_save_method(self):
        """Test the save method."""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertEqual(
            model_dict['created_at'],
            model.created_at.isoformat()
        )
        self.assertEqual(
            model_dict['updated_at'],
            model.updated_at.isoformat()
        )


if __name__ == '__main__':
    unittest.main()
