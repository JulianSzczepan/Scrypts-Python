massage1='Processing file %s'
print(massage1 % ('file_1.txt'))

massage2='File %s has size %d KB'
print(massage2 %('file_txt',1000))

massage3='Julian ma ochotę na %s ale ma tylko %d groszy'
print(massage3 %('piwo', 50))

massage8='Andrzej ma ochotę na %s ale ma tylko %d złotych'
print(massage8 %('wódkę', 20))

massage4='File %20s has size %10d KB' 
print (massage4 %('file_txt',1000))

massage5='processing file {0:s}'
print(massage5.format('failel.txt'))

massage6='file {0:s} has size {1:d}'
print(massage6.format ('filel.txt',1000))

massage7='file {0:20s} has size {1:15d}'
print(massage7.format ('filel.txt',1000))


