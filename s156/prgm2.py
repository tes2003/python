list1 = [1,-2,3,-4,5,6,-7,8,-9,10]
print("list1",list1)
print("postive numbers:")
for num in list1:
    if num >= 0:
        print(num)
list2 = [1,2,3,4,5,34,6,78,4,8]
print("list2",list2)
print("square of list:")
for n in list2:
   print(n**2)
v = ['a','e','i','o','u']
word = input("enter the word:")
s = [i for i in word if i in v]
print(s)
word = input("enter the word:")
j = [ord(x) for x in word]
print(j)