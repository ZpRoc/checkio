# ---------------------------------------------------------------- #

# Date and Time Converter
#   You have to convert date and time into more readable format
#   (Date, time, string)

# ---------------------------------------------------------------- #

# Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
# Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
# Your task is simple - convert the input date and time from computer format into a "human" format.

# Input: Date and time as a string
# Output: The same date and time, but in a more readable format
# Precondition:
#   0 < date <= 31
#   0 < month <= 12
#   0 < year <= 3000
#   0 < hours < 24
#   0 < minutes < 60


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

import datetime as dt


MONTH = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
         'August', 'September', 'October', 'November', 'December']


def date_time(time: str) -> str:
    d = dt.datetime.strptime(time, '%d.%m.%Y %H:%M')
    h = "hour" if d.hour == 1 else "hours"
    m = "minute" if d.minute == 1 else "minutes"
    return d.strftime(f'{d.day} %B %Y year {d.hour} {h} {d.minute} {m}')


def date_time_1(time: str) -> str:
    #replace this for solution
    info = [str(int(x)) for x in time.replace(' ', '.').replace(':', '.').split('.')]
    strH = 'hour' if info[3] == '1' else 'hours'
    strM = 'minute' if info[4] == '1' else 'minutes'
    return ' '.join([info[0], MONTH[int(info[1])-1], info[2], 'year', 
                     info[3], strH, info[4], strM])


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")

