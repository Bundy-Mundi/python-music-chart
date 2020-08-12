from bs4 import BeautifulSoup

def extract_melon(req, up_to):
    songs = []

    full_doc = req.find("tbody")
    titles = full_doc.find_all("div", {"class":"ellipsis rank01"})
    artists = full_doc.find_all("div", {"class":"ellipsis rank02"})
    ranks = full_doc.find_all("span", {"class": "rank"})
    images = full_doc.find_all("a", {"class": "image_typeAll"})

    for r in range(0, up_to):
      title = titles[r].find("a").string
      artist = artists[r].find("a").string
      rank = ranks[r].string
      songs.append(
        {
          "title": title, 
          "artist": artist,
          "rank": rank,
          "img": images[r].find("img")["src"],
          "index": r
        })
    return songs