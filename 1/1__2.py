
input_ = []
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        input_.append(int(line))

increased_count = 0
for index, number in enumerate(input_):
    if index == 0 or len(input_) - index < 3:
        # skip first one and last three
        continue
    if input_[index] + input_[index+1] + input_[index+2] > input_[index-1] + input_[index] + input_[index+1]:
        increased_count += 1

print(increased_count)

