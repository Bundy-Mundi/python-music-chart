from bs4 import BeautifulSoup

def extract_billboard(req, r):
    songs = []
    full_doc = req.find("ol", {"class":"chart-list__elements"})
    titles = full_doc.find_all("span", {"class":"chart-element__information__song"})
    artists = full_doc.find_all("span", {"class":"chart-element__information__artist"})
    ranks = full_doc.find_all("span", {"class": "chart-element__rank__number"})
  
    for r in range(0, r):
      title = titles[r].string
      artist = artists[r].string
      rank = ranks[r].string
      songs.append(
        {
          "title":title,
          "artist": artist,
          "rank": rank,
          "index": r
        })
    
    return songs