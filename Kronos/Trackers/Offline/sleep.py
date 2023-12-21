from datetime import datetime

# TODO : needs a way to turn off alarm for the next day

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

    def check_alarm(self):
        '''
        Function for checking the time
        '''
        curr_time = datetime.now()

        if (curr_time.minute == self.wake_hour.minute and
        curr_time.hour == self.wake_hour.hour and self.asleep):
            self.asleep = False
            return True

        elif (curr_time.minute == self.sleep_hour.minute and
        curr_time.hour == self.sleep_hour.hour and not self.asleep):
            self.asleep = True
            return True

        else:
            return False

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