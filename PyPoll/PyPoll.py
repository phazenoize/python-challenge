import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

#initial vote count for total vote number
#uses for loop with a counter function
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    voteCount = 0
    for rows in reader:
        voteCount += 1
#using nested for loops  and if statements to determine
#the amount of votes each candidate received       
with open(csvpath) as csvfile1:
    reader1 = csv.reader(csvfile1, delimiter=',')
    header1 = next(reader1)
    name1 = "Charles Casper Stockham"
    name2 = "Diana DeGette"
    name3 = "Raymon Anthony Doane"
    name1Counter = 0
    name2Counter = 0
    name3Counter = 0
    winnerIs = str()
    for row in reader1:
        for names in row:
            if name1 in names:
                name1Counter += 1
            if name2 in names:
                name2Counter += 1
            if name3 in names:
                name3Counter += 1
    value1 = round((name1Counter / voteCount) * 100,2)
    value2 = round((name2Counter / voteCount) * 100,2)
    value3 = round((name3Counter / voteCount) * 100,2)

    #simple logic test to determine the winner
    if value1 > value2 > value3:
        winnerIs = name1
    if value2 > value1 > value3:
        winnerIs = name2
    else:
        winnerIs = name3
#command prompt output statements        
print("Total Votes: ",voteCount)
print(name1 + ": " + str(value1) + "%" + " (" + str(name1Counter) + ")")
print(name2 + ": " + str(value2) + "%" + " (" + str(name2Counter) + ")")
print(name3 + ": " + str(value3) + "%" + " (" + str(name3Counter) + ")")
print("The winner is: " + winnerIs)

#converting output statements to a string for easy writing to a text file
output_string = ""
output_string += "Total Votes: " + str(voteCount) + "\n"
output_string += name1 + ": " + str(value1) + "%" + " (" + str(name1Counter) + ")\n"
output_string += name2 + ": " + str(value2) + "%" + " (" + str(name2Counter) + ")\n"
output_string += name3 + ": " + str(value3) + "%" + " (" + str(name3Counter) + ")\n"
output_string += "The winner is: " + winnerIs

with open("output.txt", "w") as file:
    file.write(output_string)