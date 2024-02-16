import random, os

correct = 0
attempts = 0
os.system("cls")

while correct < 10:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    match random.randint(1, 3):
        case 1:
            c = int(input(f"{a} + {b} = "))
            result = a + b
        case 2:
            c = int(input(f"{a} - {b} = "))
            result = a - b
        case 3:
            c = int(input(f"{a} * {b} = "))
            result = a * b

    if result == c:
        print("Correct!")
        correct += 1
    else:
        print("Incorrect!")

    attempts += 1

print(f"You have answered {(correct / attempts) * 100}% of the questions correctly.")