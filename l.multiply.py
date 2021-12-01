l=[1,2,3,4,5,6,7,8,9]
# print('Enter the no. You Want to Multiply in the List :',end='')
# m=eval(input())
# for i in l:
#     m*=i
# print('''After Multipil's a no. List Will Be a = ''',format(m,'.2f'))
def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list(l))