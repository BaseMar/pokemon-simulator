import random
from data.data_loader import get_type_multiplier
from constants import DEFAULT_LEVEL, STAB_MULTIPLIER, TYPE_MULTIPLIER_LOG

class Battle:
    def __init__(self, trainer1, trainer2):
        self.trainer1 = trainer1
        self.trainer2 = trainer2

    def run(self):
        print(f"\nRozpoczyna się walka: {self.trainer1.name} vs {self.trainer2.name}!\n")
        
        while self.trainer1.has_pokemon_left() and self.trainer2.has_pokemon_left():
            p1 = self.trainer1.choose_pokemon()
            p2 = self.trainer2.choose_pokemon()
            print(f"\nTura: {p1.name} vs {p2.name}\n")

            move1 = self.select_move(p1)
            move2 = random.choice(p2.moves)
            print(f"{self.trainer2.name} (AI) używa {move2.name}!\n")

            # kolejność po speed
            speed1 = getattr(p1, 'speed', 50)
            speed2 = getattr(p2, 'speed', 50)
            
            if speed1 >= speed2:
                self.attack(p1, p2, move1)
                if not p2.is_fainted():
                    self.attack(p2, p1, move2)
            else:
                self.attack(p2, p1, move2)
                if not p1.is_fainted():
                    self.attack(p1, p2, move1)

        if self.trainer1.has_pokemon_left():
            print(f"\n{self.trainer1.name} wygrał walkę!")
        else:
            print(f"\n{self.trainer2.name} wygrał walkę!")

    def attack(self, attacker, target, move):
        if move.power is None:
            print(f"{attacker.name} użył {move.name}! To jest ruch statusowy – nie zadaje obrażeń.\n")
            return

        attack_stat = getattr(attacker, 'attack', 50)
        defense_stat = getattr(target, 'defense', 50)

        # STAB
        stab = STAB_MULTIPLIER if move.move_type in attacker.pokemon_type else 1.0

        # multiplier typów
        type_multiplier = get_type_multiplier(move.move_type, target.pokemon_type)

        # dmg formula
        damage = (((2*DEFAULT_LEVEL/5 + 2) * move.power * attack_stat / defense_stat)/50 + 2) * stab * type_multiplier
        damage = int(damage)
        target.receive_damage(damage)

        print(f"{attacker.name} użył {move.name}!")
        print(TYPE_MULTIPLIER_LOG.get(type_multiplier, "Ruch był skuteczny."))

        if target.is_fainted():
            print(f"{target.name} padł!")

        print(f"{target.name} ma teraz {target.hp} HP\n")

    def select_move(self, pokemon):
        print(f"\nWybierz atak dla {pokemon.name}:")
        for i, move in enumerate(pokemon.moves):
            power_text = move.power if move.power is not None else "Statusowy"
            print(f"{i+1}. {move.name} ({move.move_type}, Power: {power_text})")
        while True:
            try:
                choice = int(input("Twój wybór: ")) - 1
                if 0 <= choice < len(pokemon.moves):
                    return pokemon.moves[choice]
                else:
                    print("Nieprawidłowy wybór.")
            except ValueError:
                print("Wpisz numer ruchu.")