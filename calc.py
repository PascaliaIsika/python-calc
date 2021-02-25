num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
print("select operations you want to perform")
operations = int(input("1.Addition,2 .Subtraction, 3.Multiplication,4.Division\n\n"))
if operations == 1:
    addition = num1 + num2
    print(f"  addition value is = {addition}")
elif operations == 2:
    subtraction = num1 - num2
    print(f" subtraction value is = {subtraction} ")
elif operations == 3:
    multiplication = num1 * num2
    print(f" multiplication value is = {multiplication} ")
elif operations == 4:
    Division = num1 / num2
    print(f" Division value is = {Division} ")
else:
    print("please select the given operations")





