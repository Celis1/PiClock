import pytube
import vlc
import time
import vlc

class MusicStreamer:
    def __init__(self) -> None:
        self.music_path = './DATA/MusicData'

    def play_song(self, youtube_url, start_time = 0):
        audio_url, info = self.load_song(youtube_url)
        
        # Initialize the media player
        player = self.create_vlc(audio_url)
        player.play()

        # Set the start time to 1 minute (60 seconds)
        if start_time != 0:
            player.set_time(start_time * 1000)  # Time is specified in milliseconds

        # Wait for the video to finish
        while player.get_state() != vlc.State.Ended:
            pass

        # Release the media player
        player.release()

    def load_song(self, youtube_url):
        # Create a Pytube YouTube object
        yt = pytube.YouTube(youtube_url)

        # Choose the audio stream with the highest quality
        audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

        # Get the title of the video
        video_title = yt.title
        print(video_title)

        # Get the author (uploader) of the video
        video_author = yt.author
        print(video_author)

        info = {'title': video_title, 'author': video_author}

        # Get the audio stream URL
        audio_url = audio_stream.url

        return audio_url, info

    def create_vlc(self, audio_url):
        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new(audio_url)

        Media.get_mrl()
        player.set_media(Media)
        return player

    def download_song(self, youtube_url):
        # Download the video using Pytube
        yt = pytube.YouTube(youtube_url)
        video_stream = yt.streams.filter(file_extension='mp4').first()
        video_stream.download(self.music_path)
        return True



if __name__ == "__main__":
    streamer = MusicStreamer()
    # streamer.play_song('https://www.youtube.com/watch?v=YU-m46on_bQ', 130)
    streamer.download_song('https://www.youtube.com/watch?v=YU-m46on_bQ')