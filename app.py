from flask import Flask

def app_factory() -> Flask:
    """
    Application factory

    :return: Ready-work application
    """

    # Creating application object
    app = Flask(__name__)

    # Returns a ready-work application
    return app

# Creating a application
app: Flask = app_factory()

if __name__ == "__main__":
    # If our application script is not
    # connected as library, then
    # we will run application in debug mode
    app.run(debug=True)