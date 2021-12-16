from flask import Flask
from flask_dotenv import DotEnv

from database import database

def app_factory() -> Flask:
    """
    Application factory

    :return: Ready-work application
    """

    # Creating application object
    app: Flask = Flask(__name__)

    # Initializing the .env 
    # configuration
    env: DotEnv = DotEnv(app)

    # Initializing a created
    # database instance
    database.init_app(app) 

    # Returns a ready-work application
    return app

# Creating a application
app: Flask = app_factory()

if __name__ == "__main__":
    # If our application script is not
    # connected as library, then
    # we will run application in debug mode
    app.run(debug=True)