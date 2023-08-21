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
        if birthday.strftime('%A') in result_dict.keys() and birthday.isocalendar()[1] == today.isocalendar()[1] + 1:
            key = birthday.strftime('%A')
            result_dict[key].append(person['name'])
        elif birthday.strftime('%A') in ('Saturday', 'Sunday') and birthday.isocalendar()[1] == today.isocalendar()[1]:
            result_dict['Monday'].append(person['name'])

    # print the result
    for day, names in result_dict.items():
        if names:
            print(f'{day}: {", ".join(names)}')

#implement the user list
users = [
    {"name": "Kate", "birthday": datetime.date(1984, 8, 29)},
    {"name": "Pavel", "birthday": datetime.date(1995, 8, 28)},
    {"name": "Bil", "birthday": datetime.date(1998, 8, 31)},
    {"name": "Anna", "birthday": datetime.date(1992, 8, 30)},
    {"name": "Helen", "birthday": datetime.date(1986, 9, 20)},
    {"name": "Tom", "birthday": datetime.date(1994, 8, 27)},
    {"name": "Robert", "birthday": datetime.date(1987, 8, 30)}
]

if __name__ == '__main__':
    # call the function to get the result
    get_birthdays_per_week(users)