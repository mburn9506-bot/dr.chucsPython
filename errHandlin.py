"""
error handling is your code's safety net!
it catches mistakes like division by zero or bad input
keeping your program running smoothly
handles errors to keep code running smoothly
"""
try:
        result = 10/0
except ZeroDivisionError:
        print("can't divide by zero")
#catches invalid input errors.
try:
        number = int(input("enter a number: "))
        print(number)
except ValueError:
        print("thats not a number")

# handles division and input errors together
try:
        num = int(input("enter a number: "))
        result =10/num
except ValueError:
        print("not a number")
except ZeroDivisionError:
        print("can't divde by zero")
else:
        print(f"result: {result}")
# https://youtu.be/XX44XYjK_JQ?t=3083
# adds cleanup code that aleways executes
finally:
        print("done calculating")
# builds a safe calculator with error handling
try:
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second number: "))
        op = input("enter operation (+,-,*,/): ")
        if op == "/":
                result = num1 / num2
        elif op == "*":
                result = num1 * num2
        elif op == "+":
                result = num1 + num2
        elif op == "-":
                result = num1 - num2
        else:
                raise ValueError("invalid operation")
except ValueError as e:
        print(f"error: {e}")
except ZeroDivisionError:
        print("error can't divide by zero")
else:
        print(f"result: {result}")
finally:
        print("ready for next calculation")