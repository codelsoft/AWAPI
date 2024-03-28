import select
from flask_restful import Resource
from marshmallow import ValidationError
from models import User,Reward,db
from  schemas import RewardSchemas,UserSchemas
from flask import request

class  UserRessources(Resource):

    #Objet schema User pour la serialization / deserialization
    user_schema = UserSchemas()
    user_liste_schema = UserSchemas(many=True)

    

   #GET qui affiche liste des utilisateur ou un utilisateur
    def  get(self,user_id=None):
        user_data=None
        if user_id:
            user_one  = User.query.get_or_404(user_id)
            user_data =  self.user_schema.dump(user_one)
        
        else:
            users_all = User.query.all()
            user_data =  self.user_liste_schema.dump(users_all)
        
        return  user_data
    #Post
    def post(self):
        # Recupere les données venant de l'utilisateur
        new_data = self.user_liste_schema.load(request.json)
    
        if new_data :
            for d in new_data:
                new_user = User(
                        name = d['name']
                ) 
        
                db.session.add(new_user)
                db.session.commit()
        return "Data inserted!"

    #put 

    def put(self, user_id):
        try:
            new_data = self.user_schema.load(request.json)
        except ValidationError as err:
              print(err.message)
        
        user_obj = User.query.get_or_404(user_id)

        if user_obj:
            for k,value in new_data.items():
                if value:
                    setattr(user_obj,k,value)

            db.session.commit()

        return self.user_schema.dump(user_obj)
  

    #delete
    def  delete(self,user_id):
        if user_id:
            user_to_delete = User.query.get_or_404(user_id)
            print(user_to_delete)
        if user_to_delete:
            db.session.delete(user_to_delete)
            db.session.commit()
        return "user deleted!"
    

          
class RewardResources(Resource):

    #Objet schema Reward pour la serialization / deserialization
    reward_schema = RewardSchemas()
    reward_liste_schemas = RewardSchemas(many=True)

    #Get
    def   get(self,user_id=None):

        if user_id:
    
            rewards =  db.session.query(Reward, User).join(User, User.id == Reward.user_id).all()
           
            return self.reward_liste_schemas.dump(rewards[0])
        
        else:
           pass
        
        return  0
        