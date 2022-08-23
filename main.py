from downloadYoutube import downloadYouTube
from requests import session
from re import findall
ss = session()
def get_video_link(linkPlaylist):
    sourcPage = ss.get(linkPlaylist)
    if sourcPage.status_code == 200:
        links = findall(r'webCommandMetadata(.*?)webPageType',sourcPage.text)
        for i in links:
            if 'watch' in i:
                urlVideo = i.split('":{"url":"')[1].split('","')[0]
                if 'index' in urlVideo:
                    linkDownload = 'https://www.youtube.com'+urlVideo.replace('\\u0026','&')
                    print(f'Đang Download: {linkDownload}')
                    downloadYouTube(linkDownload)
                    print(f'Download Done: {linkDownload}')
linkPlaylist = input('Enter Youtube Playlist Link: ')
get_video_link(linkPlaylist)