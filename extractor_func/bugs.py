from bs4 import BeautifulSoup

def extract_bugs(req, r):
  songs = []
  full_doc = req.find("tbody")
  titles = full_doc.find_all("p", {"class":"title"})
  artists = full_doc.find_all("p", {"class":"artist"})
  ranks = full_doc.find_all("div", {"class": "ranking"})
  images = full_doc.find_all("a", {"class": "thumbnail"})
  for r in range(0, r):
    title = titles[r].find("a").string
    artist = artists[r].find("a").string
    rank = ranks[r].find("strong").string
    songs.append(
      {
        "title": title,
        "artist": artist,
        "rank": rank,
        "img":images[r].find("img")["src"],
        "index": r
      })
  return songs