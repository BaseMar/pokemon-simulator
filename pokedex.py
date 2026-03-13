# pokedex.py
from data.db import session
from models import PokemonSpecies

def show_pokedex(name: str):
    pokemon = session.query(PokemonSpecies).filter_by(name=name).first()
    if not pokemon:
        print(f"Nie znaleziono Pokémona o nazwie {name}")
        return
    type_names = [t.type.name for t in pokemon.types]
    print("—" * 40)
    print(f"Pokédex: {pokemon.name}")
    print(f"Pokedex Number: {pokemon.pokedex_number}")
    print(f"Generation: {pokemon.generation.number} ({pokemon.generation.region_name})")
    print(f"Type(s): {', '.join(type_names)}")
    print(f"HP: {pokemon.stats.hp}")
    print(f"Attack: {pokemon.stats.attack}")
    print(f"Defense: {pokemon.stats.defense}")
    print(f"Legendary: {'Yes' if pokemon.is_legendary else 'No'}")
    print(f"Mythical: {'Yes' if pokemon.is_mythical else 'No'}")
    print(f"Height: {pokemon.height_m} m")
    print(f"Weight: {pokemon.weight_kg} kg")
    print("—" * 40)