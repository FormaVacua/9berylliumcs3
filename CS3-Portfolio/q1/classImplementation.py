class VideoGames:
    def __init__(GameName, Genre, Company, PlayerAu, Debug, Load, DLoad, Update, UnStall, Stall):
        GameName.Name = GameName
        GameName.Genre = Genre
        GameName.__Debug = Debug
        GameName.Company = Company
        GameName.Audience = PlayerAu
        GameName.DLoad = DLoad
        GameName.Update = Update
        GameName.UnStall = UnStall
    def load(GameName):
        print(f"Loading {GameName.Name}...")
    def update(GameName, Update):
        print(f"Updating {GameName.Name} to version {Update}...")
    def uninstall(GameName):
        print(f"Uninstalling {GameName.Name}...")
    def debug(GameName):
        if GameName.__Debug:
            print(f"Debugging {GameName.Name}...")
        else:
            print(f"{GameName.Name} debug screen off.")


obj_1 = VideoGames("Hollow Knight: Silksong", "Action-Adventure", "Team Cherry", "Everyone", True, True, True, "1.13.0", True, False)
obj_2 = VideoGames("Tomodachi Life: Living the Dream", "Simulation", "Lauren Montgomery and co.", "Teen", False, True, True, "1.0.0", True, False)

print(obj_1)
print(obj_2)

## Analysis - 
### Why did you make your chosen attribute private?
### Which method changes the state of your object?
### How did your two objects demonstrate that instances are independent?
### What is the difference between your class diagram and your object diagram?
