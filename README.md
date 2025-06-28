# Pokémon Simulator
Gra konsolowa, która symuluję walkę z kultowych gier serii Pokemon. Gracz wybiera dostępne Pokémony i ich ataki, a system walki rozstrzyga wynik na podstawie statystyk i typu ruchu.


## Funkcje
-Wczytywanie Pokémonów i ruchów z plików CSV (`pokemons.csv`, `moves.csv`)
-Logika walki oparta na statystykach i typach
-Menu interfejs w konsoli (nawigacja przez wpisywanie opcji)
-Możliwość ponownego wyboru Pokémonów i kolejnych walk


## Uruchomienie
### Wymagania
- Python `3.9+`

### Uruchom:
python main.py


## Struktura projektu
pokemon-simulator/
├── core/                 
│   ├── battle.py         
│   ├── move.py           
│   ├── pokemon.py        
│   └── trainer.py        
│
├── io/                   
│   └── data_loader.py
│
├── menu/                 
│   └── menu_manager.py
│
├── moves.csv             
├── pokemons.csv          
├── main.py               
├── README.md             
└── .gitignore            
                         


## Przykład użycia
1. Rozpocznij walkę
2. Wyjście
Wybierz opcję: 1
Tworzenie trenerów...
Podaj swój nick: BaseMar
Podaj nick rywala: Gary

BaseMar, wybierz Pokemona:
1. Squirtle (HP: 44)
2. Charmander (HP: 39)
3. Bulbasaur (HP: 45)
Twój wybór: 1
Gary (AI) wybiera: Bijek
Wybierz atak dla Squirtle:
1. Bite (Dark, Power: 60)
2. Rapid Spin (Normal, Power: 50)
3. Wave Crash (Water, Power: 120)
4. Hydro Pump (Water, Power: 110)
Twój wybór: 2
Squirtle użył Rapid Spin na Bijek i zadał 90 obrażeń!

BaseMar, wybierz Pokemona:
1. Squirtle (HP: 44)
2. Charmander (HP: 39)
3. Bulbasaur (HP: 45)
Twój wybór: 2
Gary (AI) wybiera: Charmander
Wybierz atak dla Charmander:
1. Dragon Breath (Dragon, Power: 60)
2. Flamethrower (Fire, Power: 90)
3. Slash (Normal, Power: 70)
4. Inferno (Fire, Power: 100)
Twój wybór: 1
Charmander użył Dragon Breath na Charmander i zadał 70 obrażeń!

BaseMar, wybierz Pokemona:
1. Squirtle (HP: 44)
2. Charmander (HP: 39)
3. Bulbasaur (HP: 45)
Twój wybór: 3
Gary (AI) wybiera: Squirtle
Wybierz atak dla Bulbasaur:
1. Solar Beam (Grass, Power: 120)
2. Take Down (Normal, Power: 90)
3. Razor Leaf (Grass, Power: 55)
4. Vine Whip (Grass, Power: 45)
Twój wybór: 4
Bulbasaur użył Vine Whip na Squirtle i zadał 45 obrażeń!

Zwycięzca: BaseMar

1. Rozpocznij walkę
2. Wyjście
Wybierz opcję: 2
Do zobaczenia!


## Dalszy rozwój
- dodanie typów pokemonów i ich ruchom (przewagi/wrażliwości)
- GUI
- dodawanie/usuwanie/edytowanie drużyny i ich ruchów