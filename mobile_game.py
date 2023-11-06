def min_enemies_to_kill(T, test_cases):
    results = []

    for case in range(T):
        N, A, B = test_cases[case][0]
        # Sort the enemies by their power levels in descending order.
        enemies = sorted(test_cases[case][1], reverse=True)
        kills = 0

        while A < B and enemies:
            for i, enemy_power in enumerate(enemies):
                if A > enemy_power:
                    A += enemy_power
                    kills += 1
                    enemies.pop(i)
                    break
            else:
                kills = -1
                break

        results.append(kills if A >= B else -1)

    return results

def read_test_cases(filename):
    test_cases = []
    with open(filename, 'r') as file:
        T = int(file.readline().strip())
        for _ in range(T):
            N, A, B = map(int, file.readline().strip().split())
            enemy_powers = list(map(int, file.readline().strip().split()))
            test_cases.append(((N, A, B), enemy_powers))
    return T, test_cases

# Read test cases from the file
T, test_cases = read_test_cases('input.txt')

# Get the Output
output = min_enemies_to_kill(T, test_cases)

# Print the output
for result in output:
    print(result)
