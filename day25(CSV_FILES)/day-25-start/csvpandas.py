#using csv module for csv files.
import csv
with open("./weather_data.csv") as w_data:
    data = csv.reader(w_data)
    temps = []
    for row in data:
        print(row)
        if row[1] != "temp":
            temps.append(int(row[1]))
    print(temps)

#using pandas for better formatting of csv data
import pandas
data = pandas.read_csv("./weather_data.csv")
# print(data)
temp = data["temp"]
# print(temp)

temp_list = temp.to_list()
for t in temp_list:
    avg = sum(temp_list)/len(temp_list)
print(avg)

# get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day =="Monday"]
print(monday.condition)
print(monday.temp)

#create a csv file.
data_dict = {
    "students": ["Amy","James","Angela"],
    "scores": [76,56,65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)