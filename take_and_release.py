"""
A implementation considering the possibility to take an object and also
return it later if another one more valuable is found.
"""


def take_and_release_knapsack(W, wt, val, n):
    items_taken = []  # index to the items taken

    for i in range(n + 1):
        if wt[i - 1] <= W:  # if there is enough space yet, take the object
            W -= wt[i - 1]
            items_taken.append(i)
            continue

        for t in range(len(items_taken)):
            # If new item found is more valuable and has the same weight
            # Take it
            if wt[i - 1] <= wt[t - 1] and val[i - 1] > val[t - 1]:
                items_taken.pop(t)
                items_taken.append(i)
                break

    return sum([val[i] for i in items_taken])
