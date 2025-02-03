import pandas as pd
from MatchUpScraper import MatchUpScraper
import argparse

class DataCompiler:
    def __init__(self):
        """
        Initialise data compiler that creates a dataframe and stores information regarding matchups
        """
        self.own_champs = ["Riven", "Mordekaiser", "Ambessa", "Volibear", "Pantheon", "Galio", "Aatrox", "Malphite", "Camille", "Jax", "Viktor"]
        self.toplane_champs = ["Aatrox", "Akali", "Ambessa", "Aurora", "Camille", "Cassiopeia", "ChoGath", "Darius", "DrMundo", "Fiora", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Gwen", "Heimerdinger", "Illaoi", "Irelia", "Jax", "Jayce", "KSante", "Karma", "Kayle", "Kennen", "Kled", "Malphite", "Maokai", "Mordekaiser", "Nasus", "Olaf", "Ornn", "Pantheon", "Poppy", "Quinn", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Sett", "Shen", "Singed", "Sion", "Smolder", "Swain", "Sylas", "TahmKench", "Teemo", "Trundle", "Tryndamere", "Udyr", "Urgot", "Varus", "Vayne", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Yasuo", "Yone", "Yorick", "Zac"]
        self.df = pd.DataFrame(columns=["Champion"]+self.own_champs)

    def get_winrate(self, mode):
        """
        Class method to extract the winrate values for each own_champ vs toplane_champ
        Input:
            mode: string to specify the winrate type/mode (base, delta1, delta2)
        """
        for champ2 in self.toplane_champs:
            row = [champ2]
            for champ1 in self.own_champs:
                if champ1 != champ2:
                    scraper = MatchUpScraper(champ1=champ1, champ2=champ2, lane="top", tier="all", patch="15.1")
                    if mode == "base":
                        winrate = scraper.get_winrate()
                    elif mode == "delta1":
                        winrate = scraper.get_winrate_delta1()
                    elif mode == "delta2":
                        winrate = scraper.get_winrate_delta2()
                    row.append(winrate)
                else:
                    row.append(0)
            self.df.loc[len(self.df)] = row

    def write_to_file(self, file_name):
        """
        Write to excel file
        """
        self.df.to_excel(file_name, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="SpreadsheetCreator",
                                     description="Compiles a spreadsheet matchup analysis of all league of legends top lane champions")
    parser.add_argument("--key", type=str)
    parser.add_argument("--filename", default="matchups.xlsx", type=str)
    args = parser.parse_args()
    key = args.key
    filename = args.filename
    print(f"Creating spreadsheet '{filename}' based on key={key}")
    compiler = DataCompiler()
    compiler.get_winrate(mode=key)

    compiler.write_to_file(filename)
        
