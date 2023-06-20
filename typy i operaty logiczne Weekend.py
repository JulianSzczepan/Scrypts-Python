print('1 Wersja')
IsWeekend=True
print('IsWeekend =',IsWeekend)

Temperature =20
print('Temperature =',Temperature)

ToDoList=''
print('ToDoList=',ToDoList)

IsHappy =IsWeekend and Temperature >= 20 and ToDoList == ''
print('IsHappy=', IsHappy)
print(' ')
print('2 Wersja')
IsWeekend=True
print('IsWeekend =',IsWeekend)

Temperature =5
print('Temperature =',Temperature)

ToDoList=''
print('ToDoList=',ToDoList)

IsHappy = IsWeekend and Temperature >= 20 and ToDoList == ''
print('IsHappy=', IsHappy)
print(' ')
print('3 Wersja')
IsWeekend=False
print('IsWeekend =',IsWeekend)

Temperature =5
print('Temperature =',Temperature)

ToDoList='Shopping'
print('ToDoList=',ToDoList)

IsHappy =not IsWeekend and Temperature >= 20 and ToDoList != ''
print('IsHappy=', IsHappy)

IsHappy = IsWeekend and Temperature >= 20 and ToDoList == ''\
or not IsWeekend and Temperature < 20 and ToDoList !=''
print('IsHappy',IsHappy)
print('IsHappy', IsHappy)
print(' ')
print('4 Wersja')
IsWeekend=False
print('IsWeekend =',IsWeekend)

Temperature =5
print('Temperature =',Temperature)

ToDoList='Shopping'
print('ToDoList=',ToDoList)

IsHappy =not IsWeekend and Temperature >= 20 and ToDoList != ''
print('IsHappy=', IsHappy)

IsHappy = IsWeekend and Temperature >= 20 and ToDoList == ''\
or not IsWeekend and Temperature < 20 and ToDoList !=''
print('IsHappy',IsHappy)
print('IsHappy', IsHappy)
print(' ')
print('5 Wersja')
IsWeekend=False
print('IsWeekend =',IsWeekend)

Temperature =5
print('Temperature =',Temperature)

ToDoList='Shopping'
print('ToDoList=',ToDoList)

IsHappy =not IsWeekend and Temperature >= 20 and ToDoList != ''
print('IsHappy', IsHappy)

IsHappy = IsWeekend and Temperature >= 20 and ToDoList == ''\
or not IsWeekend and Temperature < 20 and ToDoList !=''
print('IsHappy',IsHappy)
print('IsHappy=', IsHappy)
print(' ')
print('6 Wersja')
IsWeekend = False
print('IsWeekend =',IsWeekend)

Temperature =5
print('Temperature =',Temperature)

ToDoList='Shopping'
print('ToDoList=',ToDoList)

IsHappy =not IsWeekend and Temperature >= 20 and ToDoList == ''
print('IsHappy =', IsHappy)

IsHappy =not IsWeekend and Temperature < 20 and ToDoList != ''
print('IsHappy =', IsHappy)

IsHappy = IsWeekend and Temperature >= 20 and ToDoList == ''\
or not IsWeekend and Temperature < 20 and ToDoList !=''
print('IsHappy =',IsHappy)
print(' ')
print('7 Wersja')
IsWeekend = False
print('IsWeekend =',IsWeekend)

Temperature =25
print('Temperature =',Temperature)

ToDoList='Shopping'
print('ToDoList=',ToDoList)

IsHappy =not IsWeekend and Temperature >= 20 and ToDoList == ''
print('IsHappy =', IsHappy)

IsHappy =not IsWeekend and Temperature < 20 and ToDoList != ''
print('IsHappy =', IsHappy)

IsHappy = IsWeekend and Temperature >= 20 and ToDoList == ''\
or not IsWeekend and Temperature < 20 and ToDoList !=''
print('IsHappy =',IsHappy)
print(' ')
print('8 Wersja')
IsWeekend = True
print('IsWeekend =',IsWeekend)

Temperature =25
print('Temperature =',Temperature)

ToDoList=''
print('ToDoList=',ToDoList)

IsHappy =not IsWeekend and Temperature >= 20 and ToDoList == ''
print('IsHappy =', IsHappy)

IsHappy =not IsWeekend and Temperature < 20 and ToDoList != ''
print('IsHappy =', IsHappy)

IsHappy = IsWeekend and Temperature >= 20 and ToDoList == ''\
or not IsWeekend and Temperature < 20 and ToDoList !=''
print('IsHappy =',IsHappy)
print('')
print('przekształcanie warunków')
print('')
IsWeekend = True
print('IsWeekend =',IsWeekend)

Temperature =25
print('Temperature =',Temperature)

ToDoList=''
print('ToDoList=',ToDoList)
IsHappy = IsWeekend and Temperature >= 20 and ToDoList == ''\
or not IsWeekend and not Temperature >= 20 and ToDoList !=''
print('IsHappy =',IsHappy)
print('')
IsWeekend = True
print('IsWeekend =',IsWeekend)

Temperature =25
print('Temperature =',Temperature)

ToDoList=''
print('ToDoList=',ToDoList)
IsHappy = IsWeekend and Temperature >= 20 and ToDoList == ''\
or not IsWeekend and not Temperature >= 20 and not ToDoList ==''
print('IsHappy =',IsHappy)
print('')
IsWeekend = True
print('IsWeekend =',IsWeekend)

Temperature =25
print('Temperature =',Temperature)

ToDoList=''
print('ToDoList=',ToDoList)
IsHappy = IsWeekend and Temperature >= 20 and ToDoList == ''\
or not IsWeekend and not Temperature >= 20 or ToDoList ==''
print('IsHappy =',IsHappy)
