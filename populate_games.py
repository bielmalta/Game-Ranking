from games.models import Game

games = [
    {
        "title": "Elden Ring",
        "description": "RPG de ação desafiador em mundo aberto",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/b/b9/Elden_Ring_Box_art.jpg"
    },
    {
        "title": "God of War",
        "description": "Kratos enfrenta a mitologia nórdica",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/a/a7/God_of_War_4_cover.jpg"
    },
    {
        "title": "The Witcher 3",
        "description": "RPG com foco em história e escolhas",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/0/0c/Witcher_3_cover_art.jpg"
    },
    {
        "title": "GTA V",
        "description": "Mundo aberto caótico com múltiplos personagens",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/a/a5/Grand_Theft_Auto_V.png"
    },
    {
        "title": "Red Dead Redemption 2",
        "description": "Faroeste com história profunda",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/4/44/Red_Dead_Redemption_II.jpg"
    },
    {
        "title": "Minecraft",
        "description": "Sandbox de construção e sobrevivência",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/5/51/Minecraft_cover.png"
    },
    {
        "title": "Dark Souls III",
        "description": "RPG extremamente desafiador",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/b/bb/Dark_souls_3_cover_art.jpg"
    },
    {
        "title": "Cyberpunk 2077",
        "description": "RPG futurista em mundo aberto",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/9/9f/Cyberpunk_2077_box_art.jpg"
    },
    {
        "title": "FIFA 23",
        "description": "Simulador de futebol realista",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/e/e0/FIFA_23_Cover.jpg"
    },
    {
        "title": "Hollow Knight",
        "description": "Metroidvania com arte desenhada à mão",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/0/04/Hollow_Knight_first_cover_art.webp"
    },
    {
        "title": "The Last of Us",
        "description": "Jogo de sobrevivência com história emocional",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/8/86/The_Last_of_Us_cover.jpg"
    },
    {
        "title": "Assassin’s Creed Valhalla",
        "description": "Aventura viking em mundo aberto",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/a/a5/Assassin%27s_Creed_Valhalla_cover.jpg"
    }
]

for g in games:
    if not Game.objects.filter(title=g["title"]).exists():
        Game.objects.create(**g)