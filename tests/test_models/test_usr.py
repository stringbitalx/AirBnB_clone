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
        U1 = Usr()
        K = f"{type(u1).__name__}.{u1.id}"
        self.assertIn(K, storage.all())
        self.assertIsInstance(U1.email, str)
        self.assertIsInstance(U1.password, str)
        self.assertIsInstance(U1.first_name, str)
        self.assertIsInstance(U1.last_name, str)

    def test_init(self):
        """test the method for public instances"""
        U1 = Usr()
        U2 = Usr(**u1.to_dict())
        self.assertIsInstance(U1.id, str)
        self.assertIsInstance(U1.created_at, datetime)
        self.assertIsInstance(U1.updated_at, datetime)
        self.assertEqual(U1.updated_at, U2.updated_at)

    def test_str(self):
        """test method for string representation"""
        U1 = Usr()
        sting = f"[{type(U1).__name__}] ({U1.id}) {U1.__dict__}"
        self.assertEqual(U1.__str__(), sting)

    def test_save(self):
        """test save method"""
        U1 = Usr()
        old_updates = U1.updated_at
        U1.save()
        self.assertNotEqual(U1.updated_at, old_updates)

    def test_todict(self):
        """test mehod for dictionary"""
        U1 = Usr()
        U2 = Usr(**U1.to_dict())
        A_dict = U2.to_dict()
        self.assertIsInstance(A_dict, dict)
        self.assertEqual(A_dict['__class__'], type(U2).__name__)
        self.assertIn('created_at', A_dict.keys())
        self.assertNotEqual(U1, U2)

if __name__ == "__main__":
    unittest.main()
