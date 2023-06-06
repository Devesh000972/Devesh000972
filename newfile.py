import time
#a = int(time.strftime('%H'))
a = int (input ('Enter the hour: '))
print (a)

if (a>0 and a<12):
    print ("Good MorningSir")
elif (a>=12 and  a<18 ):
    print ("Good Afternoon Sir")
    
elif (a>=18 and a==24):
    print ("Good Night Sir")
    
else:
    print ("")
