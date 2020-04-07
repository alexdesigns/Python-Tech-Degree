import constants
import random 

def clean_the_data():
    players_list = constants.PLAYERS
    for player in players_list:
        for key, value in player.items():           
            #print(key,": ", value,"\n")
            #print(player)
            if key == 'experience':
                if value == 'YES':
                    player[key] = True
                else:
                    player[key] = False

    return players_list

def roster_list(players):
    roster_exp = []
    roster_inexp = []
    for player in players:
        for key, value in player.items():
            if key == 'experience':
                if value == True:
                    roster_exp.append(player)
                else:
                    roster_inexp.append(player)
                    
    return roster_exp, roster_inexp

def create_teams(roster_exp, roster_inexp):
    team_a = []
    team_b = []
    team_c = []
    available_players = True
    team_num = 0
    while available_players:
        team_num =+ 1
        while team_num <=3:
            exp_index = random.randint(0, len(roster_exp) - 1)
            inexp_index = random.randint(0, len(roster_inexp) - 1)
            team_a.append(roster_exp[exp_index])
            del roster_exp[exp_index]
            team_a.append(roster_inexp[inexp_index])
            del roster_inexp[inexp_index]
    else:
        available_players = False

    return team_a, team_b, team_c



if __name__ == '__main__':
    roster_exp, roster_inexp = roster_list(clean_the_data())
    panthers_players, bandits_players, warriors_players = create_teams(roster_exp, roster_inexp)

    print("BASKETBALL TEAM STATS TOOL\n")
    print("---- MENU----\n")
    print("Here are your choices:")
    print("1) Display Team Stats")
    print("2) Quit")
    option_num = input("Enter an option > 1 =")
    option_num =  int(option_num)

    if option_num <= 1:
        if option_num == 1:
            print("Team A", team_a, "-------------\n")
            print("Team A", team_b, "-------------\n")
            print("Team A", team_c, "-------------\n")

            #print("Experienced", roster_exp, "\n\n --------------------")
            #print("Not Experienced", roster_inexp, "\n\n") 
        else:
            print("Goodbye")
    elif option_num == 0:
        print("choose a 1 or 2")
    else:
        print("choose a correct number")

