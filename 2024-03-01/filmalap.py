def oraperc(osszperc):
    ora = int(osszperc) // 60
    perc = int(osszperc) % 60
    return str(ora) + "óra " + str(perc) + "perc"