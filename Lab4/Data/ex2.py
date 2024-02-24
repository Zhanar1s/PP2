from datetime import datetime, timedelta

current_data = datetime.now()
yesterday_date = current_data + timedelta( days = 1)
tomorrow_data = current_data - timedelta(days = 1)

print("Yesterday date:", yesterday_date)
print("The current date:", current_data)
print("Tomorrow date:", tomorrow_data)