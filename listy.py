państwa=['FR','PL','DE','US']
print(państwa)
państwa[2]='UK'
państwa.append('DE')
#dodanie na koniec listy

państwa.insert(2,'ES')
#wstawienie na konkretną pozycję

państwa.remove('DE')
#usunięcie elementu

państwa.sort()
#sortowanie alfabetyczne

państwa.reverse()
#odwrócienie

print(państwa.index('PL'))
#wskazuje na jakiej pozycji znajduje sie wskazane słowo

print(państwa.count('DE'))
#policz ile jest ""

nowe=['FI','CR']
państwa.extend(nowe)

#dodanie nowej listy
print(państwa)

państwaNowa=państwa.copy()
print(państwaNowa)
#kopiowanie listy i tworzenie nowej listy
nowe2=['kghm','pkp']
państwaNowa.extend(nowe2)
print(państwaNowa)
print(państwa)
państwaNowa.clear()
print(państwa.pop(2))
#funkcja .pop (position) wyciąga element z listy i pokazuje tylko ten element (usówa resztę)


