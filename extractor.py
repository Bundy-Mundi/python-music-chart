from bs4 import BeautifulSoup
import requests
import json
from extractor_func import melon, bugs, billboard
from search_api import search_youtube

class Extractor:
    def __init__(self):
        self.melon_url = "https://www.melon.com/chart/day/index.htm"
        self.bugs_url = "https://music.bugs.co.kr/chart"
        self.billboard_url = "https://www.billboard.com/charts/hot-100"
        self.Chart = Extractor.Chart(self)
    def __str__(self):
        return f"Using Websites URLs: \n\nKorea\nMelon: {self.melon_url}\nBugs: {self.bugs_url}\n\nAmerica\nBillboard: {self.billboard_url}"
    
    def search_youtube(self, artist, song_title):
        query = f"{artist} {song_title}"
        raw_result = search_youtube(query=query)
        result = self.json_parser(raw_result)
        return result

    def html_parser(self, html_doc):
        result = BeautifulSoup(html_doc, "html.parser")
        return result
    def json_parser(self, any):
        result = json.dumps(any)
        return result

    class Chart:
        """ Every Chart Functions Here """
        def __init__(self, parent):
            self.parent = parent
        def __str__(self):
            return ("Chart Class")
        
        def melon_chart(self, up_to = 100):
            req = requests.get(url=self.parent.melon_url, headers = {"User-Agent": "XY"} )
            raw_result = melon.extract_melon(self.parent.html_parser(req.text), up_to=up_to)
            result = self.parent.json_parser(raw_result)
            return result
        def bugs_chart(self, up_to = 100):
            req = requests.get(url=self.parent.bugs_url, headers = {"User-Agent": "XY"} )
            raw_result = bugs.extract_bugs(self.parent.html_parser(req.text), up_to=up_to)
            result = self.parent.json_parser(raw_result)
            return result
        def billboard_chart(self, up_to = 100):
            req = requests.get(url=self.parent.billboard_url, headers = {"User-Agent": "XY"} )
            raw_result = billboard.extract_billboard(self.parent.html_parser(req.text), up_to=up_to)
            result = self.parent.json_parser(raw_result)
            return result
