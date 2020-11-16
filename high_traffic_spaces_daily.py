"""
    Title: High Traffic Spaces: VISITS PER DAY - Hackathon 2020

    Author: Hannah Mandell

    Date:   11 - 7 - 20

    Using student movement data, this code returns a list of the buildings on campus
    and their visits per day, presented in descending order. With this
    information, students can choose safer areas to travel to or through, maximizing
    individual and group safety.
"""


def building_visit_count(movement_fname):
    """
    Takes a csv of self-reported student location data for a specific day, and creates a list of all the buildings
    that were visited.
    :param movement_fname (str) name of a file containing self-reported student location data for a specific day.
    Contains: Student ID, Building Name, Entrance Time (00:00:00 in 24hr format), Exit Time (00:00:00 in 24hr format)
    :return: (dict) dictionary of all the buildings that were visited by students on that day and the amount of times
    they were visited
    """

    # Open movement_fname and read the first line to get the column titles out of the way
    movement_file = open(movement_fname, "r")
    movement_file.readline()

    building_dict = {}
    for line in movement_file:
        data_lst = line.split(",")
        building_name = data_lst[1]
        if building_name not in building_dict:
            building_dict[building_name] = 1
        else:
            building_dict[building_name] += 1

    return building_dict


def building_visit_sort(building_dict):
    """
    Takes a csv of self-reported student location data for a specific day, and creates a list of all the buildings
    that were visited.
    :param building_dict (dict) dictionary of all the buildings that were visited by students on that day and
    the amount of times they were visited
    :return: (lst) descending-order sorted list of buildings visited by students and the amount of times
    they were visited. Each item looks like - #: Building
    """
    buildings_lst = []
    for building in building_dict:
        buildings_lst.append((str(building_dict[building]) + ": " + str(building)))

    buildings_lst.sort()
    buildings_lst.reverse()

    return buildings_lst


def main():
    print(building_visit_sort(building_visit_count("movement_data.csv")))


if __name__ == '__main__':
    main()