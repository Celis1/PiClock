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
        self.yt_music = MusicStreamer()
        self.workout = WorkoutTracker()
        # TODO : need a way to allow this to fail without breaking system
        self.weather = WeatherTracker('./config.ini')
    
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

        # TODO : fetch the current weather so we can update the app later


    # TODO : move this to clock.py
    def update_time(self):
        '''
        Function for updating the time
        '''
        curr_formatted_time = self.clock.get_time()
        day_progress, day_left = self.clock.get_day_progress()
        month_progress, month_left = self.clock.month_progress()
        year_progress, year_left = self.clock.year_progress()
        deadline_progress, deadline_left = self.clock.deadline_progress()


        info = {
            # TODO : this formated time is annoying, make a function to format for display
            'time': curr_formatted_time,
            'current_time': datetime.now(),
            'day_progress': day_progress,
            'day_left': day_left,
            'month_progress': month_progress,
            'month_left': month_left,
            'year_progress': year_progress,
            'year_left': year_left,
            'deadline_progress': deadline_progress,
            'deadline_left': deadline_left,
        }

        return info
    
    # TODO: add this to sleep clock class
    def check_alarm(self):
        '''
        Function for checking the time
        '''
        
        
        curr_time = datetime.now()

        if (curr_time.minute == self.sleep.wake_hour.minute and
        curr_time.hour == self.sleep.wake_hour.hour and self.sleep.asleep):
            self.sleep.asleep = False
            self.wake_up()
            return True

        elif (curr_time.minute == self.sleep.sleep_hour.minute and
        curr_time.hour == self.sleep.sleep_hour.hour and not self.sleep.asleep):
            self.sleep.asleep = True
            self.go_sleep()
            return False

        else:
            return False
    
    # TODO : we dont need a wake up and morning routine
    def wake_up(self):
        '''
        Function for waking up the user
        '''
        # TODO : there is probably going to be a wake up routine
        # create a thread for playing music
        self.yt_music.play_song(self.wake_url, 3)
        # add more here
        
    def go_sleep(self):
        # TODO : there is probably going to be a sleep routine
        self.yt_music.play_song(self.sleep_url, 3, 29)
        # add more here

    def start_morning_routine(self):
        '''
        Function for starting the morning routine
        '''
        if self.weather.update_weather():
            info = {}
            time_info = self.update_time()
            weather_info = self.weather()

            # TODO : find a better way than this
            info.update(time_info)
            info.update(weather_info)

            # tts.speak(info)
            threading.Thread(target=tts.speak, args=(info,)).start()



if __name__ == '__main__':
    game = LifeClock()
    # game.wake_up()
    game.go_sleep()



