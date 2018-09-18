import requests

from datetime import datetime, time, timedelta


def get_data():
    """Requests and accesses data from the San Francisco Data API, and 
       returns a python list of dictionaries."""

    url = "http://data.sfgov.org/resource/bbb8-hzi6.json"

    response = requests.get(url)
    
    assert(response.status_code == 200), "Response to data request failed."
    data = response.json() # Converts json to python list of dictionaries
    
    return data


def get_datetime():
    """Returns a datetime object of the current date and time."""

    now = datetime.now() # Local time as datetime object
    return now


def find_open_trucks(dataset):
    """Returns list of open trucks at current day and time."""

    trucks = [] # Empty list for food trucks that are open

    now = get_datetime()

    # Add'l feature: make sure trucks are still open 4 hours from now
    later = now + timedelta(hours=4)

    # Convert datetime object to a weekday as a number 0-6, 0 is Sunday
    today = now.strftime("%w")

    for entry in dataset: # Loop through list of dictionaries
        if today == entry["dayorder"]:

            # Convert open and close times to int to datetime.time object
            start_hr = int(entry["start24"][:2])
            start_min = int(entry["start24"][3:5])
            opens = time(start_hr, start_min)

            end_hr = int(entry["end24"][:2])
            end_min = int(entry["end24"][3:5])

            # Datetime hours are from 0-23
            if end_hr == 24:
                end_hr = 23
                end_min = 59
            closes = time(end_hr, end_min)

            # Checks if current time falls between opening hours
            if opens <= now.time() and later.time() <= closes:
                trucks.append([entry["applicant"], entry["location"]])

    return trucks


def print_trucks():
    """Sorts and formats the names and addresses of food trucks for display."""

    lst = find_open_trucks(get_data())
    count = 0

    # In case find_open_trucks returns an empty list, this indicates
    # that nothing is open at the current time.
    if not lst:
        print "\nSorry! Nothing open right now.\n"
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