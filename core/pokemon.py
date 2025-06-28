class Pokemon:
    def __init__(self, name, pokemon_type, hp, attack, defense, moves):
        self.name = name
        self.pokemon_type = pokemon_type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.moves = moves

    def attack_enemy(self, target, move):
        damage = max(0, move.power + self.attack - target.defense)
        target.receive_damage(damage)
        print(f"{self.name} użył {move.name} na {target.name} i zadał {damage} obrażeń!")

    def receive_damage(self, amount):
        self.hp = max(0, self.hp - amount)

    def is_fainted(self):
        return self.hp <= 0