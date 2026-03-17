#we just and it with a number with leading 1s ending with a single 0 (anding it with 0 just turns everything to 0)
x=int(input("enter number"))
x=int(x&~1)
print(x)
