import logging
from dota2gsipy.server import GSIServer

logging.basicConfig(level=logging.INFO)

server = GSIServer(("127.0.0.1", 4000),'API KEY')
server.start_server()

server.game_state.map
log = open("C://Users//1вин//Documents//log.txt", 'w')

while True:
    log.writelines(f'Gold: {server.game_state}')
    #print(f'Gold: {server.game_state.player.gold}')
    #print(f'Name: {server.game_state.player.name}')
    #print(f'Hero name: {server.game_state.hero.name}')
    #print(f'Pos: {server.game_state.hero.pos}')
    #print(f'Talents: {server.game_state.hero.talents}')
    log.close()

