#!/usr/bin/python3
"""unit test for state module
"""
import os
import unittest
from models.engine.File_strg import FileStrg
from models.usr import Usr
from models import strg
from datetime import datetime

class TestState(unittest.TestCase):
    """Test cases for the 'Usr' class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStrg data"""
        FileStrg._FileStrg__objects = {}
        if os.path.exists(FileStrg._FileStrg__file_path):
            os.remove(FileStrg._FileStrg__file_path)

    def test_params(self):
        """Tests the parameters"""
        u1 = Usr()
        j = f"{type(u1).__name__}.{u1.id}"
        self.assertIn(j, storage.all())
        self.assertIsInstance(u1.email, str)
        self.assertIsInstance(u1.password, str)
        self.assertIsInstance(u1.first_name, str)
        self.assertIsInstance(u1.last_name, str)

    def test_init(self):
        """test the method for public instances"""
        u1 = Usr()
        u2 = Usr(**u1.to_dict())
        self.assertIsInstance(u1.id, str)
        self.assertIsInstance(u1.created_at, datetime)
        self.assertIsInstance(u1.updated_at, datetime)
        self.assertEqual(u1.updated_at, u2.updated_at)

    def test_str(self):
        """test method for string representation"""
        u1 = Usr()
        sting = f"[{type(u1).__name__}] ({u1.id}) {u11.__dict__}"
        self.assertEqual(u1.__str__(), sting)

    def test_save(self):
        """test save method"""
        u1 = Usr()
        old_updates = u1.updated_at
        u1.save()
        self.assertNotEqual(u1.updated_at, old_updates)

    def test_todict(self):
        """test mehod for dictionary"""
        u1 = Usr()
        u2 = Usr(**u1.to_dict())
        b_dict = u2.to_dict()
        self.assertIsInstance(b_dict, dict)
        self.assertEqual(b_dict['__class__'], type(u2).__name__)
        self.assertIn('created_at', b_dict.keys())
        self.assertNotEqual(u1, u2)

if __name__ == "__main__":
    unittest.main()
