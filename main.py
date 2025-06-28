from data.data_loader import load_moves, load_pokemons
from menu.menu_manager import MenuManager

def main():
    moves = load_moves("moves.csv")
    pokemons = load_pokemons("pokemons.csv", moves)
    menu = MenuManager(moves, pokemons)
    
    while True:
        menu.display_menu()
        choice = input("Wybierz opcję: ").strip()
        menu.process_choice(choice)


if __name__ == "__main__":
    main()