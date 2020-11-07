import os 
import unittest 
import json 
import requests
import random
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy 
from app import create_app
from database.models import setup_db, Drink


class CoffeeTestCase(unittest.TestCase): 

    baristajwt = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5nZk04cHNmTUZSNkUtdThheFUwVyJ9.eyJpc3MiOiJodHRwczovL2phY2t3dS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZhMGMzMjYwZDQzMmMwMDZmY2Q5OWFjIiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjA0NzEzNTkzLCJleHAiOjE2MDQ3MjA3OTMsImF6cCI6IlBIVE81YVhMYWVPWk9ZaERFeE9NZEx5Y0hrM3hpd0xIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.SHao9oG7gyLOY_Gz_li-whdMCMgUNNYkowV2XyCWCak4TkbA-3tuQ0A5m8OMzAJzV3Gpd5xsqtJ5dm5por61TOMtuaPQN5pAjm4tdOsx09KDbey6MPPoy9okgP1ofkWs4H5PvQyFAWw0tO_Qg07nkg6uUcE2LJ8lNTZRp5_T0O47trCdpfSNQgP5Hwtu8-mIRi_ifMXW81yeFAiaJLSsgjd35AbMbIwDI0GhrNHyB9Rs5UYAgwpt3zByEV4e2V4XIO4g95vnrbxHZnEhRgMSTNAmdN_bU_wUijKJfcKa3XZWAbz014Bs6-6fTfrQXJsPVOSuHLYdRpclpEfS5IQyvQ"
    managerjwt = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5nZk04cHNmTUZSNkUtdThheFUwVyJ9.eyJpc3MiOiJodHRwczovL2phY2t3dS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZhMGMyZmJiZjIyZWMwMDZiNDZmNzM5IiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjA0NzEzNTQ0LCJleHAiOjE2MDQ3MjA3NDQsImF6cCI6IlBIVE81YVhMYWVPWk9ZaERFeE9NZEx5Y0hrM3hpd0xIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.YVwlWpxHyvvEZucXw0_Yf9y-yhTy-bMB5kkVd2pMfHCa8rVl6TgqgYgEVMqKvXrtffsMnaEdLoZ-HG0h6Z8PHpnzvEcr18iueFUd33vjPKjbZuh57sXU8IrYTnJz0m6DBrRE9fGYe7iPsdr9ovGKEfwYF8aGxoy-3HIgiiRZIhJUFi1LZRATYdaYKG2lzYu9AE37aCWMku3rudaaW7aekefbB3ZXhaPLUV15uHjbBvvQs14Wr5Npf1vsx67d3bvz2toMWahslwT6OedvkqQDzXQ63G4SdIxqvWWNHSUxV7Ddo7a22Xa84wo7PD-aF2kXl3VZjdvNlJx6J4NUKWKfOQ"
    sample_drink = {
        "title":"sample title",
        "recipe":[{
            "color": "black",
            "name": "sample ingredient",
            "parts": 1
        }]
    }


    def setUp(self): 
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = "postgres://hydbwdomdwndwi:e2d2c8e8d4967c4c5a2cd01743261b5a5a79eb3f4cd7dc3c772f233b0089ba65@ec2-75-101-232-85.compute-1.amazonaws.com:5432/d20253rlm2pbua"
        setup_db(self.app)


        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # self.db.drop_all()
            self.db.create_all()

    def tearDown(self): 
        pass 


    def test_get_drinks(self): 
        response = requests.get('https://coffeeshop-capstone-backend.herokuapp.com/drinks')
        self.assertEqual(response.status_code, 200)

    def test_get_drinks_failure(self): 
        response = requests.get('https://coffeeshop-capstone-backend.herokuapp.com/drink')
        self.assertEqual(response.status_code, 404)

    def test_get_drinks_detail(self): 
        response = requests.get('https://coffeeshop-capstone-backend.herokuapp.com/drinks-detail', headers={
            "Authorization":"Bearer {}".format(self.baristajwt)
        })
        self.assertEqual(response.status_code, 200)

    def test_get_drinks_detail_failure(self): 
        response = requests.get('https://coffeeshop-capstone-backend.herokuapp.com/drinks-detail')
        self.assertEqual(response.status_code, 401)

    def test_post_drinks(self):
        # self.sample_drink['title'] += str(random.randint(10, 1000))       

        response = requests.post('https://coffeeshop-capstone-backend.herokuapp.com/drinks', json={
            "title": self.sample_drink['title'] + str(random.randint(10, 1000)),
            "recipe": self.sample_drink['recipe']
        }, headers={
            "Authorization":"Bearer {}".format(self.managerjwt)
        })
        self.assertEqual(response.status_code, 200)


    def test_post_drinks_failure(self):
        response = requests.post('https://coffeeshop-capstone-backend.herokuapp.com/drinks', json=self.sample_drink)
        self.assertEqual(response.status_code, 401)

    

    def test_patch_drinks(self): 
        # response = requests.patch('https://coffeeshop-capstone-backend.herokuapp.com/drinks/1', json=self.sample_drink, headers={
        #     "Authorization":"Bearer {}".format(self.managerjwt)
        # })
        # self.assertEqual(response.status_code, 200)
        # add a new drink 
        # self.sample_drink["title"] += str(random.randint(10, 1000))
        d = Drink(
            title = self.sample_drink["title"] + str(random.randint(10, 1000)),
            recipe = json.dumps(self.sample_drink["recipe"])
        )
        d.insert()
        #delete drink 
        d_id = d.id 

        patched_drink = {
            "title":"patched drink",
            "recipe":[{
                "color": "black",
                "name": "sample ingredient",
                "parts": 1
            }]
        }

        response = requests.patch('https://coffeeshop-capstone-backend.herokuapp.com/drinks/{}'.format(d_id), json=patched_drink,headers={
            "Authorization":"Bearer {}".format(self.managerjwt)
        })
        self.assertEqual(response.status_code, 200)


    def test_patch_drinks_failure(self): 
        response = requests.patch('https://coffeeshop-capstone-backend.herokuapp.com/drinks/1')
        self.assertEqual(response.status_code, 401)


    def test_delete_drink(self): 
        #add a new drink 
        self.sample_drink['title'] += str(random.randint(10, 1000))
        d = Drink(
            title = self.sample_drink['title'],
            recipe = str(self.sample_drink['recipe'])
        )
        d.insert()
        #delete drink 
        d_id = d.id 
        response = requests.delete('https://coffeeshop-capstone-backend.herokuapp.com/drinks/{}'.format(d_id), headers={
            "Authorization":"Bearer {}".format(self.managerjwt)
        })
        self.assertEqual(response.status_code, 200)

    def test_delete_drink_failure(self): 
        response = requests.delete('https://coffeeshop-capstone-backend.herokuapp.com/drinks/9999', headers={
            "Authorization":"Bearer {}".format(self.managerjwt)
        })
        self.assertEqual(response.status_code, 404)


    def test_barista(self): 
        response = requests.get('https://coffeeshop-capstone-backend.herokuapp.com/drinks-detail', headers={
            "Authorization":"Bearer {}".format(self.baristajwt)
        })
        self.assertNotEqual(response.status_code, 401)

    def test_manager(self): 
        response = requests.get('https://coffeeshop-capstone-backend.herokuapp.com/drinks-detail', headers={
            "Authorization":"Bearer {}".format(self.managerjwt)
        })
        self.assertNotEqual(response.status_code, 401)
        response = requests.delete('https://coffeeshop-capstone-backend.herokuapp.com/drinks/9999', headers={
            "Authorization":"Bearer {}".format(self.managerjwt)
        })
        self.assertNotEqual(response.status_code, 401)
        response = requests.post('https://coffeeshop-capstone-backend.herokuapp.com/drinks', headers={
            "Authorization":"Bearer {}".format(self.managerjwt)
        })
        self.assertNotEqual(response.status_code, 401)
        response = requests.patch('https://coffeeshop-capstone-backend.herokuapp.com/drinks/45', headers={
            "Authorization":"Bearer {}".format(self.managerjwt)
        })
        self.assertNotEqual(response.status_code, 401)


if __name__ == "__main__": 
    unittest.main()