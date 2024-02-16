koridok = ['1:36.103', '1:57.799', '1:41.153', '1:51.697', '1:40.370', '1:36.106', '1:52.216', '1:40.766', '1:57.311', '1:39.668', '1:46.402', '1:59.298', '1:47.474', '1:44.234', '1:49.676', '1:57.474', '1:49.263', '1:36.397']
palyarekord = '1:35.887'

def masodperc(korido: str) -> float:
    ido = korido.split(':')
    return int(ido[0]) * 60 + float(ido[1])

def legyorsabb():
    minIndex = 0
    minErtek = koridok[0]
    for i in range(len(koridok) - 1):
        if masodperc(koridok[i + 1]) < masodperc(minErtek):
            minErtek = koridok[i + 1]
            minIndex = i + 1
    print(f"sorszám: {minIndex + 1}, idő: {minErtek}")


def palyarekord_e():
    global palyarekord
    for i in range(len(koridok)):
        if masodperc(koridok[i]) < palyarekord:
            palyarekord = koridok[i]

legyorsabb()