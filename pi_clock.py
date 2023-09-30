from Clock import TrackingClock
from YT_Music import MusicStreamer

import time


class PiClock:

    def __init__(self) -> None:
        self.clock = TrackingClock()
        self.yt_music = MusicStreamer()
    
        self.wake_hour = 7
        self.sleep_hour = 0
        self.asleep = False

        self.wake_url = 'https://www.youtube.com/watch?v=h8nIHZ-0kS4'
        self.sleep_url = 'https://www.youtube.com/watch?v=teIbh8hFQos'


    def start(self):
        '''
        Function for starting the clock
        '''
        # TODO : Add a function to play music
        # check if your awake or asleep
        pass

    def update_time(self):
        '''
        Function for updating the time
        '''
        curr_time = self.clock.get_time()
        day_progress, day_left = self.clock.get_day_progress()
        month_progress, month_left = self.clock.month_progress()
        year_progress, year_left = self.clock.year_progress()
        deadline_progress, deadline_left = self.clock.deadline_progress()

        info = {
            'time': curr_time,
            'day_progress': day_progress,
            'day_left': day_left,
            'month_progress': month_progress,
            'month_left': month_left,
            'year_progress': year_progress,
            'year_left': year_left,
            'deadline_progress': deadline_progress,
            'deadline_left': deadline_left
        }

        return info
    
    def wake_up(self):
        '''
        Function for waking up the user
        '''
        if self.asleep:
            self.asleep = False

        self.yt_music.play_song(self.wake_url, 3)
        time.sleep(120)

        
        
    def go_sleep(self):
        if not self.asleep:
            self.asleep = True

        self.yt_music.play_song(self.sleep_url, 3)
        time.sleep(29)



if __name__ == '__main__':
    game = PiClock()
    # game.wake_up()
    game.go_sleep()