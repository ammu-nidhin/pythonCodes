list1=[12,24,35,70,88,120,155]
newlist=[ele for ele in list1 if list1.index(ele)!=0 and list1.index(ele)!=4 and list1.index(ele)!=5]
print(newlist)
