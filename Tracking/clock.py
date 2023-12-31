from datetime import datetime, timedelta, time
import calendar

from time import sleep
import pickle
import os
from typing import Any

# TODO : need to split this class into 2 classes
class ClockTracker:

    # TODO : make format how I want to display
    TIME_FORMAT = "%I:%M:%S %p\n%A, %B %d, %Y"

    def __init__(self):
        self.deadline_path = './DATA/TimeData/deadline.pkl'
        self.startup_time = datetime.now()

        self.day_start = 7
        # TODO : implement this
        self.day_end = 23

        self.current_times = {
            'day':self.startup_time.day,
            'week':self.startup_time.isocalendar()[1],
            'month':self.startup_time.month,
            'year':self.startup_time.year
        }

    def __call__(self):
        '''
        Function for updating the time
        '''
        curr_formatted_time = self.get_time()
        day_progress, day_left = self.get_day_progress()
        month_progress, month_left = self.month_progress()
        year_progress, year_left = self.year_progress()
        deadline_progress, deadline_left = self.deadline_progress()


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

    def update_times(self):
        '''
        Function for updating the current times
        '''
        today = datetime.now()

        self.current_times = {
            'day':today.day,
            'week':today.isocalendar()[1],
            'month':today.month,
            'year':today.year
        }


    def get_deadline(self):
        '''
        Function for getting the final deadline of the that the clock runs down to
        '''
        # open the directory to the deadline file

        # check if the file exists
        if os.path.exists(self.deadline_path):
            with open(self.deadline_path, "rb") as file:
                deadline = pickle.load(file)
                return deadline[0], deadline[1]
        else:
            print("Deadline file does not exist")
            return None

    def set_deadline(self, deadline):
        '''
        Function for setting the final deadline of the that the clock runs down to

        deadline: string of the deadline in the format of 'mm/dd/yyyy'
        '''
        deadline += ' 09:00:00'
        deadline_date = datetime.strptime(deadline, "%m/%d/%Y %H:%M:%S")
        deadline_created = datetime.now()
        # TODO : not the best way to store this as a tuple
        parsed_date = (deadline_created, deadline_date)

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
        '''
        Function for getting the current time and displaying it properly
        '''
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime(ClockTracker.TIME_FORMAT)
        return formatted_datetime

    def normalize(self, start_time, current_time, end_time):
        '''
        Function for normalizing the time to a value between 0 and 1
        '''

        # Calculate the total time range as a timedelta
        total_time_range = end_time - start_time

        # Calculate the time elapsed from start_time to current_time as a timedelta
        time_elapsed = current_time - start_time
        
        # Calculate the normalized value as a float between 0 and 1
        normalized_value = time_elapsed.total_seconds() / total_time_range.total_seconds()
        
        # Ensure the value is within the range [0, 1]
        normalized_value = max(0.0, min(1.0, normalized_value))
        
        return normalized_value
        

    def deadline_progress(self):
        '''
        Function for getting the progress of the current date to the deadline
        '''
        start_date, end_date = self.get_deadline()
        now = datetime.now()

        # Calculate the normalized value
        norm_value = self.normalize(start_date, now, end_date)

        # calculate the days left
        days_left = (end_date - now).days

        return norm_value, days_left


    def year_progress(self):
        '''
        Function for getting the progress of the current year starting from the 1st of
        January to the 31st of December
        '''
        # Get the current date
        now = datetime.now()

        # Calculate the total number of days in the current year
        number_of_days = 365 if now.year % 4 else 366

        # get the current day
        current_day = now.timetuple().tm_yday

        # create a datetime object for the first day of the year
        first_day = now.replace(month=1, day=1, hour=0, minute=0, second=0)
        last_day = now.replace(month=12, day=31, hour=23, minute=59, second=59)

        # Calculate the normalized value
        days_left = number_of_days - current_day
        norm_value = self.normalize(first_day, now, last_day)

        return norm_value, days_left

    def month_progress(self):
        '''
        Function for getting the progress of the current month starting from the 1st of
        the current month to the last day
        '''
        # Get the current date
        now = datetime.now()

        # Calculate the total number of days in the current month
        number_of_days = calendar.monthrange(now.year, now.month)[1]

        # get the current day
        current_day = now.day

        # create a datetime object for the first day of the month
        first_day = now.replace(day=1, hour=0, minute=0, second=0)
        last_day = now.replace(day=number_of_days, hour=23, minute=59, second=59)

        # Calculate the normalized value
        days_left = number_of_days - current_day
        norm_value = self.normalize(first_day, now, last_day)

        return norm_value, days_left
    
    # TODO : add week progress

    @staticmethod
    def in_between(now, start, end):
        if start <= end:
            return start <= now < end
        else: # over midnight
            return start <= now or now < end

    def get_day_progress(self):            
        # Get the current date and time
        now = datetime.now()
        # TODO : this is just for debugging
        # now = now.replace(hour=3, minute=0, second=0)

        # Define the time ranges for 12 PM and 9 AM
        twelve_pm = datetime.combine(now, time(0, 0, 0))
        nine_am = datetime.combine(now, time(self.day_start, 0, 0))

        if self.in_between(now, twelve_pm, nine_am):
        # Check if the current time is between 12 PM and 9 AM
            # Calculate yesterday's date by subtracting one day from the current date
            yesterday = now.replace(hour=self.day_start, minute=0, second=0) - timedelta(days=1)
            tomorrow = now.replace(hour=self.day_start, minute=0, second=0)
        else:
            # Otherwise, use today's date
            yesterday = now.replace(hour=self.day_start, minute=0, second=0)
            tomorrow = now.replace(hour=self.day_start, minute=0, second=0) + timedelta(days=1)

        
        # Calculate the time difference in hours
        if now.hour <= self.day_start:
            time_difference = self.day_start - now.hour
        else:
            time_difference = 24 - now.hour + self.day_start
        
        #normalizing the time for progress bar
        norm_time = self.normalize(yesterday, now, tomorrow)

        return norm_time, time_difference



if __name__ == "__main__":

    clock = ClockTracker()
    date_string = "7/23/2024"
    clock.create_deadline(date_string)

    print('deadline')
    print(clock.get_deadline())


    while True:
        print(clock.get_time())
        print('day: ',clock.get_day_progress())
        print('month: ',clock.month_progress())
        print('year',clock.year_progress())
        print('deadline',clock.deadline_progress())
        sleep(1)