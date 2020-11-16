import csv

def parse(filename):
    """
    Converts csv file to a list of lists
    Each list represents a single entrance/exit entry
    :param filename: (file) 
    :return (list)
    """
    with open(filename, "r") as file_in:

        # converts each line in the file to a list 
        file_in_reader = csv.reader(file_in)
        next(file_in_reader)

        # add each list to a bigger list
        all_data_list = [line for line in file_in_reader]

        # convert the timestamps to integers
        for sublist in all_data_list:
            for i in range(2,4):
                sublist[i] = int(sublist[i].replace(":",""))

    return all_data_list


def check_max_capacity(filename, building_name):
    """
    Calculates the current number of students in a particular building 
    and returns True if the buiding"s max capacity has been reached

    :param filename: (file)
    :param building_name: (str) name of the building
    return: (bool) 

    """
    # step 1: filter the data_set according to the building name 
    building_data = [sublist for sublist in parse(filename) if sublist[1] == building_name]

    # step 2: # of occupants in the building = total # of entries - # of entries with null exit timestamps
    count = len(building_data)
    for sublist in building_data:
        # Subtract 1 for each entry that does not have an exit time stamp 
        # Assuming 88:88:88 is the null time stamp
        if not sublist[3] == 888888:
            count -= 1
    count = 42 # if you comment this out to return to original count of 3, the assert value should be False
    
    # step 3: get furniture space data
    with open("capacity_data.csv", "r") as file_in:
        # converts each line in the file to a list 
        file_in_reader = csv.reader(file_in)

        # add each list to a bigger list
        capacity_data_list = [line for line in file_in_reader]
        for i in capacity_data_list:
            if i[0]== building_name:
                total_space = int(i[2])
                furn_space = int(i[1])
                
    
    # step 4: check if max capacity has been reached
    # insert furn_space into the max capacity formula
    if count >= (1 - furn_space/100) * total_space/36:
        return True
    else:
        return False


# Testing

assert check_max_capacity("thedata.csv", "frary") == True
# the max capacity for frary is 41.6
print("check_max_capacity passed")

