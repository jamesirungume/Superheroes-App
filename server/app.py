#!/usr/bin/env python3

from flask import Flask, make_response,jsonify,render_template,request
from flask_migrate import Migrate
from flask_restful import Api,Resource

from models import db, Hero,HeroPower,Power

app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/build',
    template_folder='../client/build'
)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://my_name:obBw505hbh8jIfdSwuB3rkwXW8gMbrev@dpg-ckcjhqciibqc73cd0b7g-a.oregon-postgres.render.com/new_db_giq6'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.errorhandler(404)
def not_found(e):
    return render_template("index.html")

api = Api(app)

class Home(Resource):
    def get(self):
        home_response = {"Home":"Superheroes API",}
        response = make_response(jsonify(home_response),200,)
        return response
api.add_resource(Home,'/')

class HeroesResource(Resource):
    def get(self):
        heroes= [{'id':hero.id,'name':hero.name,'super_name':hero.super_name} for hero in Hero.query.all()]
        response = make_response(jsonify(heroes),200)
        return response

api.add_resource(HeroesResource,'/heroes')

class HeroesById(Resource):
    def get(self,id):
        heroes= Hero.query.filter(Hero.id == id).first()
        if not heroes:
            heroes_dict= {"error":"hero not found"}
            response = make_response(jsonify(heroes_dict),404)
            return response
        response = make_response(jsonify(heroes.serialize()),200)
        return response

api.add_resource(HeroesById,'/heroes/<int:id>')

class PowerResource(Resource):
    def get(self):
        powers = [{'id':power.id,'name':power.name,'description':power.description} for power in Power.query.all()]
        response = make_response(jsonify(powers),200)
        return response
    
api.add_resource(PowerResource,'/powers')

class PowerById(Resource):
    def get(self,id):
        power = Power.query.filter(Power.id == id).first()
        if not power:
            power_dict= {"error":"power not found"}
            response = make_response(jsonify(power_dict),404)
            return response
        response = make_response(jsonify(power.serialize()),200)
        return response
    def patch(self,id):
        data = request.get_json()
        power = Power.query.get(id)
        if not power:
            power_dict = {"error": "Power not found"}
            response = make_response(jsonify(power_dict), 404)
            return response
        if 'description' in data:
            power.description = data['description']
        try:
            db.session.commit()
            return make_response(power.serialize(), 200)
        except Exception as e:
            db.session.rollback()
            error_response = {"errors": ["Validation errors"]}
            response = make_response(jsonify(error_response), 400)
            return response
    


api.add_resource(PowerById,'/powers/<int:id>')

class HeroPowers(Resource):
    def post(self):
        data = request.get_json()
        heropowers = HeroPower(strength=data['strength'],hero_id=data['hero_id'],power_id= data['power_id'] )
        db.session.add(heropowers)
        db.session.commit()
        response = make_response(heropowers.hero.serialize(),201)
        return response


api.add_resource(HeroPowers,'/hero_powers')





if __name__ == '__main__':
    app.run(port=5555)
