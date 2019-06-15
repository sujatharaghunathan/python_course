from datetime import datetime


right_this_minute = datetime.today().minute
if right_this_minute > 0 and right_this_minute < 15:
    print("0-15")
elif right_this_minute > 15 and right_this_minute < 30:
    print("15-30")
elif right_this_minute > 30 and right_this_minute < 45:
    print("30-45")
else:
    print("45-60")