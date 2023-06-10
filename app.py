import os
from flask import(
    Flask,
    request,
    render_template)
from search import  GetArtistURL
from search import GetSongURL
from search_youtube import get_video

app= Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
   return render_template('index.html')

@app.route('/words',methods=['GET','POST'])
def words():
    return render_template('words.html')

@app.route('/search', methods=['GET','POST'])
def search():
  if request.method == 'POST':
    artist_name= request.form['artist']
    lyrics=request.form['lyric']
    song_url, title= GetSongURL(GetArtistURL(artist_name),lyrics)
    keyword=(title,artist_name)
    data = get_video(keyword)
    for video in data:
       youtube_url=str('https://www.youtube.com/watch?v=')+str(video['id']['videoId'])
    return render_template('results.html',song_url=song_url,title=title,artist_name=artist_name, youtube_url=youtube_url)
if __name__ == "__main__":
    app.run(debug=True)

