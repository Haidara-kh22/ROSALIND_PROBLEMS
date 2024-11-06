def total_rabbit_pairs(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return total_rabbit_pairs(n-1, k) + k * total_rabbit_pairs(n-2, k)


n = int(input())

k = int(input()) 
print(total_rabbit_pairs(n, k))
