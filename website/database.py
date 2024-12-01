from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker


# Create the SQLAlchemy db instance
db = SQLAlchemy()
Session = None

def create_db_connection():
    global Session

    # Initialize the Flask application
    database_info = Flask(__name__)

    # Configure the SQLAlchemy part of the app instance
    database_info.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/pemancingan'
    database_info.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the SQLAlchemy instance with the app
    db.init_app(database_info)

    # Create a sessionmaker bound to the engine
    with database_info.app_context():
        Session = sessionmaker(bind=db.engine)

    return database_info, Session

def create_session():
    return Session()