a=int(input())
b=a+a*0.80+a*0.20
c=a+a*0.90+a*0.25
d=a+a*0.95+a*0.30
if a<=10000:
    print('{:.2f}'.format(b))
elif a>10000 and a<=20000:
    print('{:.2f}'.format(c))
else:
     print('{:.2f}'.format(d))