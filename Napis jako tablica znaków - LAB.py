q='THE EYES'
print(q)
print(q[0],q[1],q[2],q[5],q[3],q[7],q[4],q[6])
print(q.lower()+' a gentelman')
print((q)+'a gentelman')
qa=(q)+'a gentelman'

print(qa[3],qa[6],qa[7],qa[2],qa[0],qa[4],qa[5],qa[1],qa[8:])

line='Program "Kropka nad i" nadamy o: 22:00'
print(line)
print(line.find(':'))
time=(line[33:])
print(time)
tmp=(line[line.find('"'):])
print(tmp)
print(tmp.find('i'))
title=(tmp[0:14])
print(title)
print(title, time)

line='Program "Pytanie na śniadanie" nadamy o: 6:00'
print(line)
time=line[line.find(':')+2:]
print(time)
tmp=line[line.find('"')+1:]
print(tmp)
title=tmp[:tmp.find('"')]
print(title)
print(time,title)



