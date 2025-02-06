from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from re import findall

class MatchUpScraper:
    def __init__(self, champ1, champ2, lane, tier, patch=None):
        """
        initialises the web scraper for lolalytics website for the given matchup and lane
        :Inputs:
            champ1: Name of champion 1 as a string
            champ2: Name of champion 2 as a string
            lane: The lane for the matchup as a string. One of ["top", "jungle", "middle", "bottom", "support"]
            tier: Which tiers to get the data from. E.g. ["all", "master_plus", "diamond_plus"]
            patch: The patch version for the data       
        """
        print(f"{champ1} vs {champ2}")
        if patch:
            self.url = f"https://lolalytics.com/lol/{champ1.lower()}/vs/{champ2.lower()}/build/?lane={lane.lower()}&vslane={lane.lower()}&tier={tier.lower()}&patch={patch}"
        else: # latest patch if no patch version is specified
            self.url = f"https://lolalytics.com/lol/{champ1.lower()}/vs/{champ2.lower()}/build/?lane={lane.lower()}&vslane={lane.lower()}&tier={tier.lower()}"
        
        self.req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        self.page = urlopen(self.req)
        self.html = self.page.read().decode("utf-8")
        self.soup = BeautifulSoup(self.html, "html.parser")
    
    def get_winrate_delta2(self):
        """
        Retrieve the delta 2 value for the winrate, which is the normalised winrate of champ1 vs champ2 compared
        to the average champion against champ2. E.g. If delta2 = 5 means champ1 has 5% higher winrate against champ2
        compared to the average champion against champ2, after both champions default winrates are considered.
        """
        data = self.soup.find("p", class_="lolx-links px-2 text-justify text-[14px] leading-normal text-white sm:px-0")
        text = data.get_text()
        winrates = findall(r"[-]?\d+[.,]?\d*", text)
        # print(winrates)
        return float(winrates[2])

    def get_winrate_delta(self):
        """
        Retrieve the delta value for the winrate
        """
        data = self.soup.find("p", class_="lolx-links px-2 text-justify text-[14px] leading-normal text-white sm:px-0")
        text = data.get_text()
        winrates = findall(r"[-]?\d+[.,]?\d*", text)
        return float(winrates[1])
    
    def get_winrate(self):
        """
        Retrieve the winrate of champ1 vs champ2
        """
        data = self.soup.find("p", class_="lolx-links px-2 text-justify text-[14px] leading-normal text-white sm:px-0")
        text = data.get_text()
        winrates = findall(r"[-]?\d+[.,]?\d*", text)
        return float(winrates[0])
