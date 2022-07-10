from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(('%Y-%m-%d %H:%M:%S'))


# ?: Data to serve with our API
PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp()
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp()
    }
}

# TODO: Create a handler for our read (GET) people


def read():
    '''
    "Create the list of people from our data."

    The first line of the function is a docstring. It's a string that describes what the function does.
    It's a good idea to include a docstring in every function you write
    :return: A list of dictionaries
    '''
    # ?: Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]
