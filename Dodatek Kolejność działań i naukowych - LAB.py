'''Wykładowca mówi studentom, że zaliczysz semestr jeżeli masz:
obecność co najmniej 80% i średnią >= 3.0 lub zaliczyłeś pracę semestralną.
Zbuduj wyrażenie w Python które stwierdzi czy student, który ma obecność 0.85,
średnią 3.5 i nie zaliczył pracy semestralnej zda czy nie.
'''

obecność =0.65
średnia =4.0 
praca = False

print('semestr zosatnie zalcziony jeśli obecność będize większa niż 80%\noraz średnia ocen wyższa niż 3.0 lub zaliczona praca: ', obecność >=0.8 and średnia >=3.0 or praca)

