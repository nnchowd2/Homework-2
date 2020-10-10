date_list = {"January": "1", "February": "2", "March": "3", "April": "4", "May": "5", "June": "6",
             "July": "7", "August": "8", "September": "9", "October": "10", "November": "11", "December": "12"}


inputDates = open("C:\\Users\\nafis\\Desktop\\Importante\\Prog\\inputDates.txt", "r")

month1 = " "
day = " "
year = " "

while True:
    dates = inputDates.read()
    if not dates:
        break
    for i in inputDates:
        if i != "-1":
            string = i.split()
            month = string[0]
            day = string[1]
            year = string[2]
            day = day.replace(',', '')
            if month in date_list:
                month1 = date_list[month]
                print("{}/{}/{}".format(month1, day, year))
        elif i == "-1":
            pass
        else:
            break
inputDates.close()




