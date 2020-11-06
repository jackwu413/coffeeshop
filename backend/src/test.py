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

    baristajwt = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5nZk04cHNmTUZSNkUtdThheFUwVyJ9.eyJpc3MiOiJodHRwczovL2phY2t3dS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZhMGMzMjYwZDQzMmMwMDZmY2Q5OWFjIiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjA0Njk3ODMwLCJleHAiOjE2MDQ3MDUwMzAsImF6cCI6IlBIVE81YVhMYWVPWk9ZaERFeE9NZEx5Y0hrM3hpd0xIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.dav1JwnohWe0tLUwOx0FuPpbZzGDg8v-hw47IVb9n4QPz5jN8JqVRhQthDC2OHt0bj8w9yGFTHpSHdD74FkyU1kWCZirVUB9Zq2P0X90FZ8eZ-MT__2IGCMyTYJxQkIkgUOHACBmisU7_CTARS8CNO2g7hmL-zXKy-bIih-MS9GJo0boy5T1tmP5EAkU2YAKp7Z_mNUvjgaCxmQddIscBh9CsSdg5wd5BYnqfamfNFGOYFAKkOD6_jQ_kTqZDgJWV6kGjXkgDVdmOmAJcBpQTAKerFNN_hAjTtzhBKSk_l4B1QKPjv832uUAgF_1KZiTgKqut9Esbcb_MRgIIA2qmw"
    managerjwt = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5nZk04cHNmTUZSNkUtdThheFUwVyJ9.eyJpc3MiOiJodHRwczovL2phY2t3dS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZhMGMyZmJiZjIyZWMwMDZiNDZmNzM5IiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjA0Njk3ODEzLCJleHAiOjE2MDQ3MDUwMTMsImF6cCI6IlBIVE81YVhMYWVPWk9ZaERFeE9NZEx5Y0hrM3hpd0xIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.DRBlzCAz6w1igBafLXYccgXAayRd0Giw3hNNG6S70LnpTFaBKUOuOn8XjUWMU4wl9lVoaMartfStF6cdTlfJj8vvyp6nUJqAqxsdJcrKQCM-ssWiINUBjBKsUZLHNtRCUSPY5bYpuluoBVGrvRy15G7oxasfqg_PLS61pBbU6vLMNt4X2oooG8r88dlaUD7OTHPC0R4qq-PdFmX0WyFnaB9N1090fsBRRw2Kc_q-pkuWA40_5BuBuVnxCtrXHSVHIvISFU1P19mPpZ0j5aCERcUPa1ezynxyQbfKCcawP36xqLAbEOu2K6x-_XvtW057WL_0zhwwes2a0X2G4fBUHg"
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
        self.sample_drink["title"] += str(random.randint(10, 1000))
        d = Drink(
            title = self.sample_drink["title"],
            recipe = str(self.sample_drink["recipe"])
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

        response = requests.patch('https://coffeeshop-capstone-backend.herokuapp.com/drinks/{}'.format(d_id), headers={
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