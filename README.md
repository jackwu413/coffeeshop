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

barista@coffeeshop.com
baristapassword-1