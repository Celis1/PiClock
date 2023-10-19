import pytube
import vlc
import os
from time import sleep
import threading

class MusicStreamer:
    def __init__(self) -> None:
        self.music_path = './DATA/MusicData'
        self.player = None
        self.volumn = 70

    def set_volumn(self, volume):
        '''
        Function for setting the volume of the VLC media player

        volume: int from 0 to 100
        '''
        
        if self.player is not None:
            self.volumn = volume
            self.player.audio_set_volume(volume)
        else:
            print('No player is currently running')

    def play_song(self, youtube_url, start_time = 0, end_time = 0):
        '''
        Function for streaming a song from YouTube
        - youtube_url: The URL of the YouTube video or the path of a downloaded mp3/mp4 file
        '''
        audio_url, info = self._load_song(youtube_url)
        
        # Initialize the media player
        self.player = self._create_vlc(audio_url)
        self.player.play()

        self.player.audio_set_volume(self.volumn)
        # Set the start time to 1 minute (60 seconds)
        if start_time != 0:
            self.player.set_time(start_time * 1000)  # Time is specified in milliseconds

        if end_time != 0:
            # Create a Timer object to execute the function after the delay
            timer = threading.Timer(end_time, self.stop_song)

            # Start the timer
            timer.start()

        # Wait for the video to finish
        # while self.player.get_state() != vlc.State.Ended:
        #     pass

    def is_playing(self):
        '''
        Checks if the vlc player is currently active
        '''
        if self.player == None:
            return False
        if self.player.get_state() == vlc.State.Ended:
            return True
        else:
            return False

    def stop_song(self):
        # Release the media player
        if self.player == None:
            return False

        if self.player.get_state() != vlc.State.Ended:
            self.player.release()
            self.player = None
            return True
        return False

    def download_song(self, youtube_url):
        '''
        Download the video using Pytube
        '''
        # Create a Pytube YouTube object
        yt = pytube.YouTube(youtube_url)
        video_stream = yt.streams.filter(file_extension='mp4').first()

        # Get the title of the video and author to make saving easy
        video_author = yt.author.replace(' ', '_')
        default_name = video_stream.default_filename.replace(' ', '_')
        file_name = f'{video_author}-{default_name}'

        path = os.path.join(self.music_path, 'Songs')
        video_stream.download(path,file_name)
        return True
    
    def _load_song(self, youtube_url):
        '''
        Function for loading a song from YouTube
        '''
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

    def _create_vlc(self, audio_url):
        '''
        Function for creating a VLC media player object
        '''
        Instance = vlc.Instance("--no-video")
        player = Instance.media_player_new()
        Media = Instance.media_new(audio_url)

        Media.get_mrl()
        player.set_media(Media)
        return player





if __name__ == "__main__":
    import time
    streamer = MusicStreamer()
    download_url = 'https://www.youtube.com/watch?v=h8nIHZ-0kS4'
    streamer.play_song(download_url, 130)
    time.sleep(10)
    # streamer.download_song(download_url)