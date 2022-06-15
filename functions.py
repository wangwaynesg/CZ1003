import datetime #used to get the current date and time
import calendar #used for converting date into day of the week
import csv      #in order to read the csv files

def getDayFromDate(date):   #format date as string "dd/mm/yyyy"
    dayTable = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    #Test to make sure input is valid for robustness
    if type(date) != str:   #make sure it is a string
        print("Please input date as a string")
        return False
    if len(date) != 10:
        print("Format according to dd/mm/yyyy")
        return False
    dayMonthYear = date.split('/') #split string by /
    if len(dayMonthYear) != 3:  #make sure there are three elements: day, month, and year
        print("Format according to dd/mm/yyyy")
        return False

    try:
        dayFromDate = dayTable[calendar.weekday(int(dayMonthYear[2]),int(dayMonthYear[1]),int(dayMonthYear[0]))] #use .weekday method to get numeric value 0-6 representing day of the week
    except ValueError:      # catch any invalid dates, if invalid return false
        print("Invalid date given!")
        return False
    return dayFromDate  # return day as string

def getTodaysDate():        #get todays date
    now = datetime.datetime.now()       #using datetime module, .now() method will retrieve current date time
    return now.strftime("%d/%m/%Y")     #format into dd/mm/yyyy

def getCurrentTime():       #get todays time
    now = datetime.datetime.now()
    return now.strftime("%H:%M")        #format into hh/mm

def checkTimeValid(time):   #check if a time is 1. formatted as hh:mm and 2. is a valid time
    if len(time) != 5:  #hh:mm has length of 5
        return False
    time = time[0:2] + time[3:5] #remove colon
    if time.isdigit() == False: #should be an integer
        return False
    elif int(time) > 2359:    #check if time is within valid range
        return False
    else:
        return True

def isWithinTime(start,end,current):        #do comparison to check if time is within valid range
    if start < end:
        return (current >= start and current <= end)
    else:                                   #over midnight
        return (current >= start or current <= end)

def getMenuTiming(restaurant):   #get the timings for breakfast, lunch, and dinner
    breakfastTiming = ""
    lunchTiming = ""
    dinnerTiming = ""
    operatingHours = open('Operating Hours/operatinghours.csv', 'r')  # open the operatinghours csv file, read using csv.reader.
    with operatingHours:
        csv_reader = csv.reader(operatingHours, delimiter=",")
        for row in csv_reader:          #operatinghours.csv row 8,9,10 is breakfast,lunch,dinner
            if not restaurant in row:       #skip until reach correct row
                continue
            else:                           #otherwise, create record the row's menu timings
                breakfastTiming = row[8]
                lunchTiming = row[9]
                dinnerTiming = row[10]
    return [breakfastTiming, lunchTiming, dinnerTiming] #return values as a list

#above are the intermediate functions

#-------------------------------------------------FOR USE IN MAIN PROGRAM-----------------------------------------------------------
#isDateValid(date), isRestaurantAvailable(restaurant,date,time), getMenu(restaurant, date, time), calculateWaitingTime(restaurant, int numOfPax), getOperatingHours(restaurant)
#format date as string 'dd/mm/yyyy' and time as string 'hh:mm'

def isDateValid(date):
	dmy = date.split("/")
	try: #try to use datetime to return a date
		datetime.datetime(year=int(dmy[2]),month=int(dmy[1]),day=int(dmy[0]))
		return True
	except ValueError: #if date does not exist, throw a ValueError
		return False


def isRestaurantAvailable(restaurant,date = getTodaysDate(),time = getCurrentTime()):     #get all available restaurants as a list given specified date and time. format as strings "dd/mm/yyyy" and "hh:mm"

    day = getDayFromDate(date)
    dayTable = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

    if day == False or checkTimeValid(time) == False:                        #if date or time given is invalid, return False
        return False

    time = time[0:2] + time[3:5]    #remove colon

    operatingHours = open('Operating Hours/operatinghours.csv', 'r')  # open the operatinghours csv file, read using csv.reader.
    with operatingHours:
        csv_reader = csv.reader(operatingHours, delimiter=",")
        currentDay = dayTable.index(day) + 1    #this will represent the column number we will be checking within the csv file.
        for row in csv_reader:          #operatinghours.csv is organized according to: restaurant name, monday opening hour, tuesday, wed, thurs...
            if not restaurant in row:       #skip until reach correct row
                continue
            if row[currentDay].lower() == "closed": #if closed during that day, return False
                return False
            if row[currentDay].lower() == "24 hours":   #if the restaurant is always open for that day, return True
                return True
            time1 = row[currentDay][0:4]
            time2 = row[currentDay][5:9]
            if isWithinTime(int(time1), int(time2), int(time)):
                return True
        else:
            return False           

