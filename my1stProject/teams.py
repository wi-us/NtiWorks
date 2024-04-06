class Team:
    def __init__(self, id, name, matchesNumber = 0, wins = 0, loses = 0, points = 0, finishedMatches = None):
        self.id = id
        self.name = name
        self.matchesNumber = matchesNumber
        self.wins = wins
        self.loses = loses
        self.points = points
        self.finishedMatches = finishedMatches

    def edit_team(self, id, name):
        self.id = id
        self.name = name

    def edit_score(self, matchesNumber, wins, loses, points):
        self.matchesNumber = matchesNumber
        self.wins = wins
        self.loses = loses
        self.points = points