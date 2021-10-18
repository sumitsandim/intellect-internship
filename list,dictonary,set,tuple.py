#list 
list_1=["sumit",23,"manish"]
print(list_1)
print(type(list_1))
#operations on list
#length
list_1=["sumit",23,"manish"]
print(len(list_1))
#acessing of element
list_1=["sumit",23,"manish"]
#$positive index
print(list_1[2])
#negative index 
print(list_1[-2])
#access inside range
print(list_1[1:3])
#MEMBERSHIP 
print(23 in list_1)
print(23 not in list_1)
#changing item value 
list_1[2]=46
print(list_1)
list_1[1]="manish"
print(list_1) 
list_1[0:2]= "manish","sumit"
print(list_1)
#insert
list_1.insert(3,55)
print(list_1)
#append 
list_1.append("dj")
print(list_1)
#remove
list_1.remove(55)
print(list_1)
#pop
list_1.pop(3)
print(list_1)
#######################################################################
#Tuple
t1=("sumit",46,"manish")
#update tuple 
L1=list(t1)
L1[2]="rahul"
t1=tuple(L1)
print(t1)
#length
print(len(t1))
#accessing element
# +
print(t1[2])
#  -
print(t1[-3])
#acess inside the range 
print(t1[0:2])
#membership
print(55 in t1)
print(46 in t1)
#changing item value
t1=('sumit', 46, 'rahul')
L1=list(t1)
L1.insert(0,"dj")
t1=tuple(L1)
print(t1)
#append
L1=list(t1)
L1.append("manish")
t1=tuple(L1)
print(t1)
#pop
print(t1)
L1=list(t1)
L1.pop(1)
t1=tuple(L1)
print(t1)
L1=list(t1)
L1.remove("dj")
t1=tuple(L1)
print(L1)
###################################
#set 
s1={"sumit","manish",76}
for x in s1 :
    print(x)
print(s1)
#add
s1.add("rahul")
print(s1)
#remove()
s1.remove(76)
print(s1)
#update()
L2=list(s1)
L2[0]="dj"
s1=set(L2)
print(s1)
#dictonary
dict1={'name':'sumit','number':8765432155,'village':'mahad'}
print(dict1)

print(dict1['number'])
#get()
print(dict1.get('village'))
#get keys 
print(dict1.keys())
dict1['village']='ratnagiri'
print(dict1)
#update
dict1.update({'name':'rahul'})
print(dict1)
#remove()
dict1.pop('number')
print(dict1)
#del()
#del()
del dict1['name']
print(dict1)




