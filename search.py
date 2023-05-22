from bs4 import BeautifulSoup
import requests
import urllib
import urllib.parse

def GetArtistURL(artist_name):
    #アーティスト名をURLに入れるための処理
    name_quote = urllib.parse.quote(artist_name)
    #URLを指定し、Webページを取得
    base_url = 'https://www.uta-net.com/search/?target=art&type=in&Keyword=' + name_quote
    response = requests.get(base_url)
    #文字化けが起こらないようにする
    response.encoding = response.apparent_encoding
    #Webページを解析する
    bs = BeautifulSoup(response.text, 'html.parser')

    #アーティスト名の検索結果を取得

    span_tag_list = bs.find_all('span', class_='fw-bold')

    #入力したアーティスト名と完全一致する要素を取り出す
    artist_number =0
    for artist in span_tag_list:
      if artist_name in artist.text:
        break
      artist_number += 1

    #①↑で取得したartist_numberに対応するアーティストID(href要素)を取得 (例：「AI」というアーティストの場合、href要素が「/artist/38/」)

    td_tag_list = bs.find_all('td',class_='pt-2')
    a_tag = td_tag_list[artist_number].find('a')
    href = a_tag.get('href')

    #② ①で取得したhref要素（「AI」の場合「/artist/38/」）を、returnで返す
    return href


def GetSongURL(artist_ID, Lyrics):
    artist_url = 'https://www.uta-net.com/' + artist_ID

    #アーティストのページに飛ぶ
    response = requests.get(artist_url)

    #文字化けが起こらないようにする
    response.encoding = response.apparent_encoding
    #Webページを解析する
    bs = BeautifulSoup(response.text, 'html.parser')

    #歌詞を取得
    span_tag_list = bs.find_all('span', class_='d-block d-lg-none utaidashi text-truncate')

    #歌詞のうち、入力と一致する要素を含むものを抽出
    song_number = 0
    for song in span_tag_list:
      if Lyrics in song.text:
        break
      song_number += 1

    #③↑で取得したsong_numberに対応する歌のURLを取得
    td_tag_list= bs.find_all('td', class_='sp-w-100 pt-0 pt-lg-2')
    a_tag = td_tag_list[song_number].find('a')
    href=a_tag.get('href')
    song_url='https://www.uta-net.com'+ href

    #曲名を取得
    span_tag_list = bs.find_all('span', class_='fw-bold songlist-title pb-1 pb-lg-0')
    title = span_tag_list[song_number].text

    #④ ③で取得したURLと曲名をreturnで返す
    return song_url,title

print(GetSongURL(GetArtistURL('AI'), '私がキミを守るから'))

