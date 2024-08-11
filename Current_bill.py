a=int(input())
if a<=199:
    c=a*1.20
elif a>=200 and a<400:
    c=a*1.50
elif a>=400 and a<600:
    c=a*1.80
else:
    c=a*2.0
if c>400:
    print('{:.2f}'.format(c+c*0.15))
else:
    print('{:.2f}'.format(c+100))