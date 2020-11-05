import os 
import unittest 
import json 
import requests
from flask_sqlalchemy import SQLAlchemy 
from app import create_app
from database.models import setup_db, Drink


class CoffeeTestCase(unittest.TestCase): 

baristajwt = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5nZk04cHNmTUZSNkUtdThheFUwVyJ9.eyJpc3MiOiJodHRwczovL2phY2t3dS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZhMGMzMjYwZDQzMmMwMDZmY2Q5OWFjIiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjA0NjA4MDMxLCJleHAiOjE2MDQ2MTUyMzEsImF6cCI6IlBIVE81YVhMYWVPWk9ZaERFeE9NZEx5Y0hrM3hpd0xIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.n6ygZHGCQC-oXdJdyy7yJ-ADT8bPCZNxSLiJo4Sfij3Vl3o4gHMMPt50qCGsVBaFPruuOR8WPy-XM8rVcE8CwjYn1r9l9m1aEcg1wAnknmYvLFID1uTvEZFzK5iJgAA0677qnTWwjUQ0Wq60hKzRTR4pPUZZRWcn5BEtcnsxM-kcjukusSQY-ue-gCfhz3VN3wt5ILUA-0NAS4Tkw1-yDvrsyO5YqIRBwwroV3sm3XykuUi2ghFzqI1EWWkfIIrRUHN5H1H-3qrMF7tql-jLB1X0UsZgUtBgpmqYUa7OAqUkW-M80B6BAq_asvgtOuHuLluTPaAVaOfNYt6iO-qmiw'
managerjwt = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5nZk04cHNmTUZSNkUtdThheFUwVyJ9.eyJpc3MiOiJodHRwczovL2phY2t3dS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZhMGMyZmJiZjIyZWMwMDZiNDZmNzM5IiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjA0NjA4MTI4LCJleHAiOjE2MDQ2MTUzMjgsImF6cCI6IlBIVE81YVhMYWVPWk9ZaERFeE9NZEx5Y0hrM3hpd0xIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.e8VNL_a4Tql7dnbuPeYiEy0oy6H0CycLhQFXjGp-unXhv_A1vbLnNeLS4uDJr5gUXN2cclsSPaaayPBo589NCkU_HroBHF94Ig73iqsgOML2pNyU9NsJNWN8f0GiqHZQbBsLLt8HfEPNyOKyI_Zf5BqaRXkmG13GRFFkHIrH87OPXco7jcl4lHA_OU-mhAcUPi6TI4Xn_31vuEEJpUJpmyaMj3j-vbWBkZxvEiuGHiyjVAuKMgPLIWlmmRjC-pS8s7P3dfv-W5yKJV-IIn5K2SS2ibpt8ppK7BytCtBFKZEIytCSRVCtMGDasc-Te34KXoFDZWqsad1cC-Pgb_l-mg'

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
            "Authorization":"Bearer {}".format(self.baristajwt)
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