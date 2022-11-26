szam = 2
def fv1():
    global szam
    szam1 = 3
    print(f"fv1 {szam1}")
    szam2 = 6
    print(f"fv1 {szam2}")
    szam = 20
    print(f"fv1 {szam}")
    """szam=12
    print(f"fv1 {szam}")"""
    #return szam1
    fv3(szam2)
    print(f"fv1 {szam1+3}")

print(f"globál {szam}")

def fv3(a):
    print(f"fv3 {szam}")
    #szam1 = fv1()
    print(f"fv3 {a+2}")



