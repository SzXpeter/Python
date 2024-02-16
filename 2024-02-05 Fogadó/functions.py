from foglalas import Foglalas

foglalasok: list[Foglalas] = []

def read_from_file():
    file = open('fogado.txt', 'r', encoding='utf-8')
    for row in file:
        foglalasok.append(Foglalas(row))
    file.close()

def search_for_appointment(teacher):
    i = 0
    for n in foglalasok:
        if n.name == teacher:
            i += 1
    return i

def search_for_teachers(appointment):
    teaches: list[Foglalas] = []
    file = open(f'{appointment.replace(':', '')}.txt', 'w', encoding='utf-8')
    for teach in foglalasok:
        if teach.appointment == appointment:
            print(teach.name)
            file.write(f"{teach.name}\n")
    file.close()

def free_appointments():
    f_a = ["16:00", "16:10", "16:20", "16:30", "16:40", "16:50",
           "17:00", "17:10", "17:20", "17:30", "17:40", "17:50"]  
    for f in foglalasok:
        if f.name == "Barna Eszter":
            f_a.remove(f.appointment)
    
    for i in f_a:
        print(i)

    if f_a[-1] != "17:50":
        print("Barna Eszter legkorábban távozhat: 18:00")
    else:
        for i in range(len(f_a) - 1, -1, -1):
            if i == 0 or free_appointments_difference(f_a[i], f_a[i-1]) > 10:
                print(f"Barna Eszter legkorábban távozhat: {f_a[i]}")
                break

def free_appointments_difference(app1:str, app2:str):
    ora1, perc1 = app1.split(':')
    ora2, perc2 = app2.split(':')

    return int(ora1) * 60 + int(perc1) - (int(ora2) * 60 + int(perc2))