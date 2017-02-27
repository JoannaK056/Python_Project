**Exersise number 4**
#Create an empty list
l = list();
#Fill the list with numbers
con=True
while con==True :
   numb=raw_input("Give a number , dear --->")
   print type(numb)
   if numb==" ":
       while numb==" ":
           numb=raw_input("Mistake!!! Give a number , I said! --->")
   else:
     l.append(numb)
   brk=raw_input("If you done giving numbers give <END>")
   brk=brk.upper()
   print brk
   if brk=="END":
       con=False
#Put the elements in order
l=sorted(l)
#Convert sting type characters in float type
l = [float(i) for i in l]
print l
#Calculate the m.o.
a=len(l)
print a
s=0
for i in range(a-2):
    if (i!=0) and (i!=1):
       s+=l[i]
       print s,i
print s
mo=s/(a-4)
print mo

#Calculate d^2
s1=0
for i in range(a-2):
    if (i!=0) and (i!=1):
       d=(l[i]-mo)**2
       s1+=d
       print d,i,s1

print s1

#Calculate d^2/n
tel_num = s1/(a-4)

import math
#Calculate tipiki apoklisi
typiki_apoklisi = math.sqrt(tel_num)
print typiki_apoklisi
