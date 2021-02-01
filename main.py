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
