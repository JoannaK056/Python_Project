# Python_Project
""" Program which removes all the exclamation marks except the one which 
is located in the end of the sentence. *Exersise number 1* """

sent=raw_input("give a sentence, dear --->")

#print sent
#calculate the lenght of the string
a=len(sent)
#print a
#transform string into lists
l=list(sent)
l1=list(sent)

for i in range(a-1):
	#print i
	if sent[i]=="!":
			l[i]=" "
			#print l

d=0
#Create an empty list
l2 = list();
for k in range(a):
	if l[k]==l1[k]:
		#put element into the list
		l2.insert( d, l[k])
		d=d+1
		#print l2

#join method of the empty string to join all of the strings together 
b=''.join(l2)
print b

