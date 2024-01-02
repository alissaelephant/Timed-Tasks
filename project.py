import csv
from csv import writer
import time
import sys



def main():
    #variables to be used
    pathway = '/project/project.csv'
    #1. get task
    task_input = input("Type the task you'd like to time today: ").lower().strip()

    #2. get task start time
    start_input = input("Please press Enter/Return to start the timer.")
    start_time = get_start_time(start_input)

    #3. get task end time IF start_time is not null/error
    end_input = input("Press Enter/Return to stop the timer")
    end_time = get_end_time(end_input)

    #4. get task duration
    duration = get_duration(start_time, end_time)

    #5. get current csv data as a dictionary
    current_task_data = get_csv_data(pathway)

    #6 loop through data and update task and timing data
    get_average = update_csv(task_input, duration, current_task_data, pathway)

    #7 provide average time to user
    convert_sec_to_min = int(get_average) / 60
    round_average = round(convert_sec_to_min, 2)
    print(f"The current average time to complete the task: '{task_input}' is {round_average} minutes.")


def get_start_time(start_input):

    if start_input == "":
        return time.time()
    elif start_input != "":
        while True:
            try:
                retry_input = input("Command not recognized, please press the Enter or Return Key")
                if retry_input == "":
                    return time.time()
            except KeyboardInterrupt:
                sys.exit("Cannot start clock, please try again later")
            else:
                continue


def get_end_time(end_input):

    if end_input == "":
        return time.time()

    while True: #use while loop reprompt user if they hit the wrong key
        try:
            end_retry = input("Command not recognized, please press the Enter or Return Key") #let user know they hit the wrong key
            if end_retry == "": #if they hit it the correct one -
                return time.time() #then they exit out of the loop and end_time is returned to main function
        except KeyboardInterrupt:
            sys.exit("Error")


def get_duration(start_time, end_time): #total amount of time to complete the task
    duration = end_time - start_time
    return duration

def get_csv_data(pathway): #put current csv data into a dictionary and return it
    with open(pathway, 'r', newline='') as current_csvfile: #open file
        csv_reader = csv.DictReader(current_csvfile) #create reader object
        data = [row for row in csv_reader] #for each row associate items with keys for new dictionary
    return data

def update_csv(task_input, duration, data, pathway): #evaluate if task exists in data, if it does update calculations and if not create new row

    field_names = ['task', 'number_of_times_timed', 'total_time', 'average_time'] #define the order of columns that will be used for writeheader() / writerows() methods

    task_found = False #flag variable to help properly loop through dictionary


    for row in data: #loops through dictionary
        if row['task'].lower() == task_input.lower(): #if user inputted task exists in file
            task_found = True
            row['number_of_times_timed'] = int(row['number_of_times_timed']) + 1 #add number of times user has timed themself
            row['total_time'] = float(row['total_time']) + duration #add to total number of time spent on given task
            row['average_time'] = row['total_time'] / row['number_of_times_timed'] #calculates new average
            new_average = row['average_time']
            break


    if not task_found: #if user inputted task doesn't exist it will create a new row
        new_entry = {'task': task_input.lower(), 'number_of_times_timed': 1, 'total_time': duration, 'average_time': duration}
        data.append(new_entry)
        new_average = duration


    with open(pathway, 'w', newline='') as csv_file: #open csv file in write mode
        csv_writer = csv.DictWriter(csv_file, fieldnames=field_names) #create writer object
        csv_writer.writeheader() #writes headers and specificies order to map data to
        csv_writer.writerows(data) #outputs data changes

    #return task_input average
    return new_average


if __name__ == "__main__":
    main()