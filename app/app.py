from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.debug = True
app.config.from_object('config.Config')

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///circular.db'
#app.config['SQLALCHEMY_ECHO'] = False
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#migrate = Migrate(app,db)
migrate = Migrate(app,db,render_as_batch=True)
#Caution if you use SQLITE, adding <render_as_batch=True> . This option is batch mode .

#import models 
