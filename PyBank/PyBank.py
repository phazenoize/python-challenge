import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

#Month counter
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    listLen = 0
    for row in reader:
        listLen += 1

#separating the PNL column and then using += to kill two birds with one stone
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    totalOf = 0
    for row in reader:
        if len(row) > 1:
            value = int(row[1])
            totalOf += value

#calculate the change between the months, storing that value and then 
#finding the average of that value
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    profit = []
    lastValue = None
    for row in reader:
        values = int(row[1])
        if lastValue is not None:
            change = values - lastValue
            profit.append(change)
        lastValue = values
totalChanges = sum(profit)
averageChange = totalChanges / len(profit)

#using nested conditionals in order to calculate the largest increase in 
#profits from the sheet
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    maxIncrease = int(0)
    maxDate = None
    prevValue1 = None
    for row in reader:
        date1 = row[0]
        value1 = int(row[1])
        if prevValue1 is not None:
            increase = value1 - prevValue1
            if increase > maxIncrease:
                maxIncrease = increase
                maxDate = date1
        prevValue1 = value1

#use the exact same code as above, except change the variable names and
#flip the logic in order to find the largest loss        
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    minIncrease = int(0)
    minDate = None
    prevValue2 = None
    for row in reader:
        date2 = row[0]
        value2 = int(row[1])
        if prevValue2 is not None:
            decrease = value2 - prevValue2
            if decrease < minIncrease:
                minIncrease = decrease
                minDate = date2
        prevValue2 = value2

#Final print statements
print("Financial Analysis")
print("-----------------------------------------------------------")
print("Number of months: ",listLen)
print("Total profit for this period is: $",totalOf)
print("The average change is: $",round(averageChange,2))
print("The greatest increase in profits was: " + str(maxDate) + " of $" + str(maxIncrease))
print("The greatest decrease in profits was: " + str(minDate) + " of $" + str(minIncrease))

#saving output to a string for easy text file writing
output_string = ""
output_string += "Financial Analysis" + "\n"
output_string += "-----------------------------------------------------------" + "\n"
output_string += "Number of months: " + str(listLen) + "\n"
output_string += "Total profit for this period is: $" + str(totalOf) + "\n"
output_string += "The average change is: $" + str(round(averageChange,2)) + "\n"
output_string += "The greatest increase in profits was: " + str(maxDate) + " of $" + str(maxIncrease) + "\n"
output_string += "The greatest decrease in profits was: " + str(minDate) + " of $" + str(minIncrease) + "\n"

with open("output.txt", "w") as file:
    file.write(output_string)