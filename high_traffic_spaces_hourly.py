"""
    Title: High Traffic Spaces: VISITS PER HOUR- Hackathon 2020

    Author: Hannah Mandell

    Date:   11 - 7 - 20

    Using student movement data, this code returns a list of the buildings on campus
    and their visits each hour. With this information, students can choose safer areas
    to travel to or through, maximizing individual and group safety.
"""


def hours_and_buildings(movement_fname):
    """
    Takes a csv of self-reported student location data for a specific day, and creates a list of all the buildings
    that were visited.

    :param movement_fname (str) name of a file containing self-reported student location data for a specific day.
    Contains: Student ID, Building Name, Entrance Time (00:00:00 in 24hr format), Exit Time (00:00:00 in 24hr format)
    :return: (list) a sorted list of lists of [hour, building] for each data entry
    """

    # Open movement_fname and read the first line to get the column titles out of the way
    movement_file = open(movement_fname, "r")
    movement_file.readline()

    # make a list of lists of [hour, building] for each data entry
    hourly_count_lst = []
    for line in movement_file:
        data_lst = line.split(",")
        building_name = data_lst[1]

        # get a value between 0 and 24 for the hour
        entrance_hour = int((int(data_lst[2].replace(':', '')) / 10000))
        exit_hour = int((int(data_lst[3].replace(':', '')) / 10000))

        # for each different hour the person was in the building, add an entry for that building in that hour
        if entrance_hour == exit_hour or exit_hour == 88:
            hourly_count_lst.append([entrance_hour, building_name])
        elif (exit_hour - entrance_hour) > 1:
            for num in range(entrance_hour, exit_hour + 1):
                hourly_count_lst.append([num, building_name])
        else:
            hourly_count_lst.append([entrance_hour, building_name])
            hourly_count_lst.append([exit_hour, building_name])

    # sort the list ascending
    hourly_count_lst.sort()

    return hourly_count_lst


def hourly_building_visit_count(hourly_lst):
    """
    Creates a dictionary of each building's traffic each hour

    :param hourly_lst (lst) a sorted ascending list of lists of [hour, building] for each data entry
    :return: (dict) a dictionary with key = hour of the day in 24 hr format, and value = tuples of
    (Building, Hourly Count) for each building during that hour
    """

    # create a dictionary of 'hour: building' : count
    hourly_count_dict = {}
    for lst in hourly_lst:
        hour = lst[0]
        building = lst[1]
        if (str(hour) + ": " + building) not in hourly_count_dict:
            hourly_count_dict[str(hour) + ": " + building] = 1
        else:
            hourly_count_dict[str(hour) + ": " + building] += 1

    # create a dictionary of 'hour: tuples of (building, count) for each building that hour'
    hourly_building_count_dict = {}
    for hour_and_building in hourly_count_dict:
        hour = int(hour_and_building.split(': ')[0])
        building = hour_and_building.split(': ')[1]
        count = hourly_count_dict[hour_and_building]
        if hour not in hourly_building_count_dict:
            hourly_building_count_dict[hour] = building, count
        else:
            # add the (building, count) info to the dictionary entry for that hour
            old = hourly_building_count_dict[hour]
            updated = old, (building, count)
            hourly_building_count_dict[hour] = updated

    return hourly_building_count_dict


def main():
    print(hourly_building_visit_count(hours_and_buildings("movement_data.csv")))


if __name__ == '__main__':
    main()