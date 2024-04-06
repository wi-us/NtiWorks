import dota2gsi

def handle_state(last_state, state):
    # Use nested gets to safely extract data from the state
    hero_name = state.get('hero', {}).get('name')
    health_percent = state.get('hero', {}).get('health_percent')
    max_health = state.get('hero', {}).get('max_health')
    # If the attributes exist, print them
    if health_percent and max_health:
        health = int(max_health * health_percent/100)
        print(f"{hero_name}'s current health: {health}/{max_health}")

server = dota2gsi.Server()
server.on_update(handle_state)
server.start()
