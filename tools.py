import re

class tools:
    fractals = {
        "Aetherblade": [14, 46, 65, 71, 96],
        "Aquatic Ruins": [7, 26, 61, 76],
        "Captain Mai Trin Boss": [18, 42, 72, 95],
        "Chaos": [13, 30, 38, 63, 88, 97],
        "Cliffside": [6, 21, 47, 69, 94],
        "Deepstone": [11, 33, 67, 84],
        "Molten Boss": [10, 40, 70, 90],
        "Molten Furnace": [9, 22, 39, 58, 83],
        "Nightmare": [23, 48, 73, 98],
        "Shattered Observatory": [24, 49, 74, 99],
        "Siren's Reef": [12, 37, 54, 78],
        "Snowblind": [3, 27, 51, 68, 86, 93],
        "Sunqua Peak": [25, 50, 75, 100],
        "Solid Ocean": [20, 35, 45, 60, 80],
        "Swampland": [5, 17, 32, 56, 77, 89],
        "Thaumanova Reactor": [15, 34, 43, 55, 64, 82],
        "Twilight Oasis": [16, 41, 59, 87],
        "Uncategorized": [2, 36, 44, 62, 79, 91],
        "Underground Facility": [8, 29, 53, 81],
        "Urban Battleground": [4, 31, 57, 66, 85],
        "Volcanic Fractal": [1, 19, 28, 52, 92],
    }

    def splitFractals(self,list):
        daily = []
        recs_temp = []
        recs = []

        [daily.append(e.replace("Daily Tier 4 ","")) for e in list if "Daily Tier 4" in e]
        [recs_temp.append(e[-2:]) for e in list if "Recommended" in e]
        [recs.append(f"{e} {k}") for k, v in self.fractals.items() for e in recs_temp if int(e) in v]
        recs.sort()

        return daily, recs

class emojis:
    #Emojis
    daily_pve = 778725530345144341
    daily_pvp = 778733003417059439
    daily_fractals = 778738389515632681
    daily_fractals_recs = 778738389741862942