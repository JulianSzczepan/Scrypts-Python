s='A Python script'
print(s)
print(s[0])
print(s[4])
print(s[3:7])
print(s[2:8])
print(s[8])
print(s[8:])
print(s[0]+' '+s[9])
'''

'''
message = 'Document "cv.doc" was printed on pronter: XEROX'
print(message)
print(message[9:17])
print(message.index('X'))
print(message.count('X'))
print(message[message.find(':')+2:])
print(message[message.find('"')+1:])
tmp=(message[message.find('"')+1:])
print(tmp[:tmp.find('"')])
