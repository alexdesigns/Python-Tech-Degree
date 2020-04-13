import random
import time
import constants


def clean_players():
    players = constants.PLAYERS
    for player in players:
        for key, value in player.items():           
            if key == 'experience' and value == 'YES':
                player[key] = True
            elif key == 'experience' and value == 'NO':
                player[key] = False

    return players

clean_player_data = clean_players()

def format_teams(teams):
    #range_teams = range(len(teams))
    #teams = {i: value for team in range_teams,value in enumerate(team, 1)}
    teams = {1: 'Panthers', 2: 'Bandits', 3: 'Warriors'}

    for key, value in teams.items():
        print(f'  {key}) {value}')
    
    select_team = input("Enter an option > 1: ")

    try: 
        select_team == int(select_team)
    except ValueError:
        print ("ERROR: CHOOSE A NUMBER\n")
    else:
        select_team = int(select_team)
        create_teams(clean_player_data, select_team, teams)


def create_teams(clean_player_data, select_team, teams):
    players_list = clean_player_data
    total_teams = 3
    total_players = len(players_list)
    num_of_players = total_players // total_teams
    roster_exp = []
    roster_inexp = []

    for player in players_list:
        for key, value in player.items():
            if key == 'experience':
                if value == True:
                    roster_exp.append(player)
                else:
                    roster_inexp.append(player)

    team_1 = []
    team_2 = []
    team_3 = []
    available_players = True    
    while available_players:
        exp_index = random.randint(0, len(roster_exp) - 1)
        inexp_index = random.randint(0, len(roster_inexp) - 1)
        team_1.append(roster_exp[exp_index])
        del roster_exp[exp_index]
        team_1.append(roster_inexp[inexp_index])
        del roster_inexp[inexp_index]
        # --------------------------------
        exp_index = random.randint(0, len(roster_exp) - 1)
        inexp_index = random.randint(0, len(roster_inexp) - 1)
        team_2.append(roster_exp[exp_index])
        del roster_exp[exp_index]
        team_2.append(roster_inexp[inexp_index])
        del roster_inexp[inexp_index]
        # --------------------------------
        exp_index = random.randint(0, len(roster_exp) - 1)
        inexp_index = random.randint(0, len(roster_inexp) - 1)
        team_3.append(roster_exp[exp_index])
        del roster_exp[exp_index]
        team_3.append(roster_inexp[inexp_index])
        del roster_inexp[inexp_index]
        # --------------------------------
        if len(roster_exp) > 0:
            continue
        else:
            available_players = False

    if select_team == 1:
        current_team = team_1
        team_name = 'Panthers'
    elif select_team == 2:
        current_team = team_2
        team_name = 'Badgers'
    else: 
        current_team = team_3
        team_name = 'Warriors'

    player_names = []
    for val in current_team:
        for key, value in val.items():
            if key == "name":
                player_names.append(value)
            if key == 'experience':
                if value == True:
                    roster_exp_num = len(roster_exp)
                else:
                    roster_inexp_num = len(roster_inexp)

    print("\nTeam: {}".format(team_name))
    print("\n", "-" * 40)
    print("Total Players: ", len(current_team))
    #print("Total Experienced Players: ", len(roster_exp_num))
    #print("Total Inexperienced Players: ", len(roster_inexp_num))
    print("Players: ",", ".join(player_names))


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
    option_num = input("Enter 1 or 2: ")
    print("-" * 40)

    play_tool = True
    while play_tool:
        try:
            option_num = int(option_num)
        except ValueError:
            print ("ERROR: ENTER 1 OR 2")
            continue
        else:
            if option_num == 1:
                format_teams(teams=constants.TEAMS)         
            else:
                print("Goodbye")
                play_tool = False
                break
        
        print("-" * 40)
        select_restart = input("Choose Another Team? Y/N")
        select_restart = select_restart.upper() 
        if select_restart == "Y":
            format_teams(teams=constants.TEAMS)         
            pass
        else:
            print("Goodbye")
            play_tool = False
        

if __name__ == '__main__': 
    start_tool()
