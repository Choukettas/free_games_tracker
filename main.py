import requests


url = "https://www.gamerpower.com/api/giveaways"


params_steam_game = {
    "platform": "steam",
    "type": "game"
}

params_epicgame_game = {
    "platform": "epic-games-store",
    "type": "game"
}

params_steam_DLC = {
    "platform": "steam",
    "type": "loot"
}

params_epicgame_DLC = {
    "platform": "epic-games-store",
    "type": "loot"
}



# ======================
# STEAM — GAME
# ======================

r = requests.get(url, params=params_steam_game, timeout=5)
data = r.json()

if data and isinstance(data, list):
    print("title :", data[0].get("title"))
    print("worth :", data[0].get("worth"))
    print("image :", data[0].get("image"))
    print("type :", data[0].get("type"))
    print("published_date :", data[0].get("published_date"))
    print("end_date :", data[0].get("end_date"))
else:
    print("Pas de données valides.")



# ======================
# EPIC GAMES — GAME
# ======================

r = requests.get(url, params=params_epicgame_game, timeout=5)
data = r.json()

if data and isinstance(data, list):
    print("title :", data[0].get("title"))
    print("worth :", data[0].get("worth"))
    print("image :", data[0].get("image"))
    print("type :", data[0].get("type"))
    print("published_date :", data[0].get("published_date"))
    print("end_date :", data[0].get("end_date"))
else:
    print("Pas de données valides.")



# ======================
# STEAM — DLC
# ======================

r = requests.get(url, params=params_steam_DLC, timeout=5)
data = r.json()

if data and isinstance(data, list):
    print("title :", data[0].get("title"))
    print("worth :", data[0].get("worth"))
    print("image :", data[0].get("image"))
    print("type :", data[0].get("type"))
    print("published_date :", data[0].get("published_date"))
    print("end_date :", data[0].get("end_date"))
else:
    print("Pas de données valides.")



# ======================
# EPIC GAMES — DLC
# ======================

r = requests.get(url, params=params_epicgame_DLC, timeout=5)
data = r.json()

if data and isinstance(data, list):
    print("title :", data[0].get("title"))
    print("worth :", data[0].get("worth"))
    print("image :", data[0].get("image"))
    print("type :", data[0].get("type"))
    print("published_date :", data[0].get("published_date"))
    print("end_date :", data[0].get("end_date"))
else:
    print("Pas de données valides.")