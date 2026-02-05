
try:
    file = open("missing.text", "r")
    number = int("abc")
except FileNotFoundError:
    print("OOps file doesn't exist!")
except ValueError:
    print("Can't convert to number")
except Exception as e:
    print(f"Something went wrong: {e}")

try:
    result = 10 /  2
except ZeroDivisionError:
    print("Can't divide by zero!")
else:
    print(f"result: {result}")
finally:
    print("Clean up code here")

