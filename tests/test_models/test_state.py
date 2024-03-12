#!/usr/bin/python3
"""unit test for state module
"""
import os
import unittest
from models.engine.File_strg import FileStrg
from models.state import State
from models import strg
from datetime import datetime

class TestState(unittest.TestCase):
    """Test cases for the 'state' class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStrg data"""
        FileStrg._FileStrg__objects = {}
        if os.path.exists(FileStrg._FileStrg__file_path):
            os.remove(FileStrg._FileStrg__file_path)

    def test_params(self):
        """Tests the parameters"""
        S1 = State()
        S3 = State("hello", "wait", "in")
        K = f"{type(S1).__name__}.{S1.id}"
        self.assertIsInstance(S1.name, str)
        self.assertEqual(S3.name, "")
        S1.name = "Chicago"
        self.assertEqual(S1.name, "Chicago")
        self.assertIn(K, storage.all())

    def test_init(self):
        """test the method for public instances"""
        S1 =State()
        S2 = State(**S1.to_dict())
        self.assertIsInstance(S1.id, str)
        self.assertIsInstance(S1.created_at, datetime)
        self.assertIsInstance(S1.updated_at, datetime)
        self.assertEqual(S1.updated_at, S2.updated_at)

    def test_str(self):
        """test method for string representation"""
        S1 = State()
        sting = f"[{type(S1).__name__}] ({S1.id}) {S1.__dict__}"
        self.assertEqual(S1.__str__(), sting)

    def test_save(self):
        """test save method"""
        S1 = State()
        old_updates = S1.updated_at
        S1.save()
        self.assertNotEqual(S1.updated_at, old_updates)

    def test_todict(self):
        """test mehod for dictionary"""
        S1 = State()
        S2 = State(**S1.to_dict())
        A_dict = S2.to_dict()
        self.assertIsInstance(A_dict, dict)
        self.assertEqual(A_dict['__class__'], type(S2).__name__)
        self.assertIn('created_at', A_dict.keys())
        self.assertNotEqual(S1, S2)

if __name__ == "__main__":
    unittest.main()
