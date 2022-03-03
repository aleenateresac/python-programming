list=[1,2,3]
list.insert(0,100)
list.insert(3,200)
list.insert(4,300)
res=[list for list in list if list > 100]

print(res)
