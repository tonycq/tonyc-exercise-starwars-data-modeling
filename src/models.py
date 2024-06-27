import os
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# Tabla intermedia para la relación muchos-a-muchos entre Usuario y Favoritos
user_favorite_association = Table(
    'user_favorite_association',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('favorite_id', Integer, ForeignKey('favorite.id'))
)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    
    # Relación uno-a-muchos con Favoritos
    favorites = relationship("Favorite", secondary=user_favorite_association, back_populates="users")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, back_populates="favorites")
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    climate = Column(String(100))
    population = Column(Integer)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birth_year = Column(String(20))
    gender = Column(String(20))
    height = Column(Integer)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet, back_populates="characters")

    # Relación uno-a-muchos con Favoritos
    favorites = relationship("Favorite", back_populates="character")

# Generar el diagrama usando eralchemy2
render_er(Base, 'diagram.png')
