#Amy Doan ID: 1895125
class Team: # Team Class
    def __init__(self,team_name = "none",team_wins = 0, team_losses = 0): # Assign constructor
        self.team_name = team_name
        self.team_wins = team_wins
        self.team_losses = team_losses
    def get_win_percentage(self): # Calculated win percentage
        Win_Percentage = float(self.team_wins) / float((self.team_wins + self.team_losses))
        return Win_Percentage
if __name__ == '__main__':
    TeamAvg = Team() # Assign Team class to TeamAvg
    TeamAvg.team_name = input() # Input name
    TeamAvg.team_wins = int(input()) # Input wins
    TeamAvg.team_losses = int(input()) # Input losses
    if TeamAvg.get_win_percentage() >= .50: # If and else to print out average message
        print("Congratulations, Team",TeamAvg.team_name,"has a winning average!")
    else:
        print("Team",TeamAvg.team_name,"has a losing average.")