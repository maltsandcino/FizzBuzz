
n = input("Enter a number to FizzBuzz: ")

if n.isnumeric() == False:
    while True:
        n = input("Your input was not a number. Please enter a number in digit form: ")
        if n.isnumeric():
            break

n = int(n)

print(f"\nSolving for 1 - {n}")
print("-------")

for i in range(1, n + 1):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)