from lottery import Lottery

lottery_nums: list[Lottery] = []

def l_input():
    l_numbers = []
    for i in range(5):
        l_numbers.append(int(input(f"\t{i + 1}. szám: ")))
    return l_numbers

def read_from_file():
    file = open("lottosz.txt", 'r', encoding='utf-8')
    for f in file:
        lottery_nums.append(Lottery(f))
    file.close()