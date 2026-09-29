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

    # COMPOSITION CHANGE from aggregiation
    def create_character(self, Name, Role, Race, Abilities):
        new_char = Characters(Name, Role, Race, Abilities)
        self.ACTcharacters.append(new_char)
        print(f"{new_char.character} has been created inside {self.Name}.")

    def cast(self):
        print(f"\n Character Roster: ")
        print(f"\n NAME | SPECIES | ROLE ")
        for char in self.ACTcharacters:
            print(f"{char.character} | {char.race} | {char.role}")


class Characters:
    def __init__(self, Name, Role, Race, Abilities):
        self.character = Name
        self.abilities = Abilities
        self.race = Race
        self.role = Role

    def __str__(self):
        return f"{self.character}"

    def Abilities_Menu(self):
        print(f"----- Skills for {self.character} ----\n")
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


# Execution ---

#Initialize the Parent object
isenburg = VideoGames("Death March", "Adventure", "Clie Co.", "Teen", False, True, True, "2.0.1", False, True)

print("--- Composition: Creating characters inside the game lifecycle --- \n")

#Composition
isenburg.create_character("Seltzer", "Rogue", "Galra", ["Galatious Swamp Strike", "Stealth"])
isenburg.create_character("Kris", "Guitarist", "Human", ["Affection Solo", "Strum"])
isenburg.create_character("Mound", "Knifebringer", "Raccoon", ["Ballsign Slash", "Scavenge"])

print(f"\n--- Objects inside Parent ---")
isenburg.cast()

