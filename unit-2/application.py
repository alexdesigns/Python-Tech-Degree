import time
import constants
import random

#clean data
def get_data():

    print("Team:")
    select_num = 0
    for key in clean_player_list.items():
        select_num += 1
        print("{}) {}".format(select_num, key))
    
    teams_tool_play = True
    while teams_tool_play:
        select_team = input("\nChoose Team - Enter an option: ")

        try:
            select_team = int(select_team)

        except ValueError:
            print ("ERROR: CHOOSE A NUMBER\n")
            
        else:
            if select_team >= 1 and select_team <= 3:
                restart_attempt = 0
                # -------------------------------------
                if select_team == 1:
                    output_team('Panthers', clean_player_list)
                elif select_team == 2:
                    output_team('Bandits', clean_player_list)
                elif select_team == 3:
                    output_team('Warriors', clean_player_list)
                # -------------------------------------
                restart_tool()
                break
            else:
                print ("ERROR: ENTER 1-3\n")
    
    return select_team
        
                
def output_team(team_name, clean_player_list):
    output_exp_num = 0
    output_inexp_num = 0
    player_names = []

    player_name = [k['name'] for k in clean_player_list[team_name]]

    print("-" * 40)
    print("\nTeam: {}".format(team_name))
    print("Total Players: ", len(clean_player_list[team_name]))
    print("Players: ",", ".join(player_name))        

def restart_tool():
    restart_attempt = 1
    print("-" * 40)
    time.sleep(.5)
    print("Quit: Enter Q")
    select_restart = input("Restart: Enter Y ")
    print("-" * 40)
    select_restart = select_restart.upper() 
    if select_restart == "Q":
        teams_tool_play = False
        print("Goodbye")
        quit()
    elif select_restart == "Y":
        get_data()        
        pass
    else:
        print("Enter Q or Y")
        pass

def player_sort():
    teams = constants.TEAMS
    players = constants.PLAYERS
    team_list = {team: [] for team in teams}
    players_per_team = len(players) // len(teams)

    for player in players.copy():
        for key, value in player.items():           
            if key == 'experience' and value == 'YES':
                player[key] = True
            elif key == 'experience' and value == 'NO':
                player[key] = False

    for name, val in team_list.items():
        exp_num = 0
        inexp_num = 0

        for player in players.copy():          
            random_player = random.choice(players)

            if random_player['experience'] == True and exp_num < 3 and len(team_list[name]) < players_per_team:
                exp_num += 1
                team_list[name].append(random_player)
                players.remove(random_player)

            elif random_player['experience'] == False and inexp_num < 3 and len(team_list[name]) < players_per_team:
                inexp_num += 1 
                team_list[name].append(random_player)
                players.remove(random_player)

    return team_list
    
clean_player_list = player_sort()
#cleaned data

def start_tool():

    print("-" * 40)
    print("BASKETBALL TEAM STATS TOOL")
    print("-" * 40)
    time.sleep(.5)
    print("\n---- MENU----\n")
    time.sleep(.5)
    print("Here are your choices:")
    print("1) Display Team Stats")
    print("2) Quit")
    print("-" * 40)

    play_tool = True
    while play_tool:

        error_num = 0
        if error_num != 0:
            option_num = input("Ready? Enter 1 or 2: ")
        else:
            time.sleep(.5)
            option_num = input("Enter 1 or 2: ")

        print("-" * 40)

        try:
            option_num = int(option_num)
        except ValueError:
            print ("ERROR: Try Again...\n")
            error_num += 1
            continue
        else:
            if option_num == 1:
                get_data() 
            elif option_num == 2:
                print("Goodbye")
                play_tool = False
                break
            else:
                print("ERROR: Try Again...\n")
                pass


if __name__ == '__main__': 
    start_tool()