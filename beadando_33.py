# paraméterként kap egy 1 és 27 közötti számot (limit), majd kiír egy N méretű betűszőnyeget.

import string


def betuszonyeg(limit):  # megírjuk a függvényt
    betuk1 = string.ascii_lowercase  # angol kisbetük,import string kell hozzá
    temp = (2 * limit) - 1 + (2 * limit - 2)  # itt adjuk meg, hogy milyen széles lesz a betűszőnyeg
    betuk = ""
    N = limit * 2

    for i in range(len(betuk1)):  # a betűk tömbjéhez hozzáadtam a "-" karaktereket, hogy később ne kelljen vele foglalkozni
        betuk = betuk + "-" + betuk1[i]

    for i in range(0, N - 2, 2):  # A felső háromszöget rajzoljuk ki
        szo = betuk[N - i - 1:N]  # egy új sztringben eltároljuk a vizsgált karaktereket
        rev_szo = szo[::-1]  # megfordítjuk
        full_szo = rev_szo + szo[1:]  # összekapcsoljuk (konkatenáljuk) a karaktersorokat, de a másodiknak az első karakterét levágjuk (pl: edcba + bcde)
        print(full_szo.center(temp,'-'))  # kiirítjuk úgy, hogy temp szélességben "-" karakterekkel legyen kitöltve a sor, középre rendezve

    for i in range(1, N, 2):  # az alsó háromszöget rajzoljuk ki, ugyanaz, mint az előbb, csak a másik háromszöggel
        szo = betuk[i:N]  # ez változik az előzőhöz képest, mert most az i karaktertől az N karakterig nézzük
        rev_szo = szo[::-1]
        full_szo = rev_szo + szo[1:]
        print(full_szo.center(temp, '-'))




betuszonyeg(5)

