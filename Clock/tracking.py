import datetime
import time


class TrackingClock:

    # TODO : make format how I want to display
    TIME_FORMAT = "%I:%M:%S %p\n%A, %B %d, %Y"

    def __init__(self):
        pass

    def get_deadline(self):
        pass

    def edit_deadline(self):
        pass

    # This is where all clocks count down from
    def create_deadline(self, deadline):
        pass
    
    @staticmethod
    def get_time():
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime(TrackingClock.TIME_FORMAT)
        return formatted_datetime

    def progress():
        pass




if __name__ == "__main__":

    clock = TrackingClock()

    while True:
        print(clock.get_time())
        time.sleep(1)