# def add(num1, num2):
#     return num1 + num2

# result1 = add(10,20)
# print(result1)

# def add(num1, num2, num3, num4):
#     return num1 + num2, num3 + num4

# result2 = add(10, 20, 30, 40)
# print(result2)


# nums = [5,2,7,3,1]
# nums.sort()
# nums.reverse()
# print(nums)

# name = "김준일"
# print(name.index("준"))


# print(nums.index(3))

# print(name.find("준"))



user = {
    "username": "testuser",
    "password": "1234",
    "name": "김준일",
    "email": "test@gmail.com"
}
print(user)
user.update({
    "phone": "010-1234-5678",
    "name": "김준이"
})
user["age"] = 31
print(user)