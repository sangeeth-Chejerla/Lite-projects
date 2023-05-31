class Cricket_stats:
    def __init__(self,runs_data, balls_data, outs_data, matches, player_name):
        self.runs_data = runs_data
        self.balls_data = balls_data
        self.outs_data = outs_data
        self.matches = matches
        self.player_name = player_name

    def total_score(self):
        total_score = sum(self.runs_data)
        return total_score
    

    
    def total_balls_faced(self):
        total_balls = sum(self.balls_data)
        return total_balls
    
    def total_outs(self):
        count = 0
        for i in self.outs_data:
          if i == True:
            count += 1
        return count
    def total_notouts(self):
        return (len(self.matches)- self.total_outs())

                
    def total_matches(self):
        return self.matches
    
    def strike_rate(self):
        return (self.total_score() / self.total_balls_faced()) * 100

    def average(self):
        return (self.total_score() / self.total_outs())



    def display_stats(self):
        print("Player Name:", self.player_name)
        print("Total Matches Played:", self.total_matches())
        print("Total Runs Scored:", self.total_score())
        print("Total Balls Faced:", self.total_balls_faced())
        print("Total Outs:", self.total_outs())
        print("Total Not Outs:", self.total_notouts())
        print("Strike Rate:", self.strike_rate())
        print("Average:", self.average())






runs_data = [125, 65, 12, 18,106]
balls_data = [30, 70, 48, 20,114]
outs_data = [True, False, True, True]
matches = [1,2,3,4,5]
player_name = "Virat kohli"

# Create an object of Cricket_stats class
player1 = Cricket_stats(runs_data, balls_data, outs_data,matches, player_name)
print(player1.display_stats())

