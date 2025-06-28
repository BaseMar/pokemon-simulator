from core.trainer import HumanTrainer, AITrainer
from core.battle import Battle
import copy
import random

TEAM_SIZE = 3


class MenuManager:
    def __init__(self, moves, pokemons):
        self.moves = moves
        self.pokemons = pokemons

    def display_menu(self):
        print("1. Rozpocznij walkę")
        print("2. Wyjście")

    def process_choice(self, choice):
        if choice == "1":
            self.start_battle()
        elif choice == "2":
            print("Do zobaczenia!")
            exit()

    def start_battle(self):
        print("Tworzenie trenerów...")
       # Gracz
        player_name = input("Podaj swój nick: ").strip()
        player_team = self.pokemons[:TEAM_SIZE]        
        player_trainer = HumanTrainer(player_name, player_team)

        # AI
        ai_name = input("Podaj nick rywala: ")
        ai_team = [copy.deepcopy(p) for p in random.sample(self.pokemons, TEAM_SIZE)]
        ai_trainer = AITrainer(ai_name, ai_team)

        battle = Battle(player_trainer, ai_trainer)
        battle.run()