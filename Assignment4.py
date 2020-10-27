"""
    Assignment Four: Creating a Sensor List and Filter List
    Submitted by Christopher Amurao
"""


def print_header():
    print("STEM Center Temperature Project")
    print("Christopher Amurao")


def print_menu():
    print('Main Menu')
    print('---------')
    print('1 - Process a new data file')
    print('2 - Choose units')
    print('3 - Edit room filter')
    print('4 - Show summary statistics')
    print('5 - Show temperature by date and time')
    print('6 - Show histogram of temperatures')
    print('7 - Quit')
    print('')


def new_file(dataset):
    """
    Open a new file
    """
    print('New File function called')


def choose_units():
    """
    Called when user chooses units (2)
    """
    print('Choose units function called')


def change_filter(sensor_list, active_sensors):
    """
    Called when use changes the filters (3)
    :param sensor_list:
    :param active_sensors:
    :return:
    """
    print('Change filter function called')


def print_summary_statistics(dataset, active_sensors):
    """
    Called when the user presses (4)
    :param dataset:
    :param active_sensors:
    :return:
    """
    print('Print summary statistics called')


def print_temp_by_day_time(dataset, active_sensors):
    """
    called when user presses (5)
    :param dataset:
    :param active_sensors:
    :return:
    """
    print('Print temp by day time called')


def print_histogram(dataset, active_sensors):
    """
    called when user presses (6)
    :param dataset:
    :param active_sensors:
    :return:
    """
    print('Print histogram called')


def convert_units(celsius_value, units):
    if units == 0:
        return celsius_value

    # fahrenheit
    if units == 1:
        return celsius_value * 9.00 / 5.00 + 32

    # kelvin
    if units == 2:
        return celsius_value + 273.15


def main():
    sensors = {
        "4213": ('STEM Center', 0),
        "4201": ('Foundations Lab', 1),
        "4204": ('CS Lab', 2),
        "4218": ('Workshop Room', 3),
        "4205": ('Tiled Room', 4),
        "Out": ('Outside', 5),
    }

    sensor_list = [(key, val[0], val[1]) for key, val in sensors.items()]

    filter_list = [val[1] for key, val in sensors.items()]

    print("Testing sensors:")
    if sensors["4213"][0] == "STEM Center" and sensors["Out"][1] == 5:
        print("Pass")
    else:
        print("Fail")

    print("Testing sensor_list length:")
    if len(sensor_list) == 6:
        print("Pass")
        print("Testing sensor_list content:")
        for item in sensor_list:
            if item[1] != sensors[item[0]][0]:
                print("Fail")
                break
        else:
            print("Pass")

    print("Testing filter_list length:")
    if len(filter_list) == 6:
        print("Pass")
    else:
        print("Fail")

    print("Testing filter_list content:")
    if sum(filter_list) == 15:
        print("Pass")
    else:
        print("Fail")

    print_header()
    on = True
    while on:
        print_menu()
        try:
            choice = int(input('What is your choice? '))
            if choice == 1:
                new_file(None)
            elif choice == 2:
                choose_units()
            elif choice == 3:
                change_filter(None, None)
            elif choice == 4:
                print_summary_statistics(None, None)
            elif choice == 5:
                print_temp_by_day_time(None, None)
            elif choice == 6:
                print_histogram(None, None)
            elif choice == 7:
                on = False
            else:
                raise ValueError
        except ValueError:
            print('That is not a valid choice. Please try again.\n')
        finally:
            print('')


if __name__ == "__main__":
    main()

"""
/Users/camurao/PycharmProjects/CS3A/venv/bin/python /Users/camurao/PycharmProjects/CS3A/Assignment4.py
Testing sensors:
Pass
Testing sensor_list length:
Pass
Testing sensor_list content:
Pass
Testing filter_list length:
Pass
Testing filter_list content:
Pass
STEM Center Temperature Project
Christopher Amurao
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 7


Process finished with exit code 0

"""
