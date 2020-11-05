import os 
import unittest 
import json 
from flask_sqlalchemy import SQLAlchemy 
from app import create_app
from database.models import setup_db, Drink

class CoffeeTestCase(unittest.TestCase): 
    def setUp(self): 
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = "postgres://hydbwdomdwndwi:e2d2c8e8d4967c4c5a2cd01743261b5a5a79eb3f4cd7dc3c772f233b0089ba65@ec2-75-101-232-85.compute-1.amazonaws.com:5432/d20253rlm2pbua"
        setup_db(self.app)

        self.sample_drink = {
            'title': 'test', 
            'recipe': 'test'
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self): 
        pass 

    def test_get_drinks(self): 
        response = self.client().get('/drinks')
        self.assertEqual(response.status_code, 200)

    # def test_get_drinks_detail(self): 
    #     response = self.client().get('/drinks-detail')
    #     self.assertEqual(response.status_code, 200)

    # def test_post_drink(self): 
    #     drinks_before = Drink.query.all()
    #     response = self.client().post('/drinks', json=self.sample_drink)
    #     drinks_after = Drink.query.all()
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(drinks_before)+1, len(drinks_after))



if __name__ == "__main__": 
    unittest.main()