def getMenu(restaurant, date = getTodaysDate(), time = getCurrentTime()):
    day = getDayFromDate(date)
    dayTable = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    menuTable = ("Breakfast","Lunch","Dinner")
    menuDict = {}

    try:                                                                    #try to open menu csv file. if it does not exist in the directory, return false
        menu = open('Menus/'+restaurant+'.csv', 'r')
    except:
        print("Restaurant does not exist")
        return False

    if not isRestaurantAvailable(restaurant,date,time):                     #if restaurant is closed just return empty dictionary
        return menuDict
    
    if day == False or checkTimeValid(time) == False:                        #if date or time given is invalid, return False
        return False

    menuTimings = getMenuTiming(restaurant)
    currentMenu = ""
    time = time[0:2] + time[3:5]
    
    for i in menuTimings:                       #check which menu to use according to time
        if i.lower() == "no":                   #skip if menu not available for lunch/breakfast/dinner
            continue
        time1 = i[0:4]
        time2 = i[5:9]
        if isWithinTime(int(time1), int(time2), int(time)):
            currentMenu = menuTable[menuTimings.index(i)]       #Select from menuTable (Breakfast, lunch, dinner) the correct menu for the given time
            break
        
    dayIndex = dayTable.index(day) + 3       #index for column of inputted day

    with menu:
        csv_reader = csv.reader(menu, delimiter=",")
        count = 0
        for row in csv_reader:
            if count < 2:      #skip the header rows (row 0 and 1)
                count += 1
                continue
            itemName = row[0]
            itemPrice = row[1]
            if row[dayIndex].lower() == "yes" and currentMenu in row:       #if column day == yes, that item is available for that day, and is the correct menu
                menuDict[itemName] = '${:,.2f}'.format(float(itemPrice)) #append formatted price (convert to float, format float to dollar and cents). Avoids error with too many decimal places
    return menuDict
        
def calculateWaitingTime(restaurant, numOfPax):         #calculate the waiting time per pax (avg time * number of pax)
    operatingHours = open('Operating Hours/operatinghours.csv', 'r')  # open the operatinghours csv file
    with operatingHours:
        csv_reader = csv.reader(operatingHours, delimiter=",")
        for row in csv_reader:
            if not restaurant in row:       #skip until reach correct row
                continue
            return int(row[11])*numOfPax    #return calculation
    return 0                                #if never found 

def getOperatingHours(restaurant):
    timingTable = []
    operatingHours = open('Operating Hours/operatinghours.csv', 'r')  # open the operatinghours csv file
    with operatingHours:
        csv_reader = csv.reader(operatingHours, delimiter=",")
        for row in csv_reader:
            if not restaurant in row:       #skip until reach correct row
                continue
            else:
                timingTable = row[1:8]          #clone the days columns for specified restaurant
                break                           #now we can exit early
    #parse data and extract date
    if timingTable[0:5].count(timingTable[0]) == 5:  #if monday timing is repeated throughout the week, use weekdays;
        operatingHoursMessage = "Weekdays: {0} \n" \
                                "Saturday: {1} \n" \
                                "Sunday: {2}".format(timingTable[0], timingTable[5], timingTable[6])
    else:                                       #else, specify the timing for each day
        operatingHoursMessage = "Monday: {0} \nTuesday: {1} \nWednesday: {2} \n" \
                                "Thursday: {3} \nFriday {4} \nSaturday: {5} \n" \
                                "Sunday: {6}".format(timingTable[0],timingTable[1],timingTable[2],timingTable[3],timingTable[4],timingTable[5],timingTable[6])
    return operatingHoursMessage


    
#if __name__ == "__main__":
      # print(getDayFromDate("24/10/2019"))
      # print(getAvailableRestaurants("27/10/2019","03:00"))
      # print(isRestaurantAvailable("McDonald's","27/10/2019","03:00"))
      # print(getMenuTiming("McDonalds"))
      # print(getMenu("Subway","27/10/2019","13:00"))
      # print(calculateWaitingTime("Subway", 4))
      # print(getOperatingHours("Subway"))
      # print(getMenu("Burger King"))
	  #print(isDateValid('29/2/2019'))      
