
# n = int(input())

# tmp = n
# reverse = 0
# while n> 0:
#     digit = n % 10   
#     reverse = (reverse * 10) + digit
#     n = n // 10  

# print(reverse)
# if tmp == reverse:
#     print('YES')
# else:
#     print("NO")



# practise day 2
#  palindrome

n = int(input())
lst = list(map(int,input().split()))

sty = lst[::-1]
if lst == sty:
    print("YES")
else:
    print("NO")


# accepted
