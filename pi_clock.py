from Clock import TrackingClock
from YT_Music import MusicStreamer

import time
import threading
from datetime import datetime


class PiClock:

    def __init__(self) -> None:
        self.clock = TrackingClock()
        self.yt_music = MusicStreamer()
    
        # TODO : add this to sleep clock class
        self.wake_hour = datetime.now().replace(hour=7, minute=0)
        self.sleep_hour = datetime.now().replace(hour=0, minute=30)
        self.asleep = False
        self.keep_playing = False

        self.wake_url = 'https://www.youtube.com/watch?v=h8nIHZ-0kS4'
        self.sleep_url = 'https://www.youtube.com/watch?v=teIbh8hFQos'


    def start(self):
        '''
        Function for starting the clock
        '''
        # TODO : add this to sleep clock class
        curr_time = datetime.now()
        if self.clock.in_between(curr_time, self.sleep_hour, self.wake_hour):
            self.asleep = True
        else:
            self.asleep = False

    def update_time(self):
        '''
        Function for updating the time
        '''
        curr_formatted_time = self.clock.get_time()
        day_progress, day_left = self.clock.get_day_progress()
        month_progress, month_left = self.clock.month_progress()
        year_progress, year_left = self.clock.year_progress()
        deadline_progress, deadline_left = self.clock.deadline_progress()


        # TODO: add this to sleep clock class
        # wake_up_bool = self.check_time()

        info = {
            'time': curr_formatted_time,
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
    
    def check_alarm(self):
        '''
        Function for checking the time
        '''
        
        # TODO: add this to sleep clock class
        curr_time = datetime.now()

        if (curr_time.minute == self.wake_hour.minute and
        curr_time.hour == self.wake_hour.hour and self.asleep):
            self.asleep = False
            self.wake_up()
            return True

        elif (curr_time.minute == self.sleep_hour.minute and
        curr_time.hour == self.sleep_hour.hour and not self.asleep):
            self.asleep = True
            self.go_sleep()
            return False

        else:
            return False
    
    def wake_up(self):
        '''
        Function for waking up the user
        '''
        # create a thread for playing music
        self.yt_music.play_song(self.wake_url, 3)
        # add more here
        
    def go_sleep(self):
        self.yt_music.play_song(self.sleep_url, 3, 29)
        # add more here



if __name__ == '__main__':
    game = PiClock()
    # game.wake_up()
    game.go_sleep()