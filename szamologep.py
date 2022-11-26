def osszeadas():
    #adatbekérés
    print("-"*20)
    szam1 = float(input("Az első szám: "))
    print("-" * 20)
    szam2 = float(input("A második szám szám: "))
    print("-" * 20)
    # számolás
    osszeg= szam1 + szam2
    # kiírás
    print("-" * 20)
    print(f"{szam1}+{szam2}={osszeg}")
    print("-" * 20)

def kivonas():
    #adatbekérés
    print("-"*20)
    szam1 = float(input("Az első szám: "))
    print("-" * 20)
    szam2 = float(input("A második szám szám: "))
    print("-" * 20)
    # számolás
    osszeg= szam1 - szam2
    # kiírás
    print("-" * 20)
    print(f"{szam1}-{szam2}={osszeg}")
    print("-" * 20)



def szamologep():
    # adatbekérés
    #lokális változó - csak a függvényen belül látszik
    szam1 = float(adatbekeres("Adj meg egy számot! "))
    muvjel = adatbekeres("Add meg a műveleti jelet! ")
    szam2 = float(adatbekeres("Adj meg még egy számot! "))
    # számolás
    szoveg=""
    eredmeny = 0
    if (muvjel=="+"):
        eredmeny = osszead(szam1, szam2)
    elif (muvjel=="-"):
        eredmeny = szam1 - szam2
    elif (muvjel == "*"):
        eredmeny = szam1 * szam2
    elif (muvjel == "/"):
        eredmeny = szam1 / szam2
    else:
        szoveg = "nem értelmezhető a művelet"
    # kiírás
    kiiras(szam1, szam2, muvjel, eredmeny, szoveg)
    # kiiras(2, 6, "gfdgsdf ", 56, "valami")

def osszead(a, b):
    e = a + b
    return e

def kiiras(szam1, szam2, muvjel, eredmeny, szoveg):
    print("-" * 20)
    if szoveg == "":
        print(f"{szam1}{muvjel}{szam2}={eredmeny}")
    else:
        print(szoveg)
    print("-" * 20)


"""paraméter átadás"""
def adatbekeres(szoveg):
    print("-" * 20)
    kismacska = (input(szoveg))
    return kismacska
    """visszatérési érték"""


