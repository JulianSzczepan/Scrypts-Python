name='Julian'
age=38
daysInYear=365
message= '%s is %d years old, so is about %d days old'
print(message %(name, age, age*daysInYear))
'''
#drugie rozwiązanie
'''
print(name,'is',age,'years old, so is about',age*daysInYear,'days old')

name = 'Chris'
age = 17
print(message % (name,age,age*daysInYear))
message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format(name,age,age*daysInYear))

print('1234567890 divided by 12345 is ',1234567890 // 12345,'and the rest is',1234567890 % 12345)
