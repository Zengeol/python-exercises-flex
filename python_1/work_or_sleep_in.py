# 5. Work or Sleep In?
# Prompt the user for a day of the week just like the previous problem. 
# Except this time print "Go to work" if it's a work day and "Sleep in" if it's a weekend day.
day = int(input('Day (0-6)? '))
week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
if day<6 and day>0:
    print('Go to work.')
else:
    print('Sleep in.')