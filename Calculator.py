#since we will be working with time, we first import the
# datetime,time and timedelta modules

# Efa Akoto wrote the codes in reference to the instructions relating to the functionalities of the wage calculator.

from datetime import datetime, date, time, timedelta
import csv 
import random

choice = 'random'


print("hello, welcome to the Wage Calculator")


def line():
    print('------------------------------------------')

def show_menu():
    line()
    print('press 1 to view instructions')
    print('press 2 to Exit instructions')
    choice = input('Enter your choice: ')
    return choice

while choice != '2':
    choice = show_menu()
    
    if choice == '1':
        print("The format for the date and time is YY MM D H M  where the values are separated with spaces:")
        print("YY is the year. e.g 2020")
        print("MM is the month. e.g 01 stands for January, 02 stands for February etc")
        print("D is the day.")
        print("H is the hours: the calculator uses the 24hrs model, meaning 1A.M=1, 1P.M=13,2A.M=2,2P.M=14 etc")
        print("M is the minutes.")
        print("Number of hours and minute off project  format is H M e.g 2 30  ")
    else:
        print('Enjoy your time here')
#Efa Akoto Comment Ended


        
# Emmanuel Akpe created the code to take user inputs on dates and time.        
# we then set a while condtion to find the start,end and break times of 
#the project


DateStart, DateEnd, Number_Hours_Minutes_off= None, None, None

print("time format is YY MM D H M e.g 2020/02/05 8:00= 2020 02 05 8 00")
while DateStart is None:
    DateEntry = input("Enter Date and Time at start of work YY MM D H M ")
    print('--------------------------------------------------------------------')
    
    try:
        DateStart = datetime.strptime(DateEntry, "%Y %m %d %H %M")
    except ValueError:
          print("Input must be \"YY MM D H M e.g 2020/02/05 8:00= 2020 02 05 8 00 \"")
   

while DateEnd is None:
    DateEntry = input("Enter Date and Time at end of work YY MM D H M ? ")
    print('--------------------------------------------------------------------')
    
    try:
        DateEnd = datetime.strptime(DateEntry, "%Y %m %d %H %M")
    except ValueError:
          print("Input must be \"YY MM D H M e.g 2020/02/05 8:00= 2020 02 05 8 00 \"")

while Number_Hours_Minutes_off is None:
    DateEntry = input("Enter number of hours and minutes off per day H M ? ")
    print('--------------------------------------------------------------------')
    try:
        Number_Hours_Minutes_off = datetime.strptime(DateEntry, "%H %M")
    except ValueError:
           print("Input must be  H M e.g 2Hrs30mins=2 30 separted by space \"")

number_of_days_work=int(input('Enter days available for work '))
print('-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->')

#Emmanuel Akpe Comment Ended


#Emmanuel Agyekum created this code to calculate the total hours worked and the
# total wage

#To find the total time spent on the project, we have to subtract the 
#time spent on break and the start time from the end date

Time_difference=(DateEnd-DateStart)
BreakMinute=Number_Hours_Minutes_off.minute
BreakHour=Number_Hours_Minutes_off.hour

#We then multiply the time spent with the amount earned on hourly
# basis to obtain the total amount earned after the task.

Total_Time_available=Time_difference.total_seconds()/(60*60)
total_Time_worked=Total_Time_available-(BreakHour+BreakMinute/60)*number_of_days_work

print('your total time spent on the project is', total_Time_worked, 'hrs')

print('Your total money made on the project is $',total_Time_worked*5 )

print('-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->-->')



with  open('tracker_log.csv', "a", newline="") as log:
    writer = csv.writer(log)
    writer.writerow(['Start Date and Time',  'Finish Date and Time',  'Hours and Minutes off','Hours Worked' ,'Money Made'])
    writer.writerow([ DateStart, DateEnd,  Number_Hours_Minutes_off,total_Time_worked, total_Time_worked*5])
    
log.close() 

        
