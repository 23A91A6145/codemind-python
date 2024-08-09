a=int(input())
b=a//3600
c=(a%3600)//60
d=(a%60)
print('H:M:S-{}:{}:{}'.format(b,c,d))