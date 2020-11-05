import os 
import unittest 
import json 
import requests
from flask_sqlalchemy import SQLAlchemy 
from app import create_app
from database.models import setup_db, Drink


class CoffeeTestCase(unittest.TestCase): 

    baristajwt = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5nZk04cHNmTUZSNkUtdThheFUwVyJ9.eyJpc3MiOiJodHRwczovL2phY2t3dS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZhMGMzMjYwZDQzMmMwMDZmY2Q5OWFjIiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjA0NjA0NjYzLCJleHAiOjE2MDQ2MTE4NjMsImF6cCI6IlBIVE81YVhMYWVPWk9ZaERFeE9NZEx5Y0hrM3hpd0xIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.oRfcTyDAqzqEJZtRUOJtqKZlkUXvHiPBrY6eI4xCuF9KUpomZqqcbJnW-eY6uMVfB3mrsyOBC6-Ba36tPdQa_33KBVSj7f6-OKOIM-HpKkaiW6p4HnWamw9-Tuko48Iz7WO1tvoPT-py4wdjdEnuKBzyoeD9s2i5lXwdRhrHAfczZEO5Q61jtwRj2JPpa2eagQmzDignfwKynnILqqJyHJACdbKMMf9O0hSTQy3Ka9dHhKrnT8TjNJHO-eNtonos6sBC8fiX-amWiKzVSPo9N3HUUeqd4NUD5o5FuiKgutSa056XZE0BTirL18Q1drX7r5WksuNR2__R9Js3aJEC8Q'


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
            # self.db.drop_all()
            self.db.create_all()

    def tearDown(self): 
        pass 

    #test get drinks success/failure 

    def test_get_drinks(self): 
        response = requests.get('https://coffeeshop-capstone-backend.herokuapp.com/drinks')
        self.assertEqual(response.status_code, 200)

    #test get drinks-detail success/failure 

    def test_get_drinks_detail(self): 
        response = requests.get('https://coffeeshop-capstone-backend.herokuapp.com/drinks-detail', headers={
            "Authorization":"Bearer{}".format(self.baristajwt)
        })
        self.assertEqual(response.status_code, 200)


    #test post drinks success/failure

    
    #test patch drinks/<id> success/failure


    #test delete drinks/<id> success/failure


    #test role based access scenarios 
 

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