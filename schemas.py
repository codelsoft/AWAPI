from flask_marshmallow import Marshmallow
from models import db,User,Reward

ma = Marshmallow()

#classe UserSchema()
class  UserSchemas(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User()



class RewardSchemas(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reward()
