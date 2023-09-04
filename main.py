import datetime

user = {}
births = []


def MaxAge():
    for x in user.values():
        return x


def new():
    now = datetime.datetime.today()
    yearNow = int(now.year)
    monthNow = int(now.month)
    dayNow = int(now.day)

    def year():
        y = int(input('Please type your birth year: '))
        if y > yearNow or y < 1800:
            print('Invalid date')
            return year()
        return y

    def month():
        m = int(input('Please type your birth month: '))
        if m < 1 or m > 12:
            print('Invalid date')
            return month()
        return m

    def day():
        d = int(input('Please type your birth day: '))
        if d < 1 or d > 31:
            print('Invalid date')
            return day()
        return d

    def age():
        age = yearNow - birth.year - ((monthNow, dayNow) < (birth.month, birth.day))
        return age

    name = input("Type your name: ")
    year_birth = year()
    month_birth = month()
    day_birth = day()
    birth = datetime.date(year_birth, month_birth, day_birth)
    births.append(birth)
    age_val = age()
    user.update({age_val: name})


while True:
    choice = input(
        '-------------------------------------------------------------\n1: if you want to add a new user\n2: show users\nType a number: ')

    if choice == "1":
        new()
    elif choice == "2":
        b = 0
        for usr_age, usr_name in user.items():
            birth_date = births[b].strftime("%A")
            print(f'{usr_name} is {usr_age} years old and was born on {birth_date}')
            b += 1

        if len(user) == 1 or len(user) == 0:
            print("There is no oldest or youngest person")
        else:
            min_age = min(user.keys())
            max_age = max(user.keys())
            print(f'The oldest one is {user[max_age]}')
            print(f'The youngest one is {user[min_age]}')
            print(f'Total People: {len(user)}')
    else:
        print("Invalid choice")





