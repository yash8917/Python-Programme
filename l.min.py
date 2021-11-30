# l=[12,34,546,4,456]
# min=l[0]
# for i in l:
#     if i<min:
#         min=i
# print(min)

l=[2232,'yash','huraah',121]
a=0
for i in l:
    if len(i) > 1 and i[0] == i[-1]:
        a+=1
    print(a)
