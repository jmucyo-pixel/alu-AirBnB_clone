import datetime
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_id_is_string(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_created_at_is_datetime(self):
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime.datetime)

    def test_save_updates_updated_at(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict_contains_expected_keys(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIn("__class__", model_dict)