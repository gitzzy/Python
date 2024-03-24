try:
    a = int(input("Dividend : "))
    b = int(input("Divisor : "))
    res = a / b
    print(res)
# except ZeroDivisionError:
#     print("Divisor can not be zero")
# except ValueError:
#     print("please enter number only")
except Exception as e:
    print(e)
finally:
    print("Finally block")