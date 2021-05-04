# import datetime as dt

# date1 = dt.datetime.today()

# print(date1)

import  time, datetime

today_date = datetime.date.today()
future_date = datetime.date(2022,1,1)
diff = future_date - today_date


print(diff.days)

import datetime, time


ny_22 = datetime.date(2022, 1, 1) - datetime.date.today()
print(ny_22)

from datetime import datetime

val1 = datetime.now()
val2 = datetime(2022, 1, 1, 00, 00, 00)

print(val2 - val1)

print(f'The 1st of January in {val2 - val1} hours')

def mins_alive(year, month, day):
    birth_date = datetime(year, month, day)
    now = datetime.now()
    time_since = now - birth_date
    minutes = int(time_since.total_seconds()/60)

    print(f'you have been alive for {minutes} minutes')


mins_alive(1990, 4, 22)


string = "19 Nov 2015  18:45:00.000"
date = datetime.strptime(string, "%d %b %Y  %H:%M:%S.%f")
print(date)

def time_to_holiday(year, month, day, holiday='Chanukah'):
    now_date = datetime.now()
    holiday_date = datetime(year, month, day)
    time_left = holiday_date - now_date
    print(f'The next holiday is {holiday} and is in {time_left} hours')
    

time_to_holiday(2021, 9, 15)

def age_on_planet(planet, orbital_period, seconds):
    earth_years = seconds/(31557600*orbital_period)
    print(f'You are {earth_years} Earth-years old on {planet}')
    

age_on_planet('Earth', 1, 1000000000)


from faker import Faker

faker = Faker()

print(f'name: {faker.name()}')


def populate_users():
    users = []
    profile = {'name': faker.name(), 'address': faker.address(), 'langage_code': faker.langage_code()}
    users.append(profile)
    print(users)

populate_users()






# try:
#     import timedelta
#     print('module time is installed')
# except ModuleNotFoundError:
#     print('module time is not installed')

