class Match:
    def __init__(self, format, team1, team2, ID = None, status = "Planned", score1 = 0, score2 = 0):
        self.ID = ID
        self.format = format
        self.team1 = team1
        self.team2 = team2
        self.status = status
        self.score1 = score1
        self.score2 = score2