from datetime import datetime


# TODO : This class should be tracking stats on sleep time
class SleepTracker:
    
    def __init__(self) -> None:
        # fundamental variables
        self.wake_hour = datetime.now().replace(hour=7, minute=0)
        self.sleep_hour = datetime.now().replace(hour=0, minute=30)
        self.asleep = False

        # tracking differences between ideal and current
        self.current_sleep_time = 0
        self.today_sleep_hour = 0
        self.today_wake_hour = 0

    def set_sleep(self, sleep_time):
        '''
        Function for setting the time to go to sleep
        '''
        pass

    def set_wake(self, wake_time):
        '''
        Function for setting the time to wake up
        '''
        pass

    def go_sleep(self):
        '''
        Function for going to sleep
        '''
        pass

    def wake_up(self):
        '''
        Function for waking up
        '''
        pass