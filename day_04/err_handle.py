
# try:
#     file = open("missing.text", "r")
#     number = int("abc")
# except FileNotFoundError:
#     print("OOps file doesn't exist!")
# except ValueError:
#     print("Can't convert to number")
# except Exception as e:
#     print(f"Something went wrong: {e}")

# try:
#     result = 10 /  2
# except ZeroDivisionError:
#     print("Can't divide by zero!")
# else:
#     print(f"result: {result}")
# finally:
#     print("Clean up code here")

# # create customer error

# class NegativeNumberError(Exception):
#     pass

# def calculate_square_root(num):
#     if num < 0:
#         raise NegativeNumberError("No negative numbbers allowed")
#     return num ** 0.5

# try:
#     calculate_square_root(-5)
# except NegativeNumberError as e:
#     print(e)
# else:
#     print("No errors occurred")
# finally:
#     print("Always executed")


# Mini project
def safe_calculator():
    """ Calculator handles all errors"""
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator ( + , -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2
        else:
            raise ValueError("Invalid operator!")

        print(f"Result: {result}")

    except ValueError as e:
        print(f"Invalid input! {e}")
    except ZeroDivisionError as e:
        print(f"math error! {e}")
    except Exception as e:
        print(f"unexpected error: {e}")
    finally:
        print("Thanks for using calculator!")

safe_calculator()