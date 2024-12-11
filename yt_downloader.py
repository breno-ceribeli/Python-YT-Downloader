from pytubefix import YouTube
from pytubefix.cli import on_progress

user_input = input("\033[31m(Digite 'audio' com um espaço de distância da url para baixar somente audio.)\033[0m\nDigite a \033[32mURL\033[0m do vídeo.\n")

input_parts = user_input.split(" ")

url = input_parts[0]
only_audio = len(input_parts) > 1 and input_parts[1].lower() == "audio"

try:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)

    yd = yt.streams.get_audio_only() if only_audio else yt.streams.get_highest_resolution()
    yd.download()
except Exception as e:
    print(f"Ocorreu um  erro: {e}")