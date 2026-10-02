#========================================================================================================
# HYPOTENUSE CALCULATOR
# NAME: Miesha Denise C. Macazo
# SECTION: 8-SAMPAGUITA
# DESCRIPTION: Calculates the hypotenuse of a right triangle using the Pythagorean theorem and Python's math library.
#========================================================================================================

import math

print("=== Right Triangle Hypotenuse Calculator ===")

# Get the two shorter sides (legs) of the triangle
side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))

# SOLVING: Pythagorean theorem: c = sqrt(a^2 + b^2)
hypotenuse = math.sqrt(side_a ** 2 + side_b ** 2)

print(f"\nThe hypotenuse is {hypotenuse:.2f}")
