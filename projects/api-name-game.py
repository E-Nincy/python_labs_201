# Add an API call to your CLI game that assigns a name to your player.

import requests

min_len = 4
max_len = 6
URL = f"https://uzby.com/api.php?min={min_len}&max={max_len}"

response = requests.get(URL)
player_name = response.text.strip()

print(f"Your player name is: {player_name}")
