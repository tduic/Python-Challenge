import datetime

# calendar is in the 1000s and ends in 6
# starting point is 1006 - not a leap year
# new start is 1016 - is a leap year
# leap years ending in 6 will be every 20 years from then
# need Jan 26 to be a Monday
# need second youngest person from this range
# important day is jan 27
def challenge15():
    years = [year for year in range(1016,1996,20) if datetime.date(year, 1, 26).isoweekday() == 1]
    return years[-2]

if __name__ == '__main__':
    print(challenge15())
