
import calcP
print(calcP)

#define your functions for the operations chosen
def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mult(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 /n2

#store the operators in a dictionary once you know all their keys and values instead of using dic_name[keys]=values.
oPs = {
    "+":add,
    "-":sub,
    "*":mult,
    "/":div
}

#create a function to control the repetitive code.
def calc():
    continueCon = True
    #ask user for first input
    n1 = float(input("What is the first number: "))

    #create a while loop to continue looping inside of function
    while continueCon:
                
        #ask the user to input an arithmetic operator
        calcFunction = input("What function will you choose today (+ , - , * , / ): ")
        
        #ask user for second input
        n2 = float(input("What is your second number: "))
        
        #for simplicity sake store complicated operations or expressions inside of variables to be used later
        ans = oPs[calcFunction](n1,n2)
        
        #using f-strings print out the result.
        print(f"The result of your decisions today is {n1} {calcFunction} {n2} = {ans}")
        
        #ask user if they would like to continue with current ans or start fresh
        choice = input(f"Would you like to continue calculating with {ans}, or type 'n' to start over!")
        if choice == "y":
            n1 = ans
        else:
            continueCon = False
            print("\n"* 5)
            
            #this is known as recursion in programming when the function is called within itself. It therefore causes a infinite loop until something is done differently
            print(calcP)
            #if you want to be in an infinite loop leave calc() inside the while loop
            calc()
#if you want it to end just call it outside of the loop only
calc()
        
    
