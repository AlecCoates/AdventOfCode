joltages = []
with open("./input.txt", "r") as file:
    for line in file.read().strip().split('\n'):
        joltages.append(int(line))

def count_variations(arr, index):
    print(index)
    count = 0
    if index - 1 > 0 and arr[index - 1] <= arr[index] + 3:
        count += count_variations(arr, index - 1)
    if index - 2 > 0 and arr[index - 2] <= arr[index] + 3:
        count += count_variations(arr, index - 2)
    if index - 3 > 0 and arr[index - 3] <= arr[index] + 3:
        count += count_variations(arr, index - 3)
    return count

joltages.append(max(joltages) + 3)
joltages.append(0)
joltages.sort(reverse=True)
counts = [1]
for i in range(1, len(joltages)):
    count = 0
    if i - 1 >= 0 and joltages[i - 1] <= joltages[i] + 3:
        count += counts[i - 1]
    if i - 2 >= 0 and joltages[i - 2] <= joltages[i] + 3:
        count += counts[i - 2]
    if i - 3 >= 0 and joltages[i - 3] <= joltages[i] + 3:
        count += counts[i - 3]
    print(i, joltages[i], count)
    counts.append(count)

print(counts[len(counts) - 1])
input('Done')