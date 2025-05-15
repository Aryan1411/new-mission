from flask import Flask
app=Flask(__name__)


from application.database import db



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from application.model import *
db.init_app(app)
with app.app_context():
    db.create_all()
    

from application.controller import *


if __name__=="__main__":
    app.run(debug=True)