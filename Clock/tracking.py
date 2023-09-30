import datetime
import time
import pickle
import os


class TrackingClock:

    # TODO : make format how I want to display
    TIME_FORMAT = "%I:%M:%S %p\n%A, %B %d, %Y"

    def __init__(self):
        self.deadline_path = './DATA/TimeData/deadline.pkl'


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
        parsed_date = datetime.datetime.strptime(deadline, "%m/%d/%Y %H:%M:%S")

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
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime(TrackingClock.TIME_FORMAT)
        return formatted_datetime

    def progress():
        pass




if __name__ == "__main__":

    clock = TrackingClock()
    date_string = "7/23/2025"
    clock.create_deadline(date_string)

    print(clock.get_deadline())


    while True:
        print(clock.get_time())
        time.sleep(1)