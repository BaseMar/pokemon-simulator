import random
from core.pokemon import Pokemon

class Battle:
    def __init__(self, trainer1, trainer2):
        self.trainer1 = trainer1
        self.trainer2 = trainer2

    def run(self):
        while self.trainer1.has_pokemon_left() and self.trainer2.has_pokemon_left():
            p1 = self.trainer1.choose_pokemon()
            p2 = self.trainer2.choose_pokemon()

            while not p1.is_fainted() and not p2.is_fainted():
                move = self.select_move(p1)
                p1.attack_enemy(p2, move)
                if p2.is_fainted(): break

                move = self.select_move(p2)
                p2.attack_enemy(p1, move)

        winner = self.trainer1 if self.trainer1.has_pokemon_left() else self.trainer2
        print(f"Zwycięzca: {winner.name}")

    def select_move(self, pokemon):
        if isinstance(pokemon, Pokemon):
            print(f"Wybierz atak dla {pokemon.name}:")
            for i, m in enumerate(pokemon.moves):
                print(f"{i+1}. {m}")
            idx = int(input("Twój wybór: ")) - 1
            return pokemon.moves[idx]
        else:
            return random.choice(pokemon.moves)