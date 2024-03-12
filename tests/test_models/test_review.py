#!/usr/bin/python3 

"""Test for the review. 

""" 

import os 

import unittest 

from models.review import Review 

from models import strg 

from datetime import datetime 

from models.engine.file_strg import FileStrg 

  

  

class TestReview(unittest.TestCase): 

    """ Review class Test cases.""" 

  

    def setUp(self): 

        pass 

  

    def tearDown(self) -> None: 

        """Resets FileStrg data.""" 

        FileStrg._FileStrg__objects = {} 

        if os.path.exists(FileStrg._FileStrg__file_path): 

            os.remove(FileStrg._FileStrg__file_path) 

  

    def test_params(self): 

        """ class attributes Test method """ 

  

        R1 = Review() 

        r3 = Review("hello", "wait", "in") 

        K = f"{type(R1).__name__}.{R1.id}" 

        self.assertIsInstance(R1.text, str) 

        self.assertIsInstance(R1.user_id, str) 

        self.assertIsInstance(R1.place_id, str) 

        self.assertEqual(r3.text, "") 

  

    def test_init(self): 

        """Test method for public instances""" 

        R1 = Review() 

        R2 = Review(**R1.to_dict()) 

        self.assertIsInstance(R1.id, str) 

        self.assertIsInstance(R1.created_at, datetime) 

        self.assertIsInstance(R1.updated_at, datetime) 

        self.assertEqual(R1.updated_at, R2.updated_at) 

  

    def test_str(self): 

        """Test method for str representation""" 

        R1 = Review() 

        string = f"[{type(R1).__name__}] ({R1.id}) {R1.__dict__}" 

        self.assertEqual(R1.__str__(), string) 

  

    def test_save(self): 

        """Test method for save""" 

        R1 = Review() 

        old_update = R1.updated_at 

        R1.save() 

        self.assertNotEqual(R1.updated_at, old_update) 

  

    def test_todict(self): 

        """  dictTest method 

""" 

        R1 = Review() 

        R2 = Review(**R1.to_dict()) 

        A_dict = R2.to_dict() 

        self.assertIsInstance(A_dict, dict) 

        self.assertEqual(A_dict['__class__'], type(R2).__name__) 

        self.assertIn('created_at', A_dict.keys()) 

        self.assertIn('updated_at', A_dict.keys()) 

        self.assertNotEqual(R1, R2) 

  

  

if __name__ == "__main__": 

    unittest.main() 
