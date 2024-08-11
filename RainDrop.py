a=int(input())
if a%3==0 and a%5==0 and a%7==0:
    print("PlingPlangPlong")
elif a%3==0 and a%5==0:
    print("PlingPlang")
elif a%3==0 and a%7==0:
    print("PlingPlong")
elif a%3==0:
    print("Pling")
elif a%5==0:
    print("Plang")
elif a%7==0:
    print("Plong")
else:
    print(a)