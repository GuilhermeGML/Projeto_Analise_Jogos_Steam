import requests
import pandas as pd
from tqdm import tqdm

def get_steam_game_details(appid):
    url = f"https://store.steampowered.com/api/appdetails?appids={appid}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data[str(appid)]['success']:
            return data[str(appid)]['data']
    return None

# Pegando todos os jogos disponíveis no SteamSpy
steamspy_url = "https://steamspy.com/api.php?request=all"
games_data = requests.get(steamspy_url).json()

jogos = []

# Processar os jogos por categoria
for game in tqdm(games_data.values()):
    appid = game["appid"]
    detalhes = get_steam_game_details(appid)
    if not detalhes:
        continue

    generos = [g["description"] for g in detalhes.get("genres", [])]
    if "Roguelike" not in generos:
        continue

    jogo = {
        "id_jogo": appid,
        "nome": detalhes.get("name"),
        "data_lancamento": detalhes.get("release_date", {}).get("date"),
        "desenvolvedor": detalhes.get("developers", [None])[0],
        "publicadora": detalhes.get("publishers", [None])[0],
        "generos": ", ".join(generos),
        "categorias": ", ".join([c["description"] for c in detalhes.get("categories", [])]),
        "plataformas": ", ".join([p for p, v in detalhes.get("platforms", {}).items() if v]),
        "preco": detalhes.get("price_overview", {}).get("final", 0) / 100 if detalhes.get("is_free") is False else 0.0,
        "moeda": detalhes.get("price_overview", {}).get("currency") if detalhes.get("price_overview") else "FREE",
        "jogadores_atuais": None
    }
    jogos.append(jogo)

    if len(jogos) >= 50:
        break

df = pd.DataFrame(jogos)
df.to_csv("steam_jogos_rogueliker.csv", index=False, encoding="utf-8-sig")

print("Arquivo CSV salvo com sucesso com", len(df), "jogos Roguelike.")
