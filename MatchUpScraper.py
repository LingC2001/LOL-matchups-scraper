from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

class MatchUpScraper:
    def __init__(self, champ1, champ2, lane):
        """
        initialises the web scraper for lolalytics website for the given matchup and lane
        :Input:
            champ1: Name of champion 1 as a string
            champ2: Name of champion 2 as a string
            lane: The lane for the matchup as a string. One of ["top", "jungle", "middle", "bottom", "support"]
        """
        self.url = f"https://lolalytics.com/lol/{champ1}/vs/{champ2}/build/?lane={lane}&vslane={lane}"
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
        self.soup.find_all("p", class_="lolx-links px-2 text-justify text-[14px] leading-normal text-white sm:px-0")
        