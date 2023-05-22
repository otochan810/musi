import os
from flask import(
    Flask,
    request,
    render_template)
from search import  (
    GetArtistURL,
    GetSongURL)

app= Flask(__name__)

def words():
    return render_template('word.html')

if __name__ == "__main__":
    app.run(debug=True)