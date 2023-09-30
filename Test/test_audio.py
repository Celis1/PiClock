import pytube
import vlc
import os
import time
import vlc

# Replace with the YouTube video URL you want to stream
video_url = 'https://www.youtube.com/watch?v=YU-m46on_bQ'


# Create a Pytube YouTube object
yt = pytube.YouTube(video_url)

# Choose the audio stream with the highest quality
audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

# Get the title of the video
video_title = yt.title
print(video_title)

# Get the author (uploader) of the video
video_author = yt.author
print(video_author)

# Get the audio stream URL
audio_url = audio_stream.url

# Specify the full path to the VLC executable on macOS
# vlc_path = "/Applications/VLC.app/Contents/MacOS/VLC"

download_path = '/Users/celis/Projects/Kivy/PiClock/DATA/MusicData/Songs/GoldLink-Crew_REMIX.mp4'
Instance = vlc.Instance("--no-video")
player = Instance.media_player_new()
Media = Instance.media_new(audio_url)

Media.get_mrl()
player.set_media(Media)

# Initialize the media player
player.play()

# Wait for the player to start
time.sleep(1)

# Define initial volume (0 to 100)
initial_volume = 50
player.audio_set_volume(initial_volume)

# Set the start time to 1 minute (60 seconds)
player.set_time(110 * 1000)  # Time is specified in milliseconds

# Wait for the video to finish
# while player.get_state() != vlc.State.Ended:
#     pass

time.sleep(10)

# Release the media player
player.release()
