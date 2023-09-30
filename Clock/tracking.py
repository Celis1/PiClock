from datetime import datetime, timedelta, time
from time import sleep
import pickle
import os


class TrackingClock:

    # TODO : make format how I want to display
    TIME_FORMAT = "%I:%M:%S %p\n%A, %B %d, %Y"

    def __init__(self):
        self.deadline_path = './DATA/TimeData/deadline.pkl'
        self.startup_time = datetime.now()


    def get_deadline(self):
        '''
        Function for getting the final deadline of the that the clock runs down to
        '''
        # open the directory to the deadline file

        # check if the file exists
        if os.path.exists(self.deadline_path):
            print('found deadline')
            with open(self.deadline_path, "rb") as file:
                deadline = pickle.load(file)
                return deadline
        else:
            print("Deadline file does not exist")
            return None

    def set_deadline(self, deadline):
        '''
        Function for setting the final deadline of the that the clock runs down to

        deadline: string of the deadline in the format of 'mm/dd/yyyy'
        '''
        deadline += ' 09:00:00'
        parsed_date = datetime.strptime(deadline, "%m/%d/%Y %H:%M:%S")

        # TODO : might need to make this modular
        with open("./DATA/TimeData/deadline.pkl", "wb") as file:
            pickle.dump(parsed_date, file)

        print(f"Date '{deadline}' converted and saved as 'deadline.pkl'")


    def edit_deadline(self, deadline):
        '''
        Function for editing the deadline of the clock

        deadline: string of the deadline in the format of 'mm/dd/yyyy'
        '''
        if not os.path.exists(self.deadline_path):
            print("Deadline file does not exist us create_deadline() to create it")
            return None
        
        self.set_deadline(deadline)
        

    # This is where all clocks count down from
    def create_deadline(self, deadline):
        '''
        Function for instantiating the deadline of the clock

        deadline: string of the deadline in the format of 'mm/dd/yyyy'
        '''
        if os.path.exists(self.deadline_path):
            print("Deadline file already exists use edit_deadline() to change it")
            return None
        
        self.set_deadline(deadline)

    @staticmethod
    def get_time():
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime(TrackingClock.TIME_FORMAT)
        return formatted_datetime

    def normalize(self, start_time, current_time, end_time):

        # Calculate the total time range as a timedelta
        total_time_range = end_time - start_time

        # Calculate the time elapsed from start_time to current_time as a timedelta
        time_elapsed = current_time - start_time
        
        # Calculate the normalized value as a float between 0 and 1
        normalized_value = time_elapsed.total_seconds() / total_time_range.total_seconds()
        
        # Ensure the value is within the range [0, 1]
        normalized_value = max(0.0, min(1.0, normalized_value))
        
        return normalized_value
        
    def initialize_progress(self):
        pass

    def deadline_progress(self):
        pass

    def year_progress(self):
        pass

    def month_progress(self):
        pass

    def get_day_progress(self):
        # Get the current date and time
        now = datetime.now()

        # Define the time ranges for 12 PM and 9 AM
        twelve_pm = datetime.combine(now, time(12, 0, 0))
        nine_am = datetime.combine(now, time(9, 0, 0))

        # Check if the current time is between 12 PM and 9 AM
        if twelve_pm <= now < nine_am:
            # Calculate yesterday's date by subtracting one day from the current date
            yesterday = now - timedelta(days=1)
            tomorrow = now
        else:
            # Otherwise, use today's date
            yesterday = now
            tomorrow = nine_am + timedelta(days=1)

        
        # Create datetime objects for 9 AM of yesterday and today
        yesterday_9am = datetime(yesterday.year, yesterday.month, yesterday.day, 9, 0, 0)
        
        # Calculate the time difference in hours
        time_difference = now.hour - yesterday_9am.hour
        
        #normalizing the time for progress bar
        norm_time = self.normalize(yesterday_9am, now, tomorrow)

        return norm_time, time_difference



if __name__ == "__main__":

    clock = TrackingClock()
    date_string = "7/23/2025"
    clock.create_deadline(date_string)

    print(clock.get_deadline())


    while True:
        print(clock.get_time())
        print(clock.get_day_progress())
        sleep(1)