import sys
numbers_counter=int(input())
counter=0
max_number= - sys.maxsize
#The value sys.maxsize, on the other hand, reports the platform's pointer size, 
#and that limits the size of Python's data structures such as strings and lists.
while counter<numbers_counter:
    number=int(input())
    counter+=1
    if number>max_number:
        max_number=number

print(max_number)

