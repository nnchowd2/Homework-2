date_list = {"January": "1", "February": "2", "March": "3", "April": "4", "May": "5", "June": "6",
             "July": "7", "August": "8", "September": "9", "October": "10", "November": "11", "December": "12"}

date_input = input()

month1 = " "
day = " "
year = " "

for i in date_input:
    if i != "-1":
        string = date_input.split()
        month = string[0]
        day = string[1]
        year = string[2]
        day = day.replace(',', '')
        if month in date_list:
                month1 = date_list[month]

print("{}/{}/{}".format(month1, day, year))







