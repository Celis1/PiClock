from datetime import datetime, timedelta, time
import calendar
import pickle
import os


class WorkoutTracker:
    workouts = [
                'biceps',
                'triceps',
                'chest',
                'back',
                'shoulders',
                'legs',
                'abs',
                'cardio',
                'yoga']
    
    combo_workouts = {
                'chest': 'triceps',
                'back': 'biceps',
                'cardio': 'abs',
                'legs': 'shoulders',
                'biceps': 'triceps'}

    
    def __init__(self) -> None:
        # tracking which workouts have been done
        self.workout_path = './DATA/TimeData/workout_data.pkl'
        self.workout_data = {
            'day': {'workout': [], 'time_session': []},
            'week': {'workout': [], 'time_session': []},
            'month': {'workout': [], 'time_session': []},
            'year': {'workout': [], 'time_session': []}
        }

        self._load_data()

        self.is_day_end = False

    def set_day(self, workouts, time_session):
        '''
        Function for setting the workout and time session for the day
        
        workout: array of workouts
        time_session: string of the time session in the format of 'hh:mm:ss'
        '''
        time_components = time_session.split(':')
        hours, minutes, seconds = int(time_components[0]), int(time_components[1]), int(time_components[2])
        timed_session = timedelta(hours=hours, minutes=minutes, seconds=seconds)

        temp_workouts = []
        for i in workouts:
            if i in self.combo_workouts and self.combo_workouts[i] in workouts:
                temp = i + '&' + self.combo_workouts[i]
                temp_workouts.append(temp)
            else:
                temp_workouts.append(i)

        self.workout_data['day']['workout'] = temp_workouts
        self.workout_data['day']['time_session'] = timed_session

    def day_end(self):
        '''
        Function for ending the day and appending the data to the other sections of time
        '''
        self.is_day_end = True

        # TODO : clean this up not modular
        self.workout_data['week']['workout'].append(self.workout_data['day']['workout'])
        self.workout_data['week']['time_session'].append(self.workout_data['day']['time_session'][0])

        self.workout_data['month']['workout'].append(self.workout_data['day']['workout'])
        self.workout_data['month']['time_session'].append(self.workout_data['day']['time_session'][0])

        self.workout_data['year']['workout'].append(self.workout_data['day']['workout'])
        self.workout_data['year']['time_session'].append(self.workout_data['day']['time_session'][0])

        # saving data
        self._save_data()

        # reset day
        self._reset('day')

    def _reset(self, period):
        if period in self.workout_data:
            self.workout_data[period]['workout'] = []
            self.workout_data[period]['time_session'] = []
        else:
            print(f"Invalid period: {period}")

    def _save_data(self):
        '''
        Function for saving the data
        '''
        with open(self.workout_path, 'wb') as f:
            pickle.dump(self.workout_data, f)

    def _load_data(self):
        '''
        Function for loading the data
        '''
        if os.path.exists(self.deadline_path):
            with open(self.workout_path, 'rb') as f:
                self.workout_data = pickle.load(f)
        else:
            print("Workout file does not exist")