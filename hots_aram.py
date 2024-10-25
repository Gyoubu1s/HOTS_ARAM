from heroes_pool_tanks import heroes_pool_tanks
from heroes_pool_bruiser import heroes_pool_bruisers
from heroes_pool_melee_assassin import heroes_pool_ma
from heroes_pool_ranged_assassin import heroes_pool_ra
from heroes_pool_support import heroes_pool_support
from heroes_pool_healer import heroes_pool_healer
import random

all_pools = [
    heroes_pool_bruisers, heroes_pool_healer, heroes_pool_ma, heroes_pool_ra,
    heroes_pool_support, heroes_pool_tanks             
]

def create_team():
    team = []
    team_char_pool = []
    
    team_char_pool.append(random.choice(heroes_pool_tanks))
    team_char_pool.append(random.choice(heroes_pool_healer))


    while len(team_char_pool) < 15:
        random_pool = random.choice(all_pools)
        random_char = random.choice(random_pool)
        
        if random_char not in team_char_pool:
            team_char_pool.append(random_char)

    for i in range(5):
        player_pool = team_char_pool[i * 3:(i + 1) * 3]
        team.append(player_pool)
    
    return team

team1 = create_team()
team2 = create_team()
print(f'Team 1 Composed of: {team1}')
print(f'Team 2 Composed of: {team2}')