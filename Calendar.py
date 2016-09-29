#=========================================
#Roosevelt Bannerman
#Fundamental Programming in Bioinformatics
#Calendar
#=========================================

global months, weekdays,days, nullString, dashString, NUM_MONTHS,NUM_WEEKDAYS

months = ("January","Feburary","March","April","May","June","July","August","September","October","November","December")
weekdays = ("Su","Mo","Tu","We","Th","Fr","Sa")
days = [31,28,31,30,31,30,31,31,30,31,30,31]
nullString = "\0" * 28
dashString = '-' * 28
NUM_MONTHS = 12
NUM_WEEKDAYS = 7

#=========================================
#Obtains the year from the user
#Returns the year
#=========================================
def obtainYear():
    isValid = False
    while(not isValid):
        print("\n\tPlease enter a year from 1900 to 2016 : ", end='')
        year = input()
        isValid = True
        if(not year.isdigit()):
            isValid = False
            continue
        year = int(year)
        if(year < 1900 or year > 2016):
            isValid = False
            
    return year

#=========================================
#Recieves the entered year
#Returns whether the year is a leap year
#=========================================
def isLeap(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                    return True
            return False
        return True
    return False

#=========================================
#Recieves the entered year
#Calculates the number of leap years since 1900
#Returns the number of leap years
#=========================================
def calculateLeaps(year):
    totalLeaps = 0

    for i in range(1900,year):
        if(i % 4 == 0):
            if(i % 100 == 0):
                if(i % 400 == 0):
                    totalLeaps += 1
                continue
            totalLeaps += 1
        continue;
    return totalLeaps

#=========================================
#Recieves the entered year and the total number of leap years
#Calculates the first day of the entered year
#Returns the integer for the first day of the entered year
#=========================================
def calculateDayOne(year,leaps):

    difference = year - 1900
    days = (difference * 365) + leaps
    
    return(days % NUM_WEEKDAYS)

#=========================================
#Recieves the entered year and the first day of the year
#Displays the calendar for the entered year
#=========================================
def displayResults(year,start):
    counter = start + 1
    if(counter == NUM_WEEKDAYS):
        counter = 0

    for currentMonth in range(12):
        spacing = int(((23 - len(months[currentMonth]))/2)) * ' '
        print("\n" + spacing + months[currentMonth] + " " + str(year))

        for day in weekdays:
            print("  " + day,end='')
            
        print("\n" + dashString)

        start = (0 + (4*counter)) * ' '
        print(start,end='')
        
        for currentDay in range(1,days[currentMonth]+1):
            if(currentDay > 9):
                print("  " + str(currentDay),end='')
                counter += 1
                if(counter == NUM_WEEKDAYS):
                    if(currentDay != days[currentMonth]):
                        print()
                    counter = 0
            else:
                print("   " + str(currentDay),end='')
                counter += 1
                if(counter == NUM_WEEKDAYS):
                    if(currentDay != days[currentMonth]):
                        print()
                    counter = 0
        print()    
    print()    
            

    
#=========================================
#Executes the Program
#=========================================
def runProgram():
    year = obtainYear()
    if(isLeap(year)):
        days[1] = 29
    totalLeaps = calculateLeaps(year)
    dayOne = calculateDayOne(year,totalLeaps)
    displayResults(year,dayOne)
    stop = input()

runProgram()







