# Coffee Shop - Capstone Project

## Full Stack Nano

This is a full stack drink menu application. The application is able to:

1) Display graphics representing the ratios of ingredients in each drink.
2) Allow public users to view drink names and graphics.
3) Allow the shop baristas to see the recipe information.
4) Allow the shop managers to create new drinks and edit existing drinks.

## About the Stack

### Backend

The `./backend` directory contains a Flask server with a SQLAlchemy module to simplify your data needs. It is hosted on Heroku at the following URL: 

"https://coffeeshop-capstone-backend.herokuapp.com/"

[View the README.md within ./backend for more details.](./backend/README.md)

### Frontend

The `./frontend` directory contains a complete Ionic frontend to consume the data from the Flask server. The environment variables found within (./frontend/src/environment/environment.ts) are set to reflect the Auth0 configuration details set up for the backend app. The frontend application must be run locally with "ionic serve" in the front repository. 

[View the README.md within ./frontend for more details.](./frontend/README.md)

### Authentication 

Sample emails/passwords with different roles/persmissions:

#### manager@coffeeshop.com 
- password: managerpassword-1 
- JWT: 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5nZk04cHNmTUZSNkUtdThheFUwVyJ9.eyJpc3MiOiJodHRwczovL2phY2t3dS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZhMGMyZmJiZjIyZWMwMDZiNDZmNzM5IiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjA0Nzc0OTc5LCJleHAiOjE2MDQ3ODIxNzksImF6cCI6IlBIVE81YVhMYWVPWk9ZaERFeE9NZEx5Y0hrM3hpd0xIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.FIsKWuFJBlN7kaorK7xxIurzFs1_Ee_nTQJwTenm9RzYIQYutOCaSTPY5UzdAXWYI6S7ySMIwdt3s1sDATk6xBBL2Yr0yMZx_lUsz32359nPuk_RnSi0zQcfEC2DdU79_6s1wT5hOp1ylKJyxsZagTuzjUCCheIYUbdrelo2zRiTVwBukwdpZN81108I60FoqDDczc6-B5rrVrXny0ZEU6sF3us-uexIHBIIDQr2_SFfjjmCzJNpPMl0ZObf_pd-pSkQo50rKPaAd672MsJFWMSOOrECfGgcfvCb0tvPbyyK2nEEo4q1sw0yx5sQL1CWSaYcARNkXjLGVTf6f2z1cA




#### barista@coffeeshop.com
- password: baristapassword-1
- JWT: 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5nZk04cHNmTUZSNkUtdThheFUwVyJ9.eyJpc3MiOiJodHRwczovL2phY2t3dS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZhMGMzMjYwZDQzMmMwMDZmY2Q5OWFjIiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjA0Nzc0OTkwLCJleHAiOjE2MDQ3ODIxOTAsImF6cCI6IlBIVE81YVhMYWVPWk9ZaERFeE9NZEx5Y0hrM3hpd0xIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.GPmqkCUQoBa-MYcTMj3mX2jpwZyOrbiMbiOy3Wgyj7jaexgrJxzeHsRz4asWxx25Pdfgu5vttugE8uaJz6RtwEPzZQvHowyMLWh9frYq6RSVAX_Q3wF_etVpWm-ER3XiGyvr079ol9RCOtyUwS3B3b0GJy8ugcxSsCdIHgbjIUBpQC3Y1pJpH1oVSoIaD_JoCqAGEBLHP6lVz5ImpyWEq4fgQUKLBcJJZX2bDLgqwejA4MUmnK6RxPEAm10w_y76ADFCCK3nkBIeVYERV0WieD8D_82GZGHTWaiKAjscKsfGsnMFWJUJRv6VJN87g7dn9G08OwvWrHpi-DHNF9gwaA