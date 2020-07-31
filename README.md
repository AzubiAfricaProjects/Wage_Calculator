## Wage-Calculator
This is a readme file for the Wage-Calculator.
The Wage-Calculator package provides a simple calculator interface to calculate 
the total wage earned by an individual or an organisation on 
hourly basis.

### Systems Requirements
To fully view and work with the code, a user must have python installed

### Built-With
* Python 3.7
* Spyder IDE


### Usage

The calculator is designed in a way that it takes user requests based on;
* date and time for the start of task
* date and time for the end of task
* break time(simply the hours and minutes for which a user will not work on his/her task)
* The number of days a user will be available for the task in a week.

### The Date and Time for Start and End of a task

The format for the date and time is YY MM D H M
where;
	YY is the year. e.g 2020
	MM is the month. e.g 01 stands for January, 02 stands for February etc
	D  is the day. 
	H  is the hours.
(the calculator uses the 24hrs model, meaning 1A.M=1, 1P.M=13,2A.M=2,2P.M=14 etc)
	M  is the minutes.

the variables, thus YY MM D H M are separated by space. For example, the 
datetime 25th January 2020, 2:30 A.M will be represented as 2020 01 25 2 30.
Likewise the datetime 1st February 2015, 2:30P.M will be represented as
2015 02 01 14 30

### Break Time.
it is basically in hours and minutes. It refers to the time a user will not be working
on his/her task in a day.The format for the time and date is H M where;
	H is the total number of hours a user will not work on task.
	M is the total number of minutes a user will not work on task.
For instance, a user that has a break time of 5hrs30mins will be represented as 5 30
and a user that has no break will be represented as 0.

### The Number of days of Work.
This refers to the working days of a user. That is, the number of days a user
works on the task in a week. For instance, if Kofi works from Monday to Friday, then his 
number of days of work is 5


### Acknowledgements
This project has taken great inspiration from the Azubi graduate programme 
organized by Azubi Africa.


If you want to suggest changes or additions, find an error or find anything that
does not work or no longer works, kindly file an issue or submit a pull request 
with your suggested changes
Thank You.


### Authors

* Emmanuel Akpe
Emmanuel.Akpe@azubiafrica.org
(Data Scientist)

* Efa Akoto
Efa.Akoto@azubiafrica.org
(Data Scientist)

* Emmanuel Agyekum
Emmanuel.Agyekum@azubiafrica.org
(Data Scientist)







