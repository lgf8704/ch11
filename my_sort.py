import random 


# 生成待排序数组
a = []
for i in range(100):
    a.append(random.randint(1, 1000))
N = len(a)

# 排序函数
def my_sort(a, left=0, right=N - 1):
    mid = N - 1
    temp = a[mid]
    for i in range(N):
        if a[i] > temp:
            a[i], a[mid] = a[mid], a[i]
    my_sort()




# 调用排序函数
my_sort(a)
print(a)
