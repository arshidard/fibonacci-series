# fibonacci series up to 10 numbers
# 0,1,1,2,3,5,8.....
# list1=[0,1]
# hi=int(input("up to which term of fibanocci series"))
# for b in range(0,hi-2):
#     a=list1[-1]+list1[-2]
#     list1.append(a)
# print(list1)
# for i in list1:
#     print(i,end=" ")


# list2=list("mohanlal")
# print(list2)
# name2="".join(list2)
# print(name2)

#print a input word or sentence with a space after 4 consecutive characters
# hi=input("enter a word or a sentence")
# list1=list(hi)
# print(list1)
# empty=[]
# for i in range(0,len(list1)):
#     if i%4==0 and i!=0:
#         empty.append(" ")
#         empty.append(list1[i])
#     else:
#         empty.append(list1[i])
# print(empty)
# newstr="".join(empty)
# print(newstr)

#create a list of numbers from 1 to 20

empty=[]
for i in range(1,21):
    empty.append(i)
print(empty)
#create a new list from the above list which carries only even numbers
empty2=[]
for i in empty:
    if i%2==0:
        empty2.append(i)
print(empty2)
