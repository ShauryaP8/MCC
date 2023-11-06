def apply_collatz(ai):
    if ai % 2 == 0:
        return ai // 2
    else:
        return 3 * ai + 1

n, k = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(k):
    new_a = [apply_collatz(ai) for ai in a]
    a = new_a

total_sum = sum(a)
print(total_sum)
