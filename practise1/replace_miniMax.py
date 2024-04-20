
n = int(input())
arr = list(map(int,input().split()))
mn = min(arr)
mx = max(arr)

min_index = arr.index(mn)
max_index = arr.index(mx)


arr[min_index], arr[max_index] = arr[max_index], arr[min_index]

for num in arr:
    print(num,end=" ")

# accepted


