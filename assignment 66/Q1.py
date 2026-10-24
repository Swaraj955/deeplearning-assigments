import math
x1 = 2
x2 = 3
w1 = 0.4
w2 = 0.6

bias = 0.5
weighted_sum = (x1 * w1) + (x2 * w2) + bias

output = 1 / (1 + math.exp(-weighted_sum))

print("Weighted Sum is =", weighted_sum)
print("Final Output is =", output)

if output >= 0.5:
    print("Output is close to 1")
else:
    print("Output is close to 0")
