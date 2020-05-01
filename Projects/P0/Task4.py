"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    listOfAllCallers = []
    print(calls)
    for callers in calls:
        listOfAllCallers.append(callers[0])
    # Removing the numbers which received calls.
    for callers in calls:
        if callers[1] in listOfAllCallers:
            listOfAllCallers.remove(callers[1])

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    # Removing numbers that sent or received texts
    for texters in texts:
        if texters[0] in listOfAllCallers:
            listOfAllCallers.remove(texters[0])
        if texters[1] in listOfAllCallers:
            listOfAllCallers.remove(texters[1])

listOfAllCallers = set(listOfAllCallers)
listOfAllCallers = list(listOfAllCallers)
listOfAllCallers = sorted(listOfAllCallers)
print("These numbers could be telemarketers: ")
for caller in listOfAllCallers:
    print(caller)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

