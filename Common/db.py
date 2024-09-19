# Common/db.py
from flask import Flask
from Common.DBManager import DBManager
from config import Config

def init_db(app: Flask) -> DBManager:
    app.config.from_object(Config)
    db_manager = DBManager(app)
    # Register db_manager with the app context
    app.extensions['db_manager'] = db_manager
    return db_manager
