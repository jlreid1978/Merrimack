

class mp3:
    # Initialize the user dictionary for the MP3 class
    def __init__(self):
        self.users = {}


    # Module to add a user. Check present if user already exists
    def add_user(self, name):
        if name in self.users:
            print(f"\n\033[31mUser {name} already exists.\033[0m\n")
        else:
            self.users[name] = {"id": len(self.users) + 1, "music": []}
            print(f"\nUser {name} added.")


    # Module to get a user from self.users
    def get_user(self, name):
        if name in self.users:
            return name
        else:
            return None
        
    
    # Module to add music
    def add_music(self, name, title, artist):
        self.users[name]["music"].append({"title": title, "artist": artist})
        print(f"\n{title} added.\n")


    # Module to delete music
    def delete_music(self, name, song):
        try:
            self.users[name]["music"] = [s for s in self.users[name]["music"] if s.get("title") != song]
            print(f"\n{song} has been removed\n")

        except (KeyError, ValueError):
            print(f"\n\033[31m{song} not found.\033[0m\n")


    # Module to get music
    def get_music(self, name):
        try:
            music = self.users[name]["music"]
            return music
        except KeyError:
            return None

        
# Creates the user menu based on if there are multiple users or any songs in the user's catelog
def menu(player, name):
    subscribers = len(player.users)
    master_list = {
        0: [f"\n---Welcome {name} ---", "null"],
        1: ["1. Add user", addUser], 
        2: ["2. Change user", changeUser], 
        3: ["3. Add a song", addSong],
        4: ["4. Retrieve song details", getSong],
        5: ["5. Update song details", changeSong],
        6: ["6. Delete a song", deleteSong],
        7: ["7. Display all songs", displaySongs],
        8: ["8. Exit", exit]
    }

    # Split the master list (dictionary) into multiple lists for easier handling by Main.
    numbers = list(master_list.keys())
    to_do = []
    choices = []

    for m in master_list.values():
        to_do.append(m[1])
        choices.append(m[0])
    try:
        songs = len(player.get_music(name))
    except TypeError:
        songs = 0
    if subscribers == 1:
        if songs == 0:
            numbers = numbers[:2] + numbers[3:4] + numbers[8:9]
        else:
            numbers = numbers[:2] + numbers[3:]
    else:
        if songs == 0:
            numbers = numbers[:4] + numbers[8:9]
        else:
            numbers = numbers[0:]

    return numbers, choices, to_do


# Function to add a user. Extra checks to verify that the user does not already exist. 
def addUser(player, user=None, run=True):
    name = input("Please add a user.  ")
    if not user:
        user = name
        player.add_user(name)
    else:
        if name == player.get_user(name):
            print(f"\n\033[31mUser {name} already exists.\033[0m\n")
        else:
            player.add_user(name)
  
    return run, user


# Function to switch to a different user, checking if that user exists.
def changeUser(player, old_user, run=True):
    name = input("What user would you like to switch to?  ")
    try:
        user = player.get_user(name)

        if name != user:
            raise ValueError
        else:
            print(f"\nSwitched to user {user}.\n")
    except ValueError:
        print(f"\n\033[31mUser {name} does not exist.\033[0m\n")

    if not user:
        user = old_user
    return run, user


# Function to add a song
def addSong(player, user, run=True):
    song = input("What song would you like to add?  ")
    artist = input(f"What artist plays {song}?  ")
    try:
        player.add_music(user, song, artist)
    except (KeyError, ValueError) as e:
        print(f"\n\033[31mError adding {song}\n{e}\nPlease check if song already exists.\033[0m\n")
    return run, user


# Function to retrieve song information 
def getSong(player, user, run=True):
    song = input("What song would you like to retrieve?  ")
    music = player.get_music(user)
    
    for m in music:
        if m["title"] == song:
            try:
                title = m["title"]
                artist = m["artist"]
                print(f"\n{title} by {artist}\n")
                return run, user
            except KeyError:
                print(f"\n\033[31m{song} does not exist in this player.\033[0m\n")

    print(f"\n\033[31m{song} does not exist in this player.\033[0m\n")
    return run, user


# Function to change song information 
def changeSong(player, user, run=True):
    song = input("What song would you like to edit?  ")
    music = player.get_music(user)
    
    for m in music:
        if m["title"] == song:
            old_artist = m["artist"]
            artist = input(f"What artist plays {song}?  ")
            try:
                player.delete_music(user, song)
                player.add_music(user, song, artist)
                print(f"{song} updated from {old_artist} to {artist}")
                return run, user
            except (KeyError, ValueError) as e:
                print(f"\n\033[31mError editing {song}\n{e}\nPlease try again.\033[0m\n")
                
    print(f"\n\033[31m{song} does not exist in this player.\033[0m\n")    
    return run, user
    

# Function to delete a song completely
def deleteSong(player, user, run=True):
    song = input("What song would you like to remove?  ")
    music = player.get_music(user)
    for m in music:
        if m["title"] == song:
            player.delete_music(user, song)
            return run, user

    print(f"\n\033[31m{song} does not exist in this player.\033[0m\n")
    return run, user


# Function to display all songs for the user
def displaySongs(player, user, run=True):
    music = player.get_music(user)
    if not music:
        print(f"\nThis player is empty.\n")
    else:
        print("\nPlayer Contents:")
        for m in music:
            print(f"{m['title']} by {m['artist']}")
    return run, user


# Function to exit the program
def exit(player, user="", run=False):            
    print("\n\033[32mExiting the player.\nHave a nice day.\033[0m\n")
    return run, user


# Function to run the program, call the menu setup, and run the functions based on valid user input.
def main():
    player = mp3()
    run = True

    while run is True:
        subscribers = len(player.users)

        if subscribers == 0:
            run, user = addUser(player)
 
        numbers, choices, to_do = menu(player, user)
    
        for n in numbers:
            print(choices[n], end="\n")

        try:
            user_choice = int(input("\nPlease make a selection. "))
            if user_choice not in numbers[1:]:
                raise ValueError
        except ValueError:
            print("\n\033[31mInvalid selection, please try again.\033[0m\n")
            continue

        try:
            selection = to_do[user_choice]
            run, user = selection(player, user)
        except (KeyError, ValueError) as e:
            print(f"\n\033[31mThere was an error with that selection.\n{e}\nPlease try again.\033[0m\n")



if __name__ == "__main__":
    main()