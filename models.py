from  flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey,String,Integer
from sqlalchemy.orm import declarative_base,relationship


Base = declarative_base()
db = SQLAlchemy(model_class=Base)

class User(Base):

    __tablename__ ='user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class Reward(Base):
    __tablename__ = 'reward'


    id =          Column(Integer, primary_key=True)
    reward_name = Column(String(250))
    user_id     = Column(Integer, ForeignKey("user.id"))  # FK added

    user = relationship("User")