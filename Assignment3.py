"""
    Assignment Two: Temperature Conversions
    Submitted by Christopher Amurao

    Assignment 2: Add code to prompt the user for a temperature in Celsius and
    then converts that temperature to a specified different temperature
    unit.

    Assignment One: Opening Lines - Christopher Amurao
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
/Users/camurao/PycharmProjects/Assignment2/venv/bin/python /Users/camurao/PycharmProjects/Assignment2/Assingment2.py
STEM Center Temperature Project
Christopher Amurao
Please enter a temperature in degrees (Celsius): 0
That's 32.00 Fahrenheit and 
 273.15 Kelvin
Please enter a temperature in degrees (Celsius): 100
That's 212.00 Fahrenheit and 
 373.15 Kelvin

Process finished with exit code 0
"""
