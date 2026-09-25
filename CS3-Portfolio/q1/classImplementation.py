class VideoGames:
    def __init__(self, GameName, Genre, Company, PlayerAu, Debug, Load, DLoad, Version, UnStall, Stall):
        self.Name = GameName
        self.Genre = Genre
        self.__Debug = Debug  # Private attribute
        self.Company = Company
        self.Audience = PlayerAu
        self.DLoad = DLoad
        self.Version = Version
        self.UnStall = UnStall
        
    def load(self):
        print(f"Loading {self.Name}...")
        
    def update(self, Update):
        self.Update = Update  # Updates the existing version attribute
        print(f"Updating {self.Name} to version {self.version}...")
        print(f"Version: {self.version}, patchnotes: None Provided")
        
    def uninstall(self):
        print(f"Uninstalling {self.Name}...")
        
    def debug(self):
        if self.__Debug:
            print(f"Debugging {self.Name}...")
        else:
            print(f"{self.Name} debug screen off.")
            
    def __str__(self):
        return f"Game: {self.Name} | Genre: {self.Genre} | Company: {self.Company} |"

obj_1 = VideoGames("Hollow Knight: Silksong", "Action-Adventure", "Team Cherry", "Everyone", True, "1.13.0") 
obj_2 = VideoGames("Tomodachi Life: Living the Dream", "Simulation", "Nintendo", "Teen", False, "1.0.0")

print(obj_1)
print(obj_2)

print("\n--- TESTING ---")
obj_1.update("2.0")
print("Object state after update on object ")
print(f"Object 1: {obj_1.Name} | Version: {obj_1.Update}")
