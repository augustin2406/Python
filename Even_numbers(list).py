new_list = []
num = int(input("Enter number of elements: "))

for i in range(num):
    element = int(input("Enter element: "))
    new_list.append(element)

even_list = []
for i in new_list:
    if i % 2 == 0:
        even_list.append(i)
print("original list=",new_list)
print("Even numbers in the list:", even_list)
