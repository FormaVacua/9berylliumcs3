class VideoGames:
    def __init__(self, GameName, Genre, Company, PlayerAu, Debug, Load, DLoad, Update, UnStall, Stall):
        self.Name = GameName
        self.Genre = Genre
        self.__Debug = Debug  # Private attribute
        self.Company = Company
        self.Audience = PlayerAu
        self.DLoad = DLoad
        self.Update = Update
        self.UnStall = UnStall
        
    def load(self):
        print(f"Loading {self.Name}...")
        
    def update(self, Update):
        self.Update = Update  # Updates the existing version attribute
        print(f"Updating {self.Name} to version {Update}...")
        print(f"Version: {Update}, patchnotes: None Provided") # Fixed empty curly braces
        
    def uninstall(self):
        print(f"Uninstalling {self.Name}...")
        
    def debug(self):
        if self.__Debug:
            print(f"Debugging {self.Name}...")
        else:
            print(f"{self.Name} debug screen off.")
            
    def __str__(self):
        return f"Game: {self.Name} | Genre: {self.Genre} | Company: {self.Company} |"


class Characters:
  def __init__(self, Name, Role, Race, Abilities):
    self.character = Name
    self.abilities = Abilities
    self.race = Race
    self.role = Role
    Inventory = []
    
    def Abilities(self):
      skill = int(input(f" Use a skill. {self.abilities}"))
        print(f"Used {self.abilities[skill-1]}. Super effective.")
