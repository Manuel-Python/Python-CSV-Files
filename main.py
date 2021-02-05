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

# data = pandas.read_csv("data.csv")
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average = sum(temp_list) / len(temp_list)
# print(average)
#
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].mode())
# print(data.condition)
#
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# print(int(monday.temp) * 9 / 5 + 32)
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data_frame = pandas.DataFrame(data_dict)
# print(data_frame)
#
# data_frame.to_csv("new_data.csv")

data = pandas.read_csv("squirrel.csv")
# grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# print(data_dict)
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("sqirrel_count.csv")
squirrel_num = data[data["Unique Squirrel ID"] == "30B-AM-1007-04"]

data_dict = {
    "Co-ords": ["X", "Y", "ID"],
    "Data": [data["Y"], data["X"], data["Unique Squirrel ID"]]
}
print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("sqirrel_data.csv")

squirrel_num1 = data[data["Highlight Fur Color"] == "White"]
print(squirrel_num1)
