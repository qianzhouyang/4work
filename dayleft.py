import datetime

deadline = datetime.date(2023, 3, 1)  # replace with your own deadline

today = datetime.date.today()
days_left = (deadline - today).days

print(f"There are {days_left} days left until the deadline.")
