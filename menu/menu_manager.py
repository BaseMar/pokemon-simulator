from core.trainer import HumanTrainer, AITrainer
import random
from constants import TEAM_SIZE

from data.data_loader import load_pokemons_from_db

class MenuManager:
    def __init__(self):
        pass

    def display_menu(self):
        print("1. Rozpocznij walkę")
        print("2. Pokedex")
        print("3. Wyjście")

    def process_choice(self, choice):
        if choice == "1":
            self.start_battle()
        elif choice == "2":
            name = input("Wpisz nazwę Pokémona: ").strip()
            from pokedex import show_pokedex
            show_pokedex(name)
        elif choice == "3":
            print("Do zobaczenia!")
            exit()

    def start_battle(self):
        print("Tworzenie trenerów...")

        all_pokemons = load_pokemons_from_db()
        
        player_name = input("Podaj swój nick: ").strip()
        player_team = []
        available = all_pokemons.copy()

        # Gracz wybiera zespół
        print(f"\nWybierz {TEAM_SIZE} Pokémonów do swojego zespołu:")
        for n in range(TEAM_SIZE):
            for i, p in enumerate(available):
                print(f"{i+1}. {p.name} (HP: {p.hp}, Type: {', '.join(p.pokemon_type)})")
            
            while True:
                try:
                    choice = int(input(f"Twój wybór ({n+1}/{TEAM_SIZE}): ")) - 1
                    if 0 <= choice < len(available):
                        break
                    else:
                        print("Nieprawidłowy numer, spróbuj ponownie.")
                except ValueError:
                    print("Wpisz poprawny numer.")

            selected = available.pop(choice)
            player_team.append(selected)

        player_trainer = HumanTrainer(player_name, player_team)

        # AI losuje swój zespół
        remaining_for_ai = [p for p in all_pokemons if p not in player_team]
        ai_team = random.sample(remaining_for_ai, TEAM_SIZE)
        ai_trainer = AITrainer("AI", ai_team)

        # Rozpoczęcie walki
        from core.battle import Battle
        battle = Battle(player_trainer, ai_trainer)
        battle.run()