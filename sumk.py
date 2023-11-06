MOD = 998244353

def fast_exp(base, exp, mod):
    res = 1
    while exp:
        if exp & 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return res

def sum_of_powers(N, K, arr):
    # Sort the array to optimize the power calculations
    arr.sort(reverse=True)
    total = 0
    prefix = 0

    # Calculate the contribution of each element
    for i, a in enumerate(arr):
        prefix = (prefix + a) % MOD
        # This is where we use the Exponentiation by Squaring technique
        total += prefix * fast_exp(2, N - i - 1, MOD)
        total %= MOD

    # If K is 1, the above total is already correct
    # If K > 1, we adjust the calculation to account for the exponent K
    if K > 1:
        new_total = 0
        for a in arr:
            total = (total - fast_exp(a, K, MOD) + MOD) % MOD
            new_total += total
            new_total %= MOD
        return new_total
    else:
        return total

# Reading input from 'input.txt'
with open('input.txt', 'r') as file:
    N, K = map(int, file.readline().strip().split())
    arr = list(map(int, file.readline().strip().split()))

# Output the result
print(sum_of_powers(N, K, arr))
