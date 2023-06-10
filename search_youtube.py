from apiclient.discovery import build


API_KEY='AIzaSyDUq6v0kcn3izf6UybEu5hbq-myuWW5OSM'
YOUTUBE_API_SERVICE_NAME='youtube'
YOUTUBE_API_VERSION='v3'

youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey=API_KEY
)

def get_video(keyword):

    youtube_query=youtube.search().list(
        part='id',
        q= keyword,
        type='video',
        maxResults=1,
        order='relevance'
    )

    youtube_response=youtube_query.execute()

    return youtube_response.get('items',[])
data=get_video('AI Story')

for video in data:
    youtube_url= str('https://www.youtube.com/watch?v=')+str(video['id']['videoId'])