def find_middle_number(a, b, c):
    numbers = [ a, b, c]
    numbers.sort()
    return numbers[1]
num1 = float(input("Please enter number 1: "))
num2 = float(input("Please enter number 2: "))
num3 = float(input("Please enter number 3: "))
middle_number = find_middle_number(num1, num2, num3)
print(f"{middle_number} is the middle number")
