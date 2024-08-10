a=float(input())
if a<150:
    print("Person is Dwarf.")
elif a>150 and a<=165:
    print("Person is average heighted.")
elif a>165 and a<=195:
    print("Person is taller.")
else:
    print("Abnormal height.")