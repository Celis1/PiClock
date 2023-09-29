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

# Get the audio stream URL
audio_url = audio_stream.url

# Specify the full path to the VLC executable on macOS
# vlc_path = "/Applications/VLC.app/Contents/MacOS/VLC"

Instance = vlc.Instance()#(f"--no-xlib --quiet --fullscreen --ignore-config --plugin-path")
player = Instance.media_player_new()
Media = Instance.media_new(audio_url)

Media.get_mrl()
player.set_media(Media)

# Initialize the media player
player.play()

# Wait for the player to start
time.sleep(1)

# Set the start time to 1 minute (60 seconds)
player.set_time(110 * 1000)  # Time is specified in milliseconds

# Wait for the video to finish
while player.get_state() != vlc.State.Ended:
    pass

# Release the media player
player.release()
