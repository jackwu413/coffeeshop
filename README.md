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

The `./frontend` directory contains a complete Ionic frontend to consume the data from the Flask server. The environment variables found within (./frontend/src/environment/environment.ts) are set to reflect the Auth0 configuration details set up for the backend app. 

[View the README.md within ./frontend for more details.](./frontend/README.md)

### Authentication 

Sample emails/passwords with different roles/persmissions:

manager@coffeeshop.com 
managerpassword-1 
JWT: 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5nZk04cHNmTUZSNkUtdThheFUwVyJ9.eyJpc3MiOiJodHRwczovL2phY2t3dS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZhMGMyZmJiZjIyZWMwMDZiNDZmNzM5IiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjA0NDE4Mjc2LCJleHAiOjE2MDQ0MjU0NzYsImF6cCI6IlBIVE81YVhMYWVPWk9ZaERFeE9NZEx5Y0hrM3hpd0xIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.GSjNvY7wAUWs-2fihuhQAS-WoCUa6TOE9knOkkUGaN52G2lKDORrl7KrXZWhtvhke-QGaYBNKhwy-SZT2HAZBJ9i2aLYpjbTiKiR10zlxYqfazOgCEaBoZqFUvKT06_sf1s8wLmhCmQkag-lnA3RFbIvxEK9Ho7FjeEHOQIZTsL1gPSXgFFe--y1gwoQ83wRi9GLGTJAFo1m4cOvIKfmS6paua9wWt7FvRjOZ489go3KvIyR_GIuc_Txa1YFNByJR3quGn2FZUul9ftphKgKBzktScT97jkaifCVurvr5uKkXCr6pmRVrHSx53_9Is0RWxyT52bDPJ_rrgOgqkC1RQ




barista@coffeeshop.com
baristapassword-1
JWT: 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5nZk04cHNmTUZSNkUtdThheFUwVyJ9.eyJpc3MiOiJodHRwczovL2phY2t3dS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZhMGMzMjYwZDQzMmMwMDZmY2Q5OWFjIiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjA0NDE4MzU3LCJleHAiOjE2MDQ0MjU1NTcsImF6cCI6IlBIVE81YVhMYWVPWk9ZaERFeE9NZEx5Y0hrM3hpd0xIIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.AtHR7PtaTkVWMB1NSJ1krDjpgyu3uAabwYDPp_XZkmVGONshXzJS_bLEDgMP5xu7Yk0lV2B43QOB-WuNnL8SaqxG8S18Uo_hr5zMrnk3cUGOgkg7iHTo1heWR_rQM9uHemjrGdBaUS4CFDlnKrCUuJa-F978C7xa2N9kz5WIg4ZHTB5eyoyA0dA4BH5IIo5yzx8LL_7Q12gDamE1cGiuyR_3WDGL-PVgpK6ac4MIq2C7A7pjykkZ5UvDUQMbU5BaD3LGp1aXG8ihsQJ3N4o6q5SnF6VqsKzhQQmeDJm6lN6R-yRF975RzwwaMwOqizKi4HngEsTUXVRH8UO6Zt_oZg
