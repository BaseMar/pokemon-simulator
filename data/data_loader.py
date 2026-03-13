import random
from sqlalchemy.orm import aliased
from data.db import session
from models import PokemonMove, PokemonSpecies, BaseStats, PokemonType, Type, Move, TypeEffectiveness
from core.pokemon import Pokemon
from core.move import Move as CoreMove
from constants import MAX_MOVES

def load_pokemons_from_db(limit=None):
    pokemons = []
    all_moves = load_all_moves()
    query = session.query(PokemonSpecies).join(BaseStats).join(PokemonType).join(Type)
    
    if limit:
        query = query.limit(limit)
    for p in query.all():
        types = [t.type.name for t in p.types]
        stats = p.stats

        if all_moves:
            moves = random.sample(all_moves, min(MAX_MOVES, len(all_moves)))
        
        #db_moves = session.query(PokemonMove).filter_by(pokemon_id=p.id).all()
        #if db_moves:
            #selected_moves = random.sample(db_moves, min(4, len(db_moves)))
            #moves = [CoreMove(m.move.name, m.move.type_rel.name, m.move.power) for m in selected_moves]
        #else:
            #moves = []

        pokemons.append(Pokemon(
            name=p.name,
            pokemon_type=types,
            hp=stats.hp,
            attack=stats.attack,
            defense=stats.defense,
            moves=moves,
        ))
    return pokemons

def load_all_moves():
    """Ładuje wszystkie ruchy z tabeli moves i zwraca listę obiektów CoreMove"""
    db_moves = session.query(Move).all()
    all_moves = [CoreMove(m.name, m.type_rel.name, m.power) for m in db_moves]
    return all_moves

def get_type_multiplier(attacking_type_name, defending_types):
    multiplier = 1.0

    AttType = aliased(Type)
    DefType = aliased(Type)

    for def_type in defending_types:
        te = session.query(TypeEffectiveness)\
            .join(AttType, TypeEffectiveness.attacking_type)\
            .join(DefType, TypeEffectiveness.defending_type)\
            .filter(AttType.name == attacking_type_name)\
            .filter(DefType.name == def_type)\
            .first()
        if te:
            multiplier *= float(te.multiplier)
        else:
            multiplier *= 1.0
    return multiplier