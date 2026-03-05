# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     print(key,value)
# # for (key) in student_dict.keys():
# #     #Access key and value
# #     print(key)

# import pandas

# #save organized DataFrame as variable
# student_data_frame = pandas.DataFrame(student_dict)

# #long way
# # for(keys,values) in student_data_frame.items():
# #     print(keys)
# #     print(values)

# #Loop through rows of a data frame using Panda Methods
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     if row.student == "Angela":
#         print(row.score)

student_data_frame = pandas.DataFrame(student_dict)

#long way
# for(keys,values) in student_data_frame.items():
#     print(keys)
#     print(values)

#Loop through rows of a data frame using Panda Methods
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    if row.student == "Angela":
        print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format using dictionary comprehension
{"A": "Alfa", "B": "Bravo"}


data = pandas.read_csv("./nato_phonetic_alphabet.csv")
# print(data.to_dict())
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}
# print(phonetic_dict)

# {for (index, row) in df.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
