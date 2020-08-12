import dotenv 
import os
from googleapiclient.discovery import build
dotenv.load_dotenv()

def search_youtube(query):
    api_key = os.getenv("API_SECRET_KEY")
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(
        part='snippet',
        maxResults=1,
        q=query)
    response = request.execute()

    ID = response.get("items")[0].get("id").get("videoId")
    THUMBNAIL = response.get("items")[0].get("snippet").get("thumbnails").get("high").get("url")
    EMBED_LINK = f"https://youtube.com/embed/{ID}"

    result = {
        "id": ID, 
        "thumbnail": THUMBNAIL, 
        "embed_link": EMBED_LINK
      }
    return result
