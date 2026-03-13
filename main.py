from menu.menu_manager import MenuManager

def main():
    menu = MenuManager()
    
    while True:
        menu.display_menu()
        choice = input("Wybierz opcję: ").strip()
        menu.process_choice(choice)


if __name__ == "__main__":
    main()