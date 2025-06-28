import random

class Trainer:
    def __init__(self, name, pokemons):
        self.name = name
        self.pokemons = pokemons

    def has_pokemon_left(self):
        return any(not p.is_fainted() for p in self.pokemons)

    def choose_pokemon(self):
        raise NotImplementedError()
    

class HumanTrainer(Trainer):
    def choose_pokemon(self):
        print(f"{self.name}, wybierz Pokemona:")
        for i, p in enumerate(self.pokemons):
            if not p.is_fainted():
                print(f"{i+1}. {p.name} (HP: {p.hp})")
        choice = int(input("Twój wybór: ")) - 1
        return self.pokemons[choice]

    

class AITrainer(Trainer):
    def choose_pokemon(self):
        alive = [p for p in self.pokemons if not p.is_fainted()]
        chosen = random.choice(alive)
        print(f"{self.name} (AI) wybiera: {chosen.name}")
        return chosen
