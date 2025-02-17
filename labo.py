def add():
    n = int(input("Enter the number of values to add: "))
    numbers = [float(input(f"Enter number {i+1}: ")) for i in range(n)]
    return sum(numbers)

def reverse():
    num = input("Enter a number to reverse: ")
    return num[::-1]

def user_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    profession = input("Enter your degree: ")
    return f"Hello {name}, you are {age} years old and your degree is {profession}."

def unique_numbers():
    n = int(input("Enter the number of values: "))
    numbers = set()
    for _ in range(n):
        num = int(input("Enter a number: "))
        numbers.add(num)
    return numbers

print("Sum of numbers:", add())
print("Reversed number:", reverse())
print(user_info())
print("Unique numbers:", unique_numbers())
