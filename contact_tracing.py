"""
    Title: Contact Tracing - Hackathon 2020

    Author: Hannah Mandell

    Date:   11 - 7 - 20

    Using student movement data and COVID-testing data, this code returns a list of student IDs who have
    come in contact with one or more COVID-positive students on a specific day, warranting immediate testing,
    quarantine, and safety measures on their behalf.
"""


def positive_times(positive_fname, movement_fname, new_fname):
    """
    Takes a csv of student IDs who have tested positive for COVID-19 and an csv of self-reported
    student location data for a specific day, and creates a file of the time periods that the COVID-positive
    students were in buildings.
    :param positive_fname: (str) name of a file containing student IDs of positive COVID-19 tests
    :param movement_fname (str) name of a file containing self-reported student location data for a specific day.
    Contains: Student ID, Building Name, Entrance Time (00:00:00 in 24hr format), Exit Time (00:00:00 in 24hr format)
    :param new_fname (str) name of the new file we write. It contains building entrance and exit times for
    the COVID-positive students of that day.
    :return: None
    """
    # Open the positive_fname and movement_fname
    # read the first lines to get the column titles out of the way
    positive_file = open(positive_fname, "r")
    positive_file.readline()
    
    movement_file = open(movement_fname, "r")
    movement_file.readline()

    # Open new_fname and write
    positive_movement_file = open(new_fname, "w")

    # Create a list of all the COVID-positive student IDs
    positive_id_list = []
    for line in positive_file:
        positive_id_list.append(line.rstrip("\n"))

    # Grab the location & time data for all the COVID-positive students, write as new csv file
    for line in movement_file:
        data_lst = line.split(",")
        student_id = data_lst[0]
        if student_id in positive_id_list:
            building_name = data_lst[1]
            entrance_time = data_lst[2]
            exit_time = data_lst[3]
            positive_movement_file.write(building_name + ", " + entrance_time + ", " + exit_time)


def contact_data(positive_movement_fname, movement_fname):
    """
    Creates a csv of the location & time data for students that crossed paths with COVID-positive students on that day.
    :param positive_movement_fname: (str) name of a file containing building name, entrance and exit times for
    the COVID-positive students of that day
    :param movement_fname: (str)  name of a file containing self-reported student location data for a specific day.
    Contains: Student ID, Building Name, Entrance Time (00:00:00 in 24hr format), Exit Time (00:00:00 in 24hr format)
    :return: (list) IDs of students that interacted with COVID-positive students on that day
    """

    # Open positive_movement_fname and movement_fname
    positive_movement_file = open(positive_movement_fname, "r")

    # Read the first lines to get the column titles out of the way
    movement_file = open(movement_fname, "r")
    movement_file.readline()

    contact_id_lst = []
    # look at the location & time for each COVID-positive student
    for pos_line in positive_movement_file:
        pos_data_lst = pos_line.split(",")
        pos_building = pos_data_lst[0]
        # change the 24 hour time format into integers for easier comparison
        pos_entrance_time = int(pos_data_lst[1].replace(':', ''))
        pos_exit_time = int(pos_data_lst[2].replace(':', ''))

        # look at the location and time for each regular student
        for line in movement_file:
            data_lst = line.split(",")
            contact_id = data_lst[0]
            building = data_lst[1]
            # change the 24 hour time format into integers for easier comparison
            entrance_time = int(data_lst[2].replace(':', ''))
            exit_time = int(data_lst[3].replace(':', ''))

            # if the two students were in the same building at the same time
            if pos_building == building:
                if entrance_time in range(pos_entrance_time, pos_exit_time):
                    # add the regular student's ID to the list of potentially-infected contacts
                    contact_id_lst.append(contact_id)
                elif exit_time in range(pos_entrance_time, pos_exit_time):
                    contact_id_lst.append(contact_id)
                elif pos_entrance_time in range(entrance_time, exit_time):
                    contact_id_lst.append(contact_id)
                elif pos_exit_time in range (entrance_time, exit_time):
                    contact_id_lst.append(contact_id)

    return contact_id_lst


def main():
    # write the csv of times & location of COVID-positive students
    positive_times("positive_data.csv", "movement_data.csv", "positive_times.csv")

    # print a list of the students (their IDs) who interacted with COVID-positive students
    print(contact_data("positive_times.csv", "movement_data.csv"))


if __name__ == '__main__':
    main()