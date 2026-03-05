student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    print(key,value)
# for (key) in student_dict.keys():
#     #Access key and value
#     print(key)

import pandas

#save organized DataFrame as variable
student_data_frame = pandas.DataFrame(student_dict)

#long way
# for(keys,values) in student_data_frame.items():
#     print(keys)
#     print(values)

#Loop through rows of a data frame using Panda Methods
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    print(index)
    print(row)



# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
with open("./nato_phonetic_alphabet.csv") as "nato_pho":
    nato = 
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

