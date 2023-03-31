# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import math

# Define fixed-point parameters
NUMBER_BITS = 16
FRACTIONAL_BITS = 8
FIXED_POINT_SCALE = (2**(NUMBER_BITS - FRACTIONAL_BITS)) / NUMBER_BITS

# Define some sample fixed-point numbers
a = 10.5
b = 3.25

# Convert the numbers to fixed-point
a_fixed = int(a * FIXED_POINT_SCALE)
b_fixed = int(b * FIXED_POINT_SCALE)

print(a_fixed)

# Perform some arithmetic operations on the fixed-point numbers
c_fixed = a_fixed + b_fixed
d_fixed = a_fixed - b_fixed
e_fixed = a_fixed * b_fixed
f_fixed = int(a_fixed / b_fixed)

# Convert the results back to floating-point
c = c_fixed / FIXED_POINT_SCALE
d = d_fixed / FIXED_POINT_SCALE
e = e_fixed / (FIXED_POINT_SCALE ** 2)
f = f_fixed / FIXED_POINT_SCALE

# Print the results
print("a =", a)
print("b =", b)
print("c = a + b =", c)
print("d = a - b =", d)
print("e = a * b =", e)
print("f = a / b =", f)
