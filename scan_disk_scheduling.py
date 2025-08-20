requests = list(map(int, input("Enter request sequence: ").split()))
head = int(input("Enter head position: "))
direction = input("Enter direction (left/right): ")
disk_size = int(input("Enter disk size: "))

requests.sort()
seek_count = 0
sequence = []

if direction == "left":
    left = [r for r in requests if r <= head]
    right = [r for r in requests if r > head]
    left.append(0)
    left.sort(reverse=True)
    right.sort()
    order = left + right
else:
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]
    right.append(disk_size-1)
    right.sort()
    left.sort(reverse=True)
    order = right + left

for r in order:
    seek_count += abs(head - r)
    head = r
    sequence.append(r)

print("Seek Sequence:", sequence)
print("Total Seek Operations:", seek_count)
