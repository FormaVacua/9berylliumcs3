class VideoGames:
    def __init__(self, GameName, Genre, Company, PlayerAu, Debug, Load, DLoad, Version, UnStall, Stall):
        self.Name = GameName
        self.Genre = Genre
        self.__Debug = Debug  # Private attribute
        self.Company = Company
        self.Audience = PlayerAu
        self.Load = Load
        self.DLoad = DLoad
        self.Version = Version
        self.UnStall = UnStall
        self.Stall = Stall

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
        print(f"{character_add.character} has been added.")
    def cast(self):
        print(f"\n Character Roster: ")
        for char in self.characters:
            print(f"{char.ACTcharacters} | {char.race} | {char.role}")

class Characters:
  def __init__(self, Name, Role, Race, Abilities):
    self.character = Name
    self.abilities = Abilities
    self.race = Race
    self.role = Role
    self.inventory = []
    
    def Abilities(self):
        print(f"----- Skills for {self.character} ----\n")
        for i, skill in enumerate(self.abilities, start=1):
            print(f"[{index}] {skill}")
        try:
            turn = int(input("Skills: "))
            if 1<= turn <= len(self.abilities):
                print(f"Used {self.abilities[turn-1]}. Super effective!")
            else:
                print("Invalid skill.")
