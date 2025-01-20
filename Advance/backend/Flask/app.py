from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import template_rendered

db = SQLAlchemy()

def database_integrate():
  db = SQLAlchemy()
  app = Flask(__name__, template_folder = 'template')
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./dbtodo.db'
  
  db.init_app(app)
  
  # nanti di import
  
  migrate = Migrate(app,db)
  
  return app
