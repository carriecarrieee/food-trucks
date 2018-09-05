import requests

from pprint import pprint

from datetime import datetime


def get_data():
    """Requests and accesses data from the San Francisco Data API, and 
       returns a python list of dictionaries."""

    url = "http://data.sfgov.org/resource/bbb8-hzi6.json"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json() # Converts json to python list of dictionaries
        return data
    else:
        print "{} {}".format("Request failed; response code:", response.status_code)


def get_curr_day():
    """Returns the current day of the week."""

    today = datetime.now().strftime("%w") # Weekday as a number
    return today


def get_curr_time():
    """Returns the current time as int."""

    curr = datetime.now().strftime("%X") # Local time in 24hr format
    time = int(curr[:2] + curr[3:5]) # Converts time into an int
    return time


def find_open_trucks(dataset):
    """Finds the open trucks at this moment."""

    trucks = [] # Empty list for food trucks that are open
    today = get_curr_day()
    curr_time = get_curr_time()

    for entry in dataset: # Loop through list of dictionaries
        if today == entry["dayorder"]:

            # Convert open and close times to int
            start = entry["start24"]
            opens = int(start[:2] + start[3:5])
            end = entry["end24"]
            closes = int(end[:2] + end[3:5])

            # Checks if current time falls between opening hours
            if opens <= curr_time <= closes:
                trucks.append([entry["applicant"], entry["location"]])

    return trucks

def print_trucks():
    """Sorts and formats the names and addresses of food trucks for display"""

    lst = find_open_trucks(get_data())
    count = 0

    # In case find_open_trucks returns an empty list, this indicates
    # that nothing is open at the current time.
    if not lst:
        return "Sorry! Nothing open right now."
    else:
        # Sort the list of trucks in alphabetical order
        trucks = sorted(lst)

        print "NAME: ADDRESS" # Header of data to be printed

        for truck in trucks:
            # If count reaches 10, this block prompts for user input
            if count == 10:
                raw_input("Press 'Enter' to continue.")
                count = 0 # Reset count for the next set of 10
            else:
                print ": ".join(truck)
                count += 1

print_trucks()