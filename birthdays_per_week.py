import datetime

def get_birthdays_per_week(users):
    """
    This function returns (prints) actual birthdays of persons in the users list
    for the next week divided by days of the week
    :param users: user list -> List
    :return: None
    """
    today = datetime.datetime.now().date()
    result_dict = {"Monday": [],
                   "Tuesday": [],
                   "Wednesday": [],
                   "Thursday": [],
                   "Friday": []}

    for person in users:
        birthday = person["birthday"]
        birthday = birthday.replace(year=today.year)
        #check the day of the week for birthday and if the birthday is next week
        if birthday.weekday() == 0 and (birthday - today).days in range(1, 8):
            result_dict["Monday"].append(person["name"])
        elif birthday.weekday() == 1 and (birthday - today).days in range(2, 9):
            result_dict["Tuesday"].append(person["name"])
        elif birthday.weekday() == 2 and (birthday - today).days in range(3, 10):
            result_dict["Wednesday"].append(person["name"])
        elif birthday.weekday() == 3 and (birthday - today).days in range(4, 11):
            result_dict["Thursday"].append(person["name"])
        elif birthday.weekday() == 4 and (birthday - today).days in range(5, 12):
            result_dict["Friday"].append(person["name"])
        elif birthday.weekday() == 5 and (birthday - today).days in range(-1, 6):
            result_dict["Monday"].append(person["name"])
        elif birthday.weekday() == 6 and (birthday - today).days in range(0, 7):
            result_dict["Monday"].append(person["name"])

    # print the result
    for day, names in result_dict.items():
        if names:
            print(f'{day}: {", ".join(names)}')

#implement the user list
users = [
    {"name": "Kate", "birthday": datetime.date(1984, 8, 19)},
    {"name": "Pavel", "birthday": datetime.date(1995, 8, 21)},
    {"name": "Bil", "birthday": datetime.date(1998, 8, 22)},
    {"name": "Anna", "birthday": datetime.date(1992, 8, 24)},
    {"name": "Helen", "birthday": datetime.date(1986, 8, 20)},
    {"name": "Tom", "birthday": datetime.date(1994, 8, 25)},
    {"name": "Robert", "birthday": datetime.date(1987, 8, 30)}
]

if __name__ == '__main__':
    # call the function to get the result
    get_birthdays_per_week(users)