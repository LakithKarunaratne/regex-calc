import re  # regex library

print("Calculator")
print(" enter 'q' to exit\n")
print(" enter 'del' to clear memory\n")
print(" enter 'M' to show memory\n")

previous = 0
run = True  # program run condition

# perform mathematical calculations 
def performMath():
    # import global var
    global run
    global previous

    if previous == 0:
        equation = input("Enter equation : ")
    else:
        equation = input(str(previous))

    if equation == 'q':  # set condition to end program
        previous = 'quit'
        run = False
    elif equation == 'del':  # delete function
        previous = 0
    elif equation == 'm':  # show memory
        if previous is not None:
            print(previous)
        else:
            print("memory blank")
    else:
        # check if the input is an empty string
        if equation == '':
            print(previous)
		# check if there are any digits in the input <-- might slow down o(n)
        elif any(char.isdigit() for char in equation):
            # clean the input
            equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

            # check if there was no value before
            if previous == 0:
				# evaluate the input in python repl
                previous = eval(equation) 
            else:
				# evaluate together with the previous value 
                previous = eval(str(previous) + equation)
        else:
            print("enter valid numeric input")

while run:
    performMath()
