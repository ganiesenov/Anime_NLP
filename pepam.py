def func(arr: list):
    arr_ = arr.reverse()
    return arr_

a = [1, 0]

a.append(func(a))
print(a[-1])
# if a[-1]:
#     print(a[0])
# else:
#     print(a[1])