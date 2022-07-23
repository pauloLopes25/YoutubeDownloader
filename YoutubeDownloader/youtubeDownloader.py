from pytube import YouTube
from pytube import Playlist


def download(option1, option2):
    if option1 == 'Video' and option2 == 'Audio':
        url = input("Por favor insira o url do audio:\n")
        try:
            yt = YouTube(url).streams.get_audio_only()
        except:
            print('********************************************')
            print(f'Video: {url} nao existente ou url é invalido')
            print('********************************************')
        else:
            print(f'Downloading: {yt.title}')
            yt.download()
            print(f'done')
    
    if option1 == 'Video' and option2 == 'Video':
        url = input("Por favor insira o url do video: \n")
        try:
            yt = YouTube(url).streams.get_highest_resolution()
        except:
            print('********************************************')
            print(f'Video: {url} nao existente ou url é invalido')
            print('********************************************')
        else:
            print(f'Downloading: {yt.title}')
            dw = yt.download()
            print('done')
        
    if option1 == 'PlayList' and option2 == 'Audio':
        url = input("Por favor insira o url da Playlist: \n")
        try:
            p = Playlist(url)
        except:
            print('********************************************')
            print(f'PlayList: {url} nao existente ou url é invalido')
            print('********************************************')
        else:
            print(f'Downloading PlayList: {p.title}')
            for video in p.videos:
                print(f"Downloading: {video.title}")
                video.streams.get_audio_only().download()
                print("done")

    if option1 == 'PlayList' and option2 == 'Video':
        url = input("Por favor insira o url da Playlist: \n")
        try:
            p = Playlist(url)
        except: 
            print('********************************************')
            print(f'Video: {url} nao existente ou url é invalido!')
            print('********************************************')
        else:
            print('********************************************')
            print(f'Downloading PlayList: {p.title}')
            print('********************************************')
            for video in p.videos:
                print(f"Downloading: {video.title}")
                video.streams.get_highest_resolution().download()
                print("done")


while True:
    option1 = input(f"Deseja fazer download de apenas um (Video) ou uma (PlayList)?\n")
    option2 = input(f"Por favor insira qual a opção desejada de download (Audio) ou (Video):\n")
    download(option1, option2)



