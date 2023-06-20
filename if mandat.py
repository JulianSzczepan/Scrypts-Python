mandat = int(input("Podaj liczbę kilometrów, o jaką przekroczyłeś dozwoloną prędkość: "))
if mandat <= 10:
    print("mandat: 100zł")
elif mandat <= 30:
    print("mandat: 200zł")
else:
    print("mandat: 400zł")
