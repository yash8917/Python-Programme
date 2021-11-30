l=[1,23,2344,4543,443]
l1=[]
n=int(input('Enter the  size :'))
for i in l:
    if len(str(i)) > n:
        l1.append(i)
print('Elements are more than the size =>',l1)
