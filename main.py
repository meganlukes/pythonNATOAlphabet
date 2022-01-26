import random
import pandas
import csv

#create ditionary
#{"a": "alpha", "b": "beta"
alphabet_file = pandas.read_csv("nato_alphabet.csv")
alphabet_dict = {row.letter:row.code for (index, row) in alphabet_file.iterrows()}


name = input("What is your name?\n").upper()
name_list = list(name)
print(name_list)
name_string = [alphabet_dict[item] for item in name_list]
print(name_string)
# for (index, row) in bamboo_data_frame.iterrows():
#     if row.bamboo == "Angel Mist":
#         print(row.height)
# bamboo_ranks = {plant:random.randint(1, 6) for plant in bamboo}

#create list of nato codewords

# bamboo_dict = {
#     "bamboo": ["Timor", "Angel Mist", "Blue Chungii", "Golden Goddess"],
#     "height": [40, 30, 35, 12]
# }
# # for (key, value) in bamboo_dict.items():
# #     print(value)
#
# bamboo_data_frame = pandas.DataFrame(bamboo_dict)
# print(bamboo_data_frame)
#
# for (index, row) in bamboo_data_frame.iterrows():
#     if row.bamboo == "Angel Mist":
#         print(row.height)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day:(temp*9/5) + 32 for (day, temp) in weather_c.items()}
# print(weather_f)

# sentence = "Why is bamboo an awesome plant?"
# sentence_list = sentence.split()
# word_lengths = {word:len(word) for word in sentence_list}
# print(word_lengths)


# bamboo = ['Black', 'Blue Chungii', 'Yin Yang Yellowstripe', 'Angel Mist', 'Golden Goddess']
# bamboo_ranks = {plant:random.randint(1, 6) for plant in bamboo}
# print(bamboo_ranks)
#
# good_bamboo = {plant:score for (plant, score) in bamboo_ranks.items() if score >= 3}
# print(good_bamboo)

# with open("file1.txt") as file_1:
#     file_1 = file_1.readlines()
# with open("file2.txt") as file_2:
#     file_2 = file_2.readlines()

# file_1_num = [num.strip() for num in file_1]
# file_1_nums = [int(num) for num in file_1_num]
#
# file_2_num = [num.strip() for num in file_2]
# file_2_nums = [int(num) for num in file_2_num]
#
# newnum1 = [int(num.strip()) for num in file_1]
# newnum2 = [int(num.strip()) for num in file_2]
# common_nums = [num for num in newnum1 if num in newnum2]
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# double_numbers = [n * n for n in numbers]
# even_numbers = [n for n in numbers if n % 2 == 0]

# print(newnum1)