import datetime
from objects import Player, Lineup

# Initialize the lineup
lineup = Lineup()

def display_title():
    current_date = datetime.datetime.now()
    print("================================================================")
    print(" Baseball Team Manager")
    print(f"CURRENT DATE: {current_date.strftime('%Y-%m-%d')}")
    print("================================================================")

def display_menu():
    print("MENU OPTIONS")
    print("1 – Display lineup")
    print("2 – Add player")
    print("3 – Remove player")
    print("4 – Move player")
    print("5 – Edit player position")
    print("6 – Edit player stats")
    print("7 - Exit program")
    print("================================================================")

def add_player():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    position = input("Position: ").upper()
    at_bats = int(input("At bats: "))
    hits = int(input("Hits: "))
    player = Player(first_name, last_name, position, at_bats, hits)
    lineup.add_player(player)  # Use Lineup class to add player
    print(f"{player.full_name} was added.")

def display_lineup():
    print(" Player                 POS  AB    H    AVG")
    print("----------------------------------------------------------------")
    for i, player in enumerate(lineup, 1):  # Use iterator of Lineup
        print(f"{i} {player.full_name.ljust(20)} {player.position}  {str(player.at_bats).rjust(4)}  {str(player.hits).rjust(4)}  {str(player.batting_average).rjust(5)}")

def main():
    display_title()
    while True:
        display_menu()
        option = input("Menu option: ")
        if option == "1":
            display_lineup()
        elif option == "2":
            add_player()
        elif option == "3":
            # Implement remove player functionality
            name_to_remove = input("Enter the full name of the player to remove: ")
            lineup.remove_player(name_to_remove)
            print(f"{name_to_remove} was removed.")
        elif option == "4":
            print("Move player functionality not implemented yet.")
        elif option == "5":
            print("Edit player position functionality not implemented yet.")
        elif option == "6":
            print("Edit player stats functionality not implemented yet.")
        elif option == "7":
            print("Bye!")
            break
        else:
            print("Not a valid option. Please try again.")

if __name__ == "__main__":
    main()
