from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    super_name= db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    hero_powers = db.relationship('HeroPower',backref='hero')
    def serialize(self):
        return {
            'id':self.id,
            'name':self.name,
            'super_name': self.super_name,
            'powers': [power.power.serialize() for power in self.hero_powers]
        }
class HeroPower(db.Model,SerializerMixin):
    __tablename__='hero_powers'

    id = db.Column(db.Integer,primary_key=True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer,db.ForeignKey('powers.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('strength')
    def validates_strength(self,key,strength):
        if strength not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must either be 'Strong', 'Weak', 'Average'")
        return strength
    
class Power(db.Model,SerializerMixin):
    __tablename__='powers'

    id = db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    hero_powers = db.relationship('HeroPower',backref='power')\

    def serialize(self):
        return {
            'id':self.id,
            'name':self.name,
            'description':self.description
        }

    @validates('description')
    def validate_description(self,key,description):
        if len(description) < 20:
            raise ValueError("Description length should be at least 20")
        return description
     
