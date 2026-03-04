#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"        

        
with open("./Input/Names/invited_names.txt") as n_file:
    names = n_file.readlines()
  
with open("./Input/Letters/starting_letter.txt") as s_letter:
    l_contents = s_letter.read()
    print(l_contents) 
    for name in names:
       #strip the name of the excess space
        s_name = name.strip()
        #replace [name with Placeholder]
        n_letter = l_contents.replace(PLACEHOLDER,s_name)
        print(n_letter)
                
#       #renaming files
        with open(f"./Output/ReadyToSend/letter_for_{s_name}.txt", mode = "w") as c_letter:
            c_letter.write(n_letter)