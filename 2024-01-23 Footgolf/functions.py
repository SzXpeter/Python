from myClass import Footgolf

footgolfers: list[Footgolf] = []

def read_from_file():
    f = open('fob2016.txt', 'r', encoding='utf-8')
    for row in f:
        footgolfers.append(Footgolf(row))
    f.close()

def woman_percent():
    women = 0
    for foot in footgolfers:
        if foot.category == "Noi":
            women += 1
    return women / len(footgolfers)

def woman_champion():
    most_points = None
    mp_index = 0
    i = 0
    for f in footgolfers:
        points = f.total_score()
        if most_points != None:
            if points >= most_points and f.category == "Noi":
                mp_index = i
                most_points = points
        else:
            if f.category == "Noi":
                mp_index = i
                most_points = points
        i += 1

    return footgolfers[mp_index]

def write_to_file():
    file = open("osszpontFF.txt", 'w', encoding="utf-8")
    for f in footgolfers:
        if f.category == "Felnott ferfi":
            file.write(f"{f.name};{f.total_score()}\n")