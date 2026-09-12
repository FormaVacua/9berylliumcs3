class VideoGames:
    # Changed first argument to 'self' to avoid overwriting input arguments
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


obj_1 = VideoGames("Hollow Knight: Silksong", "Action-Adventure", "Team Cherry", "Everyone", True, True, True, "1.13.0", True, False)
obj_2 = VideoGames("Tomodachi Life: Living the Dream", "Simulation", "Nintendo", "Teen", False, True, True, "1.0.0", True, False)

print(obj_1)
print(obj_2)

print("\n--- TESTING ---")

obj_1.update("2.0")

print("Object state after update on object ")
print(f"Object 1: {obj_1.Name} | Version: {obj_1.Update}")

## Analysis - 
### Why did you make your chosen attribute private? The visual clutter of lines of code shouldn't be seen by the user. Not only because the code can be vulnerable and dissectable for replicas, but also because the code would distract the player.
### Which method changes the state of your object? The method 'update' updates the version of the game.
### How did your two objects demonstrate that instances are independent? Object 2 wasn't affected by the update in object 1.
### What is the difference between your class diagram and your object diagram? The class diagram shows what comprises the class-- the attributes and methods. While the object diagram shows the blueprint class being used to create objects.
