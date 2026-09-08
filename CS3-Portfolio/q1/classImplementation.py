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
        GameName.Stall = Stall
    def load(GameName):
        print(f"Loading {GameName.Name}...")
    def download(GameName):
        print(f"Downloading {GameName.Name}...")
    def update(GameName, Update):
        print(f"Updating {GameName.Name} to version {Update}...")
    def uninstall(GameName):
        print(f"Uninstalling {GameName.Name}...")
    def debug(GameName):
        if GameName.__Debug:
            print(f"Debugging {GameName.Name}...")
        else:
            print(f"{GameName.Name} debug screen off.")

## Analysis
### Why did you make your chosen attribute private?
### Which method changes the state of your object?
### How did your two objects demonstrate that instances are independent?
### What is the difference between your class diagram and your object diagram?
