i = open("input.txt", "r")
o = open("output.txt", "w")
for line in i:
    nums = line.split(",")
    s = 0
    for num in nums:
        s += int(num)
    o.write(f"{s}\n")
i.close()
o.close()