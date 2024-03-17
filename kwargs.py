# **kwargs = parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword argumement

def hello(**kwargs):
    kwargs[0] = Ms.
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print (value,end=" ")

hello(title="Mr.", first="Bro", middle="Dude", Last="Code")