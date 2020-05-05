"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    # Creating a dictionary to calculate how much time each person spent on phone.
    # Key = Phone Number , Value = count of seconds spent on phone.
    timeOnPhone = {}
    for caller in calls:
        timeOnPhone[caller[0]] = timeOnPhone.get(caller[0], 0) + int(caller[3])
        timeOnPhone[caller[1]] = timeOnPhone.get(caller[1], 0) + int(caller[3])

    # Finding the maximum time spent on phone now.
    maxCaller = ""
    maxTime = 0
    for caller, time in timeOnPhone.items():
        if maxTime < time:
            maxCaller = caller
            maxTime = time

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(maxCaller, maxTime))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

