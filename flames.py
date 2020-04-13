#!/usr/bin/python3

standard_input = ["Harishkumar", "Soomerandomxyz"]

name1 = input('Enter your name       : ')
name2 = input('Enter your crush name : ')

list1 = list(name1.upper())
list2 = list(name2.upper())

test1 = list1.copy()
test2 = list2.copy()

for i in list1:
    if i in test2:
        test1.remove(i)
        test2.remove(i)

count = len(test1) + len(test2)

flames = ['F', 'L', 'A', 'M', 'E', 'S']

length = len(flames)-1

for _ in range(length):

    index = count % len(flames)
    del flames[index-1]
    print(flames)


# if count % 2 == 0:
#     del flames[1]
# else:
#    del flames[1]

if flames[0] == 'F':
    print('You both are friends')

elif flames[0] == 'F':
    print('You both are friends')

elif flames[0] == 'L':
    print('You both are lovers')

elif flames[0] == 'A':
    print('She is having a crush on you')

elif flames[0] == 'E':
    print('You both are Enemies')

elif flames[0] == 'M':
    print('You both are going to get married')

elif flames[0] == 'S':
    print('Sorry bro, she is your sister ')
