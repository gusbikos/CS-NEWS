from app.config import FACEIT_API_KEY
import requests

BASE_URL = "https://open.faceit.com/data/v4"
headers = {"Authorization": f"Bearer {FACEIT_API_KEY}"}

def search_team_by_name(nickname):
    endpoint = "/teams"
    params = {"nickname": nickname}
    
    response = requests.get(
        f"{BASE_URL}{endpoint}",
        headers=headers,
        params=params
    )
    
    if response.status_code == 200:
        data = response.json()
        return data.get("items", [])
    else:
        print(f"Error {response.status_code}: {response.text}")
        return []
    
    
def search_player_by_nickname(nickname):
    endpoint = "/players"
    params = {"nickname": nickname}
    
    response = requests.get(
        f"{BASE_URL}{endpoint}",
        headers=headers,
        params=params
    )
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
    
    
def get_player_league_details(league_id, season_id, player_id):
    endpoint = f"/leagues/{league_id}/seasons/{season_id}/players/{player_id}"
    
    response = requests.get(
        f"{BASE_URL}{endpoint}",
        headers=headers
    )
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
    


# # Example usage
# team_nickname = "Lemon Party"
# teams = search_team_by_nickname(team_nickname)

# if teams:
#     for team in teams:
#         print(f"Team Name: {team['name']}, Team ID: {team['team_id']}")
# else:
#     print("No teams found.")
