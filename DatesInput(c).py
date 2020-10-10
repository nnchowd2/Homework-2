#ID 1591144

date_list={"January": "1", "february": "2", "march": "3", "april": "4", "may": "5", "june": "6",
           "july": "7", "august": "8", "september": "9", "october": "10", "november": "11", "december": "12"}

inputDates = open('C:\\Users\\nafis\\Desktop\\Importante\\Prog\\inputDates.txt', 'r')
parsedDates =open('C:\\Users\\nafis\\Desktop\\Importante\\Prog\\parsedDates.txt', 'w')

for i in inputDates:
    if i != "-1":
        string = i.split()
        month = string[0]
        day = string[1]
        year = string[2]
        day = day.replace(',', '')
        if month in date_list:
            month1 = date_list[month]
            dates = month1 + "/" + day + "/" + year
            parsedDates.write(dates)

parsedDates.close()
inputDates.close()
