# up, down, right, left
# out: 4
# N, E
# DFS -> O(N+E) -> func call stack
# BFS -> O(N+E)


def get_longest_path(y_coord, x_coord, nums, max_path=0):
    max_y = len(nums)
    max_x = len(nums[0])
    if y_coord > 0:
        if nums[y_coord, x_coord] > nums[y_coord - 1, x_coord]:
            max_path = max(max_path, 1 + get_longest_path(y_coord - 1, x_coord, nums))
        else:
            return 1
    if y_coord < max_y - 1:
        max_path = max(max_path, 1 + get_longest_path(y_coord + 1, x_coord, nums))
        # Look left
    if x_coord > 0:
        max_path = max(max_path, 1 + get_longest_path(y_coord, x_coord - 1, nums))
        # Look left
    if x_coord < max_x - 1:
        max_path = max(max_path, 1 + get_longest_path(y_coord, x_coord + 1, nums))
    if max_path == 0:
        return 1


max_paths = []

nums = [
    [3, 2, 1],
    [6, 5, -1]
]

for y_coord, row in enumerate(nums):
    for x_coord, val in enumerate(row):
        max_paths.append(get_longest_path(y_coord, x_coord, nums))

# print(max(max_paths))
