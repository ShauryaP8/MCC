# Open the file for reading. Replace 'input.txt' with your actual file name.
with open('input.txt', 'r') as file:
    # Read the first line and extract N and K.
    N, K = map(int, file.readline().split())
    # Read the second line and extract the card values.
    cards = sorted(set(map(int, file.readline().split())))  # Sort the non-wild cards and remove duplicates.

# Initialize the variable for the longest run.
longest_run = 0

# Iterate through the cards to use each card as a possible starting point for a run.
for i in range(len(cards)):
    # Use wild cards to extend the run if needed.
    wilds_remaining = K
    run_length = 1
    last_card = cards[i]

    # Check subsequent cards to see if they continue the run.
    for j in range(i + 1, len(cards)):
        gap = cards[j] - last_card - 1

        # If the gap is less than or equal to the remaining wild cards, use them.
        if gap <= wilds_remaining:
            run_length += gap + 1  # Add the gap and the current card to the run length.
            wilds_remaining -= gap  # Decrease the wild cards count by the gap used.
            last_card = cards[j]    # Update the last card in the run.
        else:
            # No more wild cards to fill the gap, break the loop.
            break

    # Add any remaining wild cards at the end of the run.
    run_length += wilds_remaining

    # Update the longest run if the current run is longer.
    longest_run = max(longest_run, run_length)

# Output the length of the longest run.
print(longest_run)
