number = 10
print(type(number))

print(id(10)) #id() 주소값
print(id(number))
number += 1
print(id(number))
number -= 1
print(id(number))

print(type("test"))
print(type([]))
print(type(()))
print(type([]))

print([1,2,3,4])
print((1,2,3,4))
print({"id":1, "name":"김준일"})

list = [1,2,3,4]
tp = (5,6,7,8)
dict1 = {"id": 1, "name": "김준일"}

print(list[0])
print(tp[0])
print(dict["id"])

list.append(5)
print(list)
print(tp.index(7))
list2 = list(tp)
print(list2)
print(dict1.keys())
print(dict1.values())
print(list(dict1.items())[0])

print(True)
print(False)