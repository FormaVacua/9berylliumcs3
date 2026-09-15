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
  def __init__(self, Name, Equipment, Role, Race, Inventory, Abilities, UseInventory):
    self.character = Name
    self.abilities_default = [["RC"],["ES"],["EQ"]]
    self.abilities = Abilities
    self.race = Race
    self.stats_default = [["HP: ", 100], ["ATK: ", 15], ["DEF: ", 30], ["MANA: ", 10]]
    self.equipment = Equipment
    self.role = Role
    Invetory = [[],[],[],[]]
    self.inventory = Inventory
    
    def Abilities(self):
      skill = int(input(" Use a skill. | 1-RC | 2-ES | 3-EQ |"))
      if skill == 1:
        self.stats_default = self.stats_default([]) - 5
      print("Used torrent. Super effective.")
    def UseInvetory(self, Inventory):
      option = int(input("| Storage 1 | Weapon 2 | Food 3 | Buffers 4 |"))
      if len(invetory([0],[1],[2],[3])) ==! 0:
        if option == 1:
          use = input("Use Storage")
        if option == 2:
          use = input("Use Weapon")
        if option == 3:
          use = input("Use Food")
        if option == 4:
          use = input("Use buff")
  
obj_1 = VideoGames("Hollow Knight: Silksong", "Action-Adventure", "Team Cherry", "Everyone", True, True, True, "1.13.0", True, False)
obj_2 = VideoGames("Tomodachi Life: Living the Dream", "Simulation", "Nintendo", "Teen", False, True, True, "1.0.0", True, False)

print(obj_1)
print(obj_2)

print("\n--- TESTING ---")

obj_1.update("2.0")

print("Object state after update on object ")
print(f"Object 1: {obj_1.Name} | Version: {obj_1.Update}")
