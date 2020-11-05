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
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5nZk04cHNmTUZSNkUtdThheFUwVyJ9.eyJpc3MiOiJodHRwczovL2phY2t3dS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZhMGMyZmJiZjIyZWMwMDZiNDZmNzM5IiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjA0NjA4MTI4LCJleHAiOjE2MDQ2MTUzMjgsImF6cCI6IlBIVE81YVhMYWVPWk9ZaERFeE9NZEx5Y0hrM3hpd0xIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.e8VNL_a4Tql7dnbuPeYiEy0oy6H0CycLhQFXjGp-unXhv_A1vbLnNeLS4uDJr5gUXN2cclsSPaaayPBo589NCkU_HroBHF94Ig73iqsgOML2pNyU9NsJNWN8f0GiqHZQbBsLLt8HfEPNyOKyI_Zf5BqaRXkmG13GRFFkHIrH87OPXco7jcl4lHA_OU-mhAcUPi6TI4Xn_31vuEEJpUJpmyaMj3j-vbWBkZxvEiuGHiyjVAuKMgPLIWlmmRjC-pS8s7P3dfv-W5yKJV-IIn5K2SS2ibpt8ppK7BytCtBFKZEIytCSRVCtMGDasc-Te34KXoFDZWqsad1cC-Pgb_l-mg




#### barista@coffeeshop.com
- password: baristapassword-1
- JWT: 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5nZk04cHNmTUZSNkUtdThheFUwVyJ9.eyJpc3MiOiJodHRwczovL2phY2t3dS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZhMGMzMjYwZDQzMmMwMDZmY2Q5OWFjIiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjA0NjA4MDMxLCJleHAiOjE2MDQ2MTUyMzEsImF6cCI6IlBIVE81YVhMYWVPWk9ZaERFeE9NZEx5Y0hrM3hpd0xIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.n6ygZHGCQC-oXdJdyy7yJ-ADT8bPCZNxSLiJo4Sfij3Vl3o4gHMMPt50qCGsVBaFPruuOR8WPy-XM8rVcE8CwjYn1r9l9m1aEcg1wAnknmYvLFID1uTvEZFzK5iJgAA0677qnTWwjUQ0Wq60hKzRTR4pPUZZRWcn5BEtcnsxM-kcjukusSQY-ue-gCfhz3VN3wt5ILUA-0NAS4Tkw1-yDvrsyO5YqIRBwwroV3sm3XykuUi2ghFzqI1EWWkfIIrRUHN5H1H-3qrMF7tql-jLB1X0UsZgUtBgpmqYUa7OAqUkW-M80B6BAq_asvgtOuHuLluTPaAVaOfNYt6iO-qmiw
