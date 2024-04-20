def sum_digits(n,a):
    sum = 0
    for d in a:

        sum += int(d)
    print(sum)


n = int(input())

a = input()

sum_digits(n,a)
