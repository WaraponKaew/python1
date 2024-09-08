x=int(input("input first value: "))
print(x)
y=int(input("input second value: "))
print(y)
print("choose + - * / ")
z=input("input: ")
print(z)
if z == "+":
    total = x+y
elif z=="-":
    total = x-y
elif z=="*":
    total = x*y
else:
    total = x/y
print(total) 
