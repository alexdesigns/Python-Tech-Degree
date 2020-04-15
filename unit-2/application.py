import time
import constants
import random

def data_tool():
    teams = teams=constants.TEAMS
    teams = {k: v for k, v in enumerate(teams, 1)}

    print("Team:")
    for key, value in teams.items():
        print(f'  {key}) {value}')
    
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
                final_teams()
                # -------------------------------------
                show_data(select_team)
                # -------------------------------------
                restart_tool()
                break
            else:
                print ("ERROR: ENTER 1-3\n")
        
                
def final_teams():
    get_roster = players_tool()
    all_roster = dict(j for i in get_roster for j in i.items())
    
    roster_players = len(all_roster)
    players_amount = roster_players // 3

    team_1 = []
    team_2 = []
    team_3 = []

    exp_count = 0
    inexp_count = 0

    print(all_roster, "----------------")
        

    for k, v in all_roster.items():  
        print(f'  {k}) {v}')
        random_player = random.choice(list(all_roster.keys()))
        #random_player_exp = random_player['experience']
        #print(random_player_exp)
        quit()
        for player in all_roster:
            if random_player['experience'] == True and exp_count < 3 and 3 < 6:
                exp_count += 1
                #team_val = vars()['team_{}'.format(exp_count)]
                team_1.append(random_player)
                all_roster.remove(random_player)

            elif random_player['experience'] == False and inexp_count < 3 and 3 < 6:
                inexp_count += 1
                #team_val = vars()['team_{}'.format(exp_count)]
                team_1.append(random_player)
                all_roster.remove(random_player)

    print("team_1:", team_1)
    return team_1, team_2, team_3


def show_data(current_team):
    team_1, team_2, team_3 = final_teams()

    #print(final_teams())

    teams = teams=constants.TEAMS
    player_names = []
    roster_exp_num = 0
    roster_inexp_num = 0

    if current_team == 1:
        final_team = team_1
        team_name = teams[current_team]
    elif current_team == 2:
        final_team = team_2
        team_name = teams[current_team]
    else: 
        final_team = team_3
        team_name = teams[current_team]
    
    for val in final_team:
        for key, value in val.items():
            if key == "name":
                player_names.append(value)
            if key == 'experience' and value == True:
                roster_exp_num += 1
            else:
                roster_inexp_num += 1

    print("-" * 40)
    print("\nTeam: {}".format(team_name))
    print("Total Players: ", len(final_team))
    print("Total Experienced Players: ", roster_exp_num)
    print("Total Inexperienced Players: ", roster_inexp_num)
    print("Players: ",", ".join(player_names))        

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
        data_tool()        
        pass
    else:
        print("Enter Q or Y")
        pass

def players_tool():
    players = constants.PLAYERS
    for player in players:
        for key, value in player.items():           
            if key == 'experience' and value == 'YES':
                player[key] = True
                pass
            elif key == 'experience' and value == 'NO':
                player[key] = False
                pass
    
    return players

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
    option_num = input("Ready? Enter 1 or 2: ")
    print("-" * 40)

    play_tool = True
    while play_tool:
        try:
            option_num = int(option_num)
        except ValueError:
            print ("ERROR: ENTER 1 OR 2")
            #pass
        else:
            if option_num == 1:
                data_tool()         
            else:
                print("Goodbye")
                play_tool = False
                break


if __name__ == '__main__': 
    start_tool()
