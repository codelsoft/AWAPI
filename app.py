from flask import Flask
from models import User,Reward,db
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from resources import RewardResources, UserRessources
from schemas import ma
from flask_restful import Api


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/AWDB'

db.init_app(app)
ma.init_app(app)

api =Api(app)
api.add_resource(UserRessources,'/user','/user/<int:user_id>')
api.add_resource(RewardResources,'/reward','/reward/<int:user_id>')


"""
with app.app_context():
    #db.create_all()

    user_on = User(name='Alzo niane') 
    user_two = User(name= 'Bra Sy')

    reward1= Reward(reward_name='Prix Newyork',user_id=1, user= user_on)
    reward2= Reward(reward_name='Prix Nouakchot',user_id=1, user= user_on)
    reward3= Reward(reward_name='Prix Newyork',user_id=2, user= user_two)

    db.session.add(user_on)
    db.session.add(user_two)
    db.session.add(reward1)
    db.session.add(reward2)
    db.session.add(reward3)
    db.session.commit()
"""


app.run(debug=True)