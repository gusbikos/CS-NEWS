from typing import Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.faceit_api import search_team_by_name, search_player_by_nickname, get_player_league_details



app = FastAPI()

@app.get("/")
def root():
    return {"message": "FACEIT API is running"}


@app.get("/teams/{nickname}")
def get_team(nickname):
    teams = search_team_by_name(nickname)
    
    if not teams:
        raise HTTPException(
            status_code=404,
            detail="Team not found"
        )
    return teams


@app.get("/players/{nickname}")
def search_player(nickname: str):    
    player = search_player_by_nickname(nickname)
    
    if not player:
        raise HTTPException(
            status_code=404,
            detail="Player not found"
        )
    return player


@app.get("/leagues/{league_id}/seasons/{season_id}/players/{player_id}")
def get_league_info(league_id: str, season_id: int, player_id: str):    
    details = get_player_league_details(league_id, season_id, player_id)
    
    if not details:
        raise HTTPException(
            status_code=404,
            detail="League details for this player not found"
        )
    return details


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}