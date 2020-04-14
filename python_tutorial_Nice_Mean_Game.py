#
#Python:    3.8.2
#
#Author:    Andrew Nally
#
#Purpose:   ASSIGNMENT for The Tech Academy-Python Course, Creating our first program together.
#           Demonstrating how to pass variables from function to function
#           while producing a functional game
#
#           Remember, function_name(variable) _means that we pass in the variable.
#           return variable _means we are returning the variable
#           back to the calling function.



def start():
    f_name = "sarah"
    l_name = "Smither"
    age = 28
    gender = "female"
    get_name(f_name,l_name,age,gender)



def get_name(f_name,l_name,age,gender):
    print("My name is {} {}. I am a {} yearold {}.".format(f_name,l_name,age,gender))











if __name__ == "__main__":
    start()

    
