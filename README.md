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
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5nZk04cHNmTUZSNkUtdThheFUwVyJ9.eyJpc3MiOiJodHRwczovL2phY2t3dS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZhMGMyZmJiZjIyZWMwMDZiNDZmNzM5IiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjA0NjgwNjEzLCJleHAiOjE2MDQ2ODc4MTMsImF6cCI6IlBIVE81YVhMYWVPWk9ZaERFeE9NZEx5Y0hrM3hpd0xIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.GQGJwebAsyrIntNwcYB3rOfm8AMPU2mZHJuCCZPKKNIou90iiKSs6y9-iIuFmg6dvX8jPPWz89OgsBSL6dIpVPt5kvWjBCvRX4o0qGaqj3pg0m8QFtbFy6g87cZcHBzgQA3b7lXnqZtDRU-LZIICV8jyAazmr0njpW1cEXRj3AWjStMnP8itJNKNzBbc6qkxhUSEH09NYS-1Wcc4zASWzCmS370OgQ-k1ByJ84FMcs-wjbjLMXCvQZaAa2Bbk5toBlWJzxvM7HRmeiCXGeHp5F0VQm_qdbqvbYirxllm0fBKNtjgSFAADfpch8pKwt_tUR80h4mGgfSM7BWY0pIotw




#### barista@coffeeshop.com
- password: baristapassword-1
- JWT: 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5nZk04cHNmTUZSNkUtdThheFUwVyJ9.eyJpc3MiOiJodHRwczovL2phY2t3dS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZhMGMzMjYwZDQzMmMwMDZmY2Q5OWFjIiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjA0NjgwNjQzLCJleHAiOjE2MDQ2ODc4NDMsImF6cCI6IlBIVE81YVhMYWVPWk9ZaERFeE9NZEx5Y0hrM3hpd0xIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.Qod-7kThKTRDG8WoaFrCmBsXO7YMVAmQscmvCzDP4nKrkzWVAQGlnhmaXSNnNJhPDMkb0VBFAHvqqBrZApj6Bm1BQZAycPrdkpYi5tki0RIKMqZJ0ibv_f8Q12yqdOvc4xBmmdC094uVUx76ONbqp5klQsDggAFbpMyDbfeoxsrIkgpcHZX3niLRjUDRcuFhEDSARtDvsRQ8co8twyNucE62TMTx0j8bJPcer1KxINtEItHsWjHoAUKdztILGgVIR-caB_o0eROkmFGo_UF7ggfSzEx04IB5wZweToJv5VcmidfP_fW27eTc91cuevunZakMybzQQkjPJizi6Xw2tQ