**Exercise number 5**
#Create empty lists
ls = list();
lp = list();

for m in range(1000):

    a=str(m)
    if len(a)==1:
          ls.append(m)
          lp.append(m)
    else:
        l=list(a)
        #print l
        #Convert sting type characters in int type
        l = [int(i) for i in l]
        sum=0
        prod=1
        a1=len(a)
        for k in range(a1):
            sum+=l[k]
            prod*=l[k]
            #print type(sum)
            #print sum, prod
        if (m % sum)==0:
             ls.append(m)
        if prod!=0:
            if (m % prod)==0:
                lp.append(m)

print "Harshad numbers"
print ls
print " "
print "Numbers which divided by the product of their digits"
print lp
print " "
