import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False, unique=True)
    first_name= Column(String(100), nullable=False)
    last_name = Column(String(100), nullable = False)
    password = Column(String(150), nullable = False)

class Planeta(Base):
    __tablename__='planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    user_planet_id = Column(Integer, ForeignKey=('usuario.id'))


class Personaje(Base):
    __tablename__='personajes'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    eye_color = Column(String(50))
    age  = Column(Integer)
    user_character_id=Column(Integer, ForeignKey=('usuario.id'))
    
class Favorito(Base):
    __tablename__='favoritos'
    id = Column(Integer, primary_key=True)
    user_favorite_id=Column(Integer, ForeignKey=('usuario.id'))
    planet_id=Column(Integer, ForeignKey=('planetas.id'))
    character_id = Column(Integer, ForeignKey=('personajes.id'))
    




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
