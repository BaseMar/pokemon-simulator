import csv
from core.move import Move
from core.pokemon import Pokemon

def load_moves(filename):
    moves = {}
    with open (filename, encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            name = row["name"]
            move_type = row["type"]
            power = int(row["power"])
            moves[name] = Move(name, move_type, power)
    return moves

def load_pokemons(filename, moves_dict):
    pokemons = []
    with open (filename, encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            name = row["name"]
            pokemon_type = row["type"]
            hp = int(row["hp"])
            attack = int(row["attack"])
            defense = int(row["defense"])
            moves_name = row["moves"].split("|")
            pokemon_moves = [moves_dict[mn] for mn in moves_name if mn in moves_dict]
            pokemons.append(Pokemon(name, pokemon_type, hp, attack, defense, pokemon_moves))
    return pokemons