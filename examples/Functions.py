import ledpanel

#functions let us bundle up a bit of logic so that we can reuse it easily later
#we make a function with 'def {name}' where {name} is a name of our choice. 
#a function takes in some data and gives some back.


#this just defines the function- it wont run till we 'call ' it
def example_function_name( example_input_data):
    #this will print first, reversing whatever the input data was.
    print( example_input_data)
    #then the function will return
    return example_input_data + example_input_data


example_function_parameter = input("Do an input : ")

#we run the function and store the output
example_function_output = example_function_name(example_function_parameter)

#then we print the output
ledpanel.PrintPanelRGB(example_function_output)


##ADVANCED##
#if functions have the same inputs and outputs, we can treat them interchangeably
n = 3

def goUp(num):
    return num+1

def goDown(num):
    return num-1

choice = input("My number is " + str(n) +". Should it go up or down? : ")

f = goUp

if(choice=="down"):
    f = goDown

n = f(n)
print("Now it's " + str(n))