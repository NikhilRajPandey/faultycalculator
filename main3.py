# its difenitly work without any Quary
# making a faulty calculator

# taking input from the user and changing into integer
inp1 = input("Operator")

# taking 2nd input from user
inp2 = input("First number")

# taking 3rd number
inp3 = input("Last number")

# making a new variable
new_input = inp2 + inp1 + inp3

# checking the input
if new_input == "45*3":
    print(555)
elif new_input == "56+9":
    print(77)
elif new_input == "56/6":
    print(4)
elif inp1 == "*":
    print(int(inp2) * int(inp3))
elif inp1 == "+":
    print(int(inp2) + int(inp3))
elif inp1 == "-":
    print(int(inp2) - int(inp3))
elif inp1 == "/":
    print(int(inp2) / int(inp3))
