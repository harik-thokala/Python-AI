print("Hello world!")

print("this is a test")

temp =18

if temp > 30:
    print("its hot outside")
elif temp > 20:
    print("its nice outside")
else:    
    print("its cold outside")   


age = 18
has_license = False

if age >= 18 and not has_license:
    print("you can drive")
else:    print("you cannot drive")  

if age >= 18 or has_license:
    print("you can drive")
else:    print("you cannot drive")  

age = 19
has_ticket = True   
if not has_ticket:
    if age >= 18:
        print("you can enter the concert")
    else:
        print("you cannot enter the concert")
else:
    print("please buy a ticket to enter the concert")

# loops
for i in range(5):
    print("hello", i+1)

for i in range(1, 11,2):
    print("Hari",i)
