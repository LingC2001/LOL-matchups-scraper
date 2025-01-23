import pandas as pd
from MatchUpScraper import MatchUpScraper

class DataCompiler:
    def __init__(self):
        """
        Initialise data compiler that creates a dataframe and stores information regarding matchups
        """
        self.own_champs = ["Riven", "Mordekaiser", "Ambessa", "Volibear", "Galio", "Aatrox", "Malphite", "Camille", "Jax", "Viktor"]
        self.toplane_champs = ["Aatrox", "Akali", "Ambessa", "Aurora", "Camille", "Cassiopeia", "ChoGath", "Darius", "DrMundo", "Fiora", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Gwen", "Heimerdinger", "Illaoi", "Irelia", "Jax", "Jayce", "KSante", "Karma", "Kayle", "Kennen", "Kled", "Malphite", "Maokai", "Mordekaiser", "Nasus", "Olaf", "Ornn", "Pantheon", "Poppy", "Quinn", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Sett", "Shen", "Singed", "Sion", "Smolder", "Swain", "Sylas", "TahmKench", "Teemo", "Trundle", "Tryndamere", "Udyr", "Urgot", "Varus", "Vayne", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Yasuo", "Yone", "Yorick", "Zac"]
        self.df = pd.DataFrame(columns=["Champion"]+self.own_champs)

    def get_delta2(self):
        """
        Class method to extract the delta2 values for each own_champ vs toplane_champ
        """
        for champ2 in self.toplane_champs:
            row = [champ2]
            for champ1 in self.own_champs:
                if champ1 != champ2:
                    scraper = MatchUpScraper(champ1=champ1, champ2=champ2, lane="top", patch="15.1")
                    delta2 = scraper.get_winrate_delta2()
                    row.append(delta2)
                else:
                    row.append(0)
            self.df.loc[len(self.df)] = row

    def write_to_file(self, file_name):
        """
        Write to excel file
        """
        self.df.to_excel(file_name, index=False)

if __name__ == "__main__":
    compiler = DataCompiler()
    compiler.get_delta2()
    print(compiler.df)
    compiler.write_to_file("matchups.xlsx")
        
