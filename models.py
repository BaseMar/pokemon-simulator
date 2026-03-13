from sqlalchemy import Column, Integer, SmallInteger, String, Boolean, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from data.db import Base

class Generation(Base):
    __tablename__ = "generations"
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    region_name = Column(String)
    pokemon_species = relationship("PokemonSpecies", back_populates="generation")

class PokemonSpecies(Base):
    __tablename__ = "pokemon_species"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    pokedex_number = Column(Integer)
    generation_id = Column(Integer, ForeignKey("generations.id"))
    height_m = Column(Numeric)
    weight_kg = Column(Numeric)
    is_legendary = Column(Boolean)
    is_mythical = Column(Boolean)

    generation = relationship("Generation", back_populates="pokemon_species")
    types = relationship("PokemonType", back_populates="pokemon")
    stats = relationship("BaseStats", uselist=False, back_populates="pokemon")

class PokemonType(Base):
    __tablename__ = "pokemon_types"
    pokemon_id = Column(Integer, ForeignKey("pokemon_species.id"), primary_key=True)
    type_id = Column(Integer, ForeignKey("types.id"), primary_key=True)
    slot = Column(Integer)
    pokemon = relationship("PokemonSpecies", back_populates="types")
    type = relationship("Type", back_populates="pokemon_types")

class BaseStats(Base):
    __tablename__ = "base_stats"
    pokemon_id = Column(Integer, ForeignKey("pokemon_species.id"), primary_key=True)
    hp = Column(Integer)
    attack = Column(Integer)
    defense = Column(Integer)
    pokemon = relationship("PokemonSpecies", back_populates="stats")

class Type(Base):
    __tablename__ = "types"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    pokemon_types = relationship("PokemonType", back_populates="type")

class Move(Base):
    __tablename__ = "moves"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    type_id = Column(Integer, ForeignKey("types.id"))
    power = Column(SmallInteger)
    type_rel = relationship("Type")

class PokemonMove(Base):
    __tablename__ = "pokemon_moves"
    pokemon_id = Column(Integer, ForeignKey("pokemon_species.id"), primary_key=True)
    move_id = Column(Integer, ForeignKey("moves.id"), primary_key=True)
    # learn_method i level_learned pominięte

    move = relationship("Move")

class TypeEffectiveness(Base):
    __tablename__ = "type_effectiveness"
    attacking_type_id = Column(Integer, ForeignKey("types.id"), primary_key=True)
    defending_type_id = Column(Integer, ForeignKey("types.id"), primary_key=True)
    multiplier = Column(Numeric(3,2), nullable=False)

    attacking_type = relationship("Type", foreign_keys=[attacking_type_id])
    defending_type = relationship("Type", foreign_keys=[defending_type_id])