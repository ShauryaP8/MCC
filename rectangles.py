def min_area_of_blue_rectangles(N, K, rectangles):
    # Initialize DP array with infinity since we want to minimize
    dp = [[float('inf')] * (K + 1) for _ in range(N + 1)]
    # Base case: 0 rectangles with 0 blue rectangles has 0 area
    dp[0][0] = 0

    # Start filling the DP array
    for i in range(1, N + 1):
        for k in range(1, K + 1):
            # Initialize width and height for the current grouping
            width_sum = 0
            max_height = 0
            for j in range(i, 0, -1):
                # Update the width and max height
                width_sum += rectangles[j-1][1]
                max_height = max(max_height, rectangles[j-1][0])
                # Check if we can extend the previous rectangle group or start a new one
                if k > 1:
                    dp[i][k] = min(dp[i][k], dp[j-1][k-1] + width_sum * max_height)
                else:  # When k == 1, we can't start a new blue rectangle
                    dp[i][k] = width_sum * max_height
    return dp[N][K]

# Sample Input
# Sample Input for N=125, K=65
N, K = 125, 65
rectangles = [
    (613, 551), (22, 791), (242, 269), (718, 598), (35, 676), (151, 998), (347, 920), (512, 113),
    (846, 674), (720, 46), (385, 183), (449, 335), (785, 883), (774, 140), (941, 387), (857, 584),
    (784, 987), (610, 705), (365, 96), (507, 122), (475, 560), (776, 568), (673, 493), (472, 996),
    (562, 176), (113, 985), (466, 334), (906, 698), (507, 20), (12, 671), (206, 942), (939, 926),
    (721, 755), (255, 388), (504, 463), (869, 718), (690, 811), (481, 929), (253, 949), (880, 400),
    (237, 937), (805, 604), (749, 234), (319, 882), (120, 551), (275, 867), (594, 353), (889, 513),
    (988, 39), (492, 522), (598, 281), (571, 175), (835, 958), (1000, 618), (425, 923), (90, 796),
    (427, 114), (603, 693), (133, 746), (960, 607), (566, 918), (522, 912), (60, 518), (473, 271),
    (619, 290), (872, 786), (879, 913), (345, 884), (659, 125), (369, 433), (554, 959), (454, 100),
    (902, 968), (159, 245), (719, 511), (823, 356), (209, 657), (575, 205), (353, 686), (299, 179),
    (428, 376), (562, 469), (337, 828), (154, 930), (493, 808), (724, 825), (493, 508), (964, 379),
    (952, 870), (68, 806), (207, 435), (213, 617), (20, 259), (513, 306), (280, 234), (228, 444),
    (739, 607), (428, 203), (959, 958), (42, 240), (184, 675), (371, 537), (956, 998), (342, 133),
    (11, 483), (886, 313), (903, 183), (214, 230), (570, 17), (583, 281), (48, 32), (307, 583),
    (225, 44), (622, 739), (709, 94), (204, 499), (786, 477), (412, 330), (280, 707), (964, 38),
    (435, 1000), (418, 598), (4, 493), (438, 859), (210, 109)
]

# Compute and print the minimum area of blue rectangles needed
print(min_area_of_blue_rectangles(N, K, rectangles))
