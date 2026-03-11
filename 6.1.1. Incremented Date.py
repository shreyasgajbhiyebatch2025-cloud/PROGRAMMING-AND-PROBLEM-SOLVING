def is_leap_year(year):
    
	return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

def get_days_in_month(month, year):

	if month in [1, 3, 5, 7, 8, 10, 12]:
		return 31
	elif month in [4, 6, 9, 11]:
		return 30
	elif month == 2:
		return 29 if is_leap_year(year) else 28
	else:
		return 0  

def validate_date(day, month, year):
	if year <= 0:
		return False
	if month < 1 or month > 12:
		return False
	days_in_month = get_days_in_month(month, year)
	if day < 1 or day > days_in_month:
		return False
	return True

def next_day(day, month, year):
	days_in_month = get_days_in_month(month, year)
	if day < days_in_month:
		return day + 1, month, year
	else:
		if month == 12:  
			return 1, 1, year + 1
		else:  
			return 1, month + 1, year


day = int(input())
month = int(input())
year = int(input())


if validate_date(day, month, year):
	nd, nm, ny = next_day(day, month, year)
	print(f"{nd:02d}-{nm:02d}-{ny}")
else:
	print("Invalid Date")

 
