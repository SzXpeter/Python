from peak import Peak

list_of_peaks : list[Peak] = []

def load_from_file():
    file = open("hegyekMo.txt", 'r', encoding='utf-8')
    file.readline()
    for row in file:
        list_of_peaks.append(Peak(row.strip()))
    file.close()

def count():
    i = 0
    for p in list_of_peaks:
        i += 1
    return i

def average_height():
    n = 0
    for p in list_of_peaks:
        n += p.height
    return n/count()

def highest_mountain():
    max = 0
    i = 0
    for p in list_of_peaks:
        if p.height >= list_of_peaks[max].height:
            max = i
        i += 1
    return list_of_peaks[max]

def higher_than(height):
    i = 0
    while i < len(list_of_peaks):
        if height < list_of_peaks[i].height:
            return list_of_peaks[i]
        i += 1

def higher_then_3000f():
    i = 0
    for p in list_of_peaks:
        if p.height * 3.280839895 > 3000:
            i += 1
    return i

# def statistics():

def write_to_file():
    f = open("bukk-videk.txt", 'w', encoding='utf-8')
    f.write("Hegycsúcs neve;Magasság lábban")
    for p in list_of_peaks:
        if p.mountain == "Bükk-vidék":
            f.write(f"{p.name};{(p.height * 3.280839895):.1f}\n")
    f.close()
