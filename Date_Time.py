import datetime
from datetime import datetime, timedelta, date, time


#1

def date_after_days(days):

	dt = datetime.now() + timedelta(days)
	print("Current date is ", datetime.now().strftime("%m-%d-%y"))
	print("The date after {:d} days is ".format(days), dt.strftime("%m-%d-%y"))


date_after_days(10)


#2
def date_before_days(days):

	dt = datetime.now() - timedelta(days=days)
	print("Current date is ", datetime.now().strftime("%m-%d-%y"))
	print("The date {:d} days ago is ".format(days), dt.strftime("%m-%d-%y"))


date_before_days(10)


#3
def time_after_hours(hours):
	dt = datetime.now() + timedelta(hours=hours)
	print("Current time is ", datetime.now().strftime("%I:%M %p"))
	print("The time after {:d} hours is {}".format(hours, dt.strftime("%I:%M %p")))


time_after_hours(5)


#4
def time_before_hours(hours):
	dt = datetime.now() - timedelta(hours=hours)
	print("Current time is ", datetime.now().strftime("%I:%M %p"))
	print("The time {:d} hours ago is {}".format(hours, dt.strftime("%I:%M %p")))


time_before_hours(5)


#5
def date_after_weeks(weeks):

	dt = datetime.now() + timedelta(weeks=weeks)
	print("Current date is ", datetime.now().strftime("%m-%d-%y"))
	print("The date after {:d} weeks is ".format(weeks), dt.strftime("%m-%d-%y"))


date_after_weeks(10)


#6
def date_before_weeks(weeks):

	dt = datetime.now() - timedelta(weeks=weeks)
	print("Current date is ", datetime.now().strftime("%m-%d-%y"))
	print("The date {:d} weeks ago is ".format(weeks), dt.strftime("%m-%d-%y"))


date_before_weeks(10)


#7
def calculate_age(dtob):
	today = datetime.date.today()
	return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))

print(calculate_age(date(1997,5,4)))


#8
def get_time():

	return datetime.now().strftime("Current time is: %I:%M:%S")

print (get_time())


#9
def get_date():

	return datetime.now().strftime("The date today is %B %d, %Y")

print (get_date())


#10
def record_time():
	response = input("Would you like to record your time in?(Y or N) ").lower()

		if response == 'y':
			return ("Your timed in on {}:{} {}").format(datetime.now().strftime('%I'), datetime.now().minute, datetime.now().strftime('%p'))

		elif response == 'n':
			return "You refused to time in"

		else:
			return "Input only Y or N!"


print(record_time())



