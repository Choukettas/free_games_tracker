import requests
import json
import time
from datetime import datetime

url = "https://www.gamerpower.com/api/giveaways"
webhook_url = "https://discord.com/api/webhooks/XXXXXXXXXXXX"

params_steam_game = {
    "platform": "steam",
    "type": "game"
}

print("Bot lancé...")

while True:
    try:
        # ======================
        # STEAM — GAME
        # ======================
        r = requests.get(url, params=params_steam_game, timeout=5)
        r.raise_for_status()
        data = r.json()

        with open("./data/steam_game.json", "w", encoding="utf-8") as fichier:
            json.dump(data, fichier, indent=4, ensure_ascii=False)

        if data and isinstance(data, list):
            d = data[0]

            title = d.get("title")
            open_giveaway = d.get("open_giveaway")
            image = d.get("image")
            worth = d.get("worth")
            description = d.get("description")
            end_date = d.get("end_date")

            payload = {
                "embeds": [
                    {
                        "title": title,
                        "description": (
                            f"{description}\n\n"
                            f"~~{worth}~~ **Gratuit jusqu’au {end_date}**\n"
                            f"🔗 [Ouvrir dans la boutique]({open_giveaway})"
                        ),
                        "color": 0x7F00FF,
                        "footer": {
                            "text": "by choukettas"
                        },
                        "timestamp": datetime.utcnow().isoformat(),
                        "image": {
                            "url": image
                        },
                        "thumbnail": {
                            "url": "https://i.postimg.cc/hjrPkWbj/S2Qw-Qtm.png"
                        }
                    }
                ]
            }

            requests.post(webhook_url, json=payload)
            print(f"[OK] {title} envoyé")

        else:
            print("Aucune donnée valide")

    except Exception as e:
        print("Erreur :", e)

    # ⏳ pause 30 minutes
    time.sleep(1800)
