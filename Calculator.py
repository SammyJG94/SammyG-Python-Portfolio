action = input("What operation would you like performed? Addition, Subtraction, Division, or Multiplication? ")

try:
    first_num = int(input("What is the first number? "))
    second_num = int(input("What is the second number? "))
except ValueError:
    print("Invalid input. Please enter an integer.")

# Perform the actions
if action == "Addition":
    print(f"{first_num} + {second_num}")
    print("Answer:", first_num + second_num)
elif action == "Subtraction":
    print(f"{first_num} - {second_num}")
    print("Answer:", first_num - second_num)
elif action =="Division":
    print(f"{first_num} / {second_num}")
    print("Answer:", first_num / second_num)
elif action == "Multiplication":
    print(f"{first_num} + {second_num}")
    print("Answer:", first_num * second_num)
else:
    print(f"{action} is not recognized. Please enter a valid action.")