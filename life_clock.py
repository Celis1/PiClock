from Tracking import ClockTracker, WorkoutTracker, SleepTracker, WeatherTracker
from YT_Music import MusicStreamer

# Importing TTS
from speech import TextToSpeech as tts

from datetime import datetime
import threading


class LifeClock:

    def __init__(self) -> None:
        # Importing trackers
        self.clock = ClockTracker()
        self.sleep = SleepTracker()
        self.workout = WorkoutTracker()
        # TODO : need a way to allow this to fail without breaking system
        self.weather = WeatherTracker('./config.ini')

        self.yt_music = MusicStreamer()

        # public variables
        self.keep_playing = False

        # TODO : this needs to be moved to the playlist class
        self.wake_url = 'https://www.youtube.com/watch?v=h8nIHZ-0kS4'
        self.sleep_url = 'https://www.youtube.com/watch?v=teIbh8hFQos'


    def start(self):
        '''
        Function for starting the clock
        '''
        # TODO : add functionality for if this is the first time running the app ever
        # figuring out if we should be asleep or not
        curr_time = datetime.now()
        if self.clock.in_between(curr_time, self.sleep.sleep_hour, self.sleep.wake_hour):
            self.sleep.asleep = True
        else:
            self.sleep.asleep = False

        # setting the clock 24hr cycle
        self.clock.day_start = self.sleep.sleep_hour.hour
        self.clock.day_end = self.sleep.wake_hour.hour

        # TODO : fetch the current weather so we can update the app

    def start_morning_routine(self):
        '''
        Function for starting the morning routine
        '''
        if self.weather.update_weather():
            info = {}
            time_info = self.clock()
            weather_info = self.weather()

            # TODO : find a better way than this
            info.update(time_info)
            info.update(weather_info)

            # tts.speak(info)
            print('---- start speaking ----')
            threading.Thread(target=tts.speak, args=(info,)).start()



if __name__ == '__main__':
    import time
    game = LifeClock()
    # game.wake_up()
    # game.go_sleep()
    game.start_morning_routine()




