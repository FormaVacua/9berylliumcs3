class VideoGames:
    def __init__(self, GameName, Genre, Company, PlayerAu, Debug, Load, DLoad, Version, UnStall, Stall):
        self.Name = GameName
        self.Genre = Genre
        self.__Debug = Debug
        self.Company = Company
        self.Audience = PlayerAu
        self.Load = Load
        self.DLoad = DLoad
        self.Version = Version
        self.UnStall = UnStall
        self.Stall = Stall
        self.ACTcharacters = []

    def load(self):
        print(f"Loading {self.Name}...")

    def update(self, Update):
        self.Version = Update
        print(f"Updating {self.Name} to version {self.Version}...")
        print(f"Version: {self.Version}, patchnotes: None Provided")

    def uninstall(self):
        print(f"Uninstalling {self.Name}...")

    def debug(self):
        if self.__Debug:
            print(f"Debugging {self.Name}...")
        else:
            print(f"{self.Name} debug screen off.")

    def __str__(self):
        return f"Game: {self.Name} | Genre: {self.Genre} | Company: {self.Company} |"
        
    def characters(self, character_add):
        self.ACTcharacters.append(character_add)
        print(f"{character_add.name} has been associated with {self.Name}.")

    def cast(self):
        print(f"\n--- Character Roster (Aggregate Objects) ---")
        print(f"NAME | ROLE | LEVEL | HP STATUS")
        for char in self.ACTcharacters:
            status = f"{char.hp}/{char.max_hp}" if char.is_alive else "DEFEATED"
            print(f"{char.name} | {char.role} | Lvl {char.level} | {status}")


class Entity:
    def __init__(self, Name, MaxHP):
        self.name = Name
        self.hp = MaxHP
        self.max_hp = MaxHP
        self.level = 1
        self.exp = 0
        self.is_alive = True

    def take_damage(self, amount):
        """Universal combat calculation method."""
        if not self.is_alive:
            print(f"{self.name} is already down!")
            return
        
        self.hp -= amount
        print(f" {self.name} took {amount} damage! (HP: {self.hp}/{self.max_hp})")
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
            print(f"{self.name} has collapsed...")

    def gain_exp(self, amount):
        """Universal level progression logic."""
        if not self.is_alive:
            print(f"{self.name} cannot earn EXP while defeated!")
            return

        self.exp += amount
        print(f" {self.name} gained {amount} EXP! (Total: {self.exp})")
        
        while self.exp >= 100:
            self.exp -= 100
            self.level += 1
            self.max_hp += 20  # increases
            self.hp = self.max_hp
            print(f" LOVE increased! {self.name} reached Level {self.level}! Max HP increased to {self.max_hp}.")


class Characters(Entity):
    def __init__(self, Name, Role, Race, Abilities, MaxHP):
        super().__init__(Name, MaxHP)
        self.role = Role
        self.race = Race
        self.abilities = Abilities

    def __str__(self):
        return f"{self.name} the {self.role}"

    def Abilities_Menu(self):
        print(f"----- Skills for {self.name} ----\n")
        for i, skill in enumerate(self.abilities, start=1):
            print(f"[{i}] {skill}")
        try:
            turn = int(input("Skills: "))
            if 1 <= turn <= len(self.abilities):
                print(f"Used {self.abilities[turn-1]}. Super effective!")
            else:
                print("Invalid skill.")
        except ValueError:
            print("Please enter a valid number.")


# Execution 

# Characters are born separately from the game
char1 = Characters("Seltzer", "Rogue", "Galra", ["Stealth"], MaxHP=100)
char2 = Characters("Kris", "Guitarist", "Human", ["Strum"], MaxHP=80)
char3 = Characters("Mound", "Knifebringer", "Raccoon", ["Scavenge"], MaxHP=120)

isenburg = VideoGames("Death March", "Adventure", "Clie Co.", "Teen", False, True, True, "2.0.1", False, True)

print("---- Objects before association ----")
print(char1)
print(char2)
print(char3)
print(f"Active Game: {isenburg}\n")

print("---- Testing Inherited Parent Features Prior to Association ----")
char1.gain_exp(120)     # Testing both combat tracking and exp systems
char2.take_damage(25)   
print()

print("---- Association Formation ----")
isenburg.characters(char1)
isenburg.characters(char2)
isenburg.characters(char3)
print()

print("---- Objects After Association Assessment ----")
isenburg.cast()
