"""
Leetcode 77: Combinations https://leetcode.com/problems/combinations/.

Given two integers n and k, return all possible combinations of k numbers
chosen from the range [1, n].

You may return the answer in any order.
"""


def combine(n: int, k: int) -> list[list[int]]:
    """Calculate the probability requested by the problem given input n.

    Args:
        n (int): The upper bound of the range to choose from.
        k (int): The quantity of numbers to choose from [1, n].
    Returns:
        All possible combinations of k numbers chosen from the range [1, n].
    """

    if k == 1:  # k = 1; just return all [1, n] individually wrapped.
        return [[i] for i in range(1, n + 1)]  # List comprehensions are fun :)

    sub_list = [*range(1, k + 1)]  # Initial list
    out_list = [[*range(1, k + 1)]]

    # Expand the initial list
    pos = -1 # pos is the position in the sublist we're working on expanding
    max_pos = -k # the limit (first item of sub_list represented as negative index)

    while(pos > max_pos):
        while (sub_list[-1] < n): # Last item in the list isn't at n yet
            sub_list[-1] += 1 # Increment it
            out_list.append([*sub_list]) # List slicing has the effect of deepcopy here, but is much faster.

        pos -= 1 # Backtrack to the previous item in the list
        if (sub_list[pos] < (n + pos + 1)): # Check if it's at its maximum
            # (The maximum is based on its position in the list)
            sub_list[pos] += 1 # If yes, increment it
            for i in range(pos + 1, 0): # Reset rest of list accordingly
                sub_list[i] = sub_list[pos] + i - pos
            out_list.append([*sub_list])
            pos = -1 # Reset position back to last item
    return out_list


# Test cases
print("combine(4, 2):", combine(4, 2))
print("combine(1, 1):", combine(1, 1))
print("combine(2, 1):", combine(2, 1))
print("combine(2, 2):", combine(2, 2))
print("combine(4, 3):", combine(4, 3))
print("combine(6, 5):", combine(6, 5))
print("combine(6, 3):", combine(6, 3))
print("combine(7, 4):", combine(7, 4))
print("combine(10, 7):", combine(10, 7))