def check_greater(a, b, c, d):
    if a > b and c > d:
        return "True"
    else:
        return "False"

print(check_greater(5, 3, 4, 2))
print(5 > 3 and 4 > 2)
print(check_greater(5, 4, 4, 6))
print(5 > 4 and 4 > 6)

print(5 > 6 and 1/0 > 3)
# print(check_greater(5, 6, 1/0, 3))

def sum_four_times(a):
    return a + a + a + a

print(sum_four_times(5 ** 6))