 #Lists

my_list = [1, 2, 3, 4, 5]
print(my_list , my_list[-1])

my_list1 = ["apple", "banana", "cherry"]

mylist2 = [1, "hello", 3.14, True]

mylist3 = my_list1 + mylist2
print(mylist3)

print(len(mylist3))

mylist3.pop(4)
print(mylist3)

mylist3.reverse()
print(mylist3)

age = 20

mylist3.append(age)
print(mylist3)

for item in mylist3:
    print(item)

for i in range(len(mylist3)):
    for j in range(i+1, len(mylist3)):
        if mylist3[i] == mylist3[j]:
            print("Duplicate found:", mylist3[i])
        elif mylist3[i] != mylist3[j]:
            print("No duplicate found:", mylist3[i], "and", mylist3[j])




# Using set to find duplicates
seen = set()
duplicates = set()

for item in mylist3:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

if duplicates:
    print(f"Duplicates found: {duplicates}")
else:
    print("No duplicates found")



    # Fixed duplicate finder with proper indentation
for i in range(len(mylist3)):
    for j in range(i+1, len(mylist3)):
        if mylist3[i] == mylist3[j]:
            print("Duplicate found:", mylist3[i])
        elif mylist3[i] != mylist3[j]:
            print("No duplicate found:", mylist3[i], "and", mylist3[j])

new_list = []
for i in range(len(mylist3)):
    if mylist3[i] not in new_list:
        new_list.append(mylist3[i])


print(new_list)