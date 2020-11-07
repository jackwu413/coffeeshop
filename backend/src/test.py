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

    baristajwt = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5nZk04cHNmTUZSNkUtdThheFUwVyJ9.eyJpc3MiOiJodHRwczovL2phY2t3dS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZhMGMzMjYwZDQzMmMwMDZmY2Q5OWFjIiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjA0Nzc0OTkwLCJleHAiOjE2MDQ3ODIxOTAsImF6cCI6IlBIVE81YVhMYWVPWk9ZaERFeE9NZEx5Y0hrM3hpd0xIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.GPmqkCUQoBa-MYcTMj3mX2jpwZyOrbiMbiOy3Wgyj7jaexgrJxzeHsRz4asWxx25Pdfgu5vttugE8uaJz6RtwEPzZQvHowyMLWh9frYq6RSVAX_Q3wF_etVpWm-ER3XiGyvr079ol9RCOtyUwS3B3b0GJy8ugcxSsCdIHgbjIUBpQC3Y1pJpH1oVSoIaD_JoCqAGEBLHP6lVz5ImpyWEq4fgQUKLBcJJZX2bDLgqwejA4MUmnK6RxPEAm10w_y76ADFCCK3nkBIeVYERV0WieD8D_82GZGHTWaiKAjscKsfGsnMFWJUJRv6VJN87g7dn9G08OwvWrHpi-DHNF9gwaA"
    managerjwt = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5nZk04cHNmTUZSNkUtdThheFUwVyJ9.eyJpc3MiOiJodHRwczovL2phY2t3dS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZhMGMyZmJiZjIyZWMwMDZiNDZmNzM5IiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjA0Nzc0OTc5LCJleHAiOjE2MDQ3ODIxNzksImF6cCI6IlBIVE81YVhMYWVPWk9ZaERFeE9NZEx5Y0hrM3hpd0xIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.FIsKWuFJBlN7kaorK7xxIurzFs1_Ee_nTQJwTenm9RzYIQYutOCaSTPY5UzdAXWYI6S7ySMIwdt3s1sDATk6xBBL2Yr0yMZx_lUsz32359nPuk_RnSi0zQcfEC2DdU79_6s1wT5hOp1ylKJyxsZagTuzjUCCheIYUbdrelo2zRiTVwBukwdpZN81108I60FoqDDczc6-B5rrVrXny0ZEU6sF3us-uexIHBIIDQr2_SFfjjmCzJNpPMl0ZObf_pd-pSkQo50rKPaAd672MsJFWMSOOrECfGgcfvCb0tvPbyyK2nEEo4q1sw0yx5sQL1CWSaYcARNkXjLGVTf6f2z1cA"
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

        patched_title = "patched drink " + str(random.randint(1,1000))


        patched_drink = {
            "title": patched_title,
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