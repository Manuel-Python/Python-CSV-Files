import pandas

# with open("data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#
#     temperature = []
#
#     for row in data:
#         print(data)
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)

data = pandas.read_csv("data.csv")
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

average = sum(temp_list) / len(temp_list)
print(average)

print(data["temp"].mean())
print(data["temp"].max())
print(data["temp"].mode())
print(data.condition)

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

print(int(monday.temp) * 9 / 5 + 32)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data_frame = pandas.DataFrame(data_dict)
print(data_frame)

data_frame.to_csv("new_data.csv")
