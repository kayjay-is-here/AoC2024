with open("inputs/day1.txt", "r") as f:
    lines = f.read().splitlines()

left = []
right = []

for line in lines:
    l, r = line.split("   ")
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()


def count_occurrences(sorted_list, value):
    from bisect import bisect_left, bisect_right
    left_idx = bisect_left(sorted_list, value)
    right_idx = bisect_right(sorted_list, value)
    return right_idx - left_idx


result_sum = 0
for i in range(len(left)):
    count = count_occurrences(right, left[i])
    result_sum += left[i] * count

print(result_sum)
f.close()

# I lost the part A solution but it shouldn't matter its an idiot test anyway