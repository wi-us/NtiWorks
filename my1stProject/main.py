from teams import Team
from gui.interface import root
# Create teams
arrTeams = []
arrTeams.append(Team(0, "Liquid", 4, 2, 6, 2))
arrTeams.append(Team(1, "1win", 4, 2, 6, 2))
arrTeams.append(Team(2, "Aurora", 4, 6, 2, 6))

for teams in arrTeams:
    print(teams.id, '|', teams.name, '|',teams.matchesNumber, '|',teams.wins, '-',teams.loses)


root.mainloop()