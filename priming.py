#!/usr/bin/env python

import sys

# 4   g/L  : mild carbonation, British ales
# 5-7 g/L  : lager, other ales
# 8   g/L  : weizen (fizzy!)

grams_per_litre = 6
try:
    amount = float(sys.argv[1])
    bottle_size = float(sys.argv[2])
    if len(sys.argv) > 3:
        grams_per_litre = float(sys.argv[3])
except:
    print("Usage: %s litres bottle-size [grams-per-litre: 6]" % sys.argv[0])
    exit(1)

grams_sugar = amount * grams_per_litre # [L]*[g/L] = [g]
solution_volume = grams_sugar * 1.64 # [g]*[mL/g] = [mL]
solution_per_bottle = solution_volume * bottle_size / amount # [mL]*[L]/[L] = [mL]
print(
"""
Solve %g g of sugar in %g mL of water.
Add %g mL of sugar solution to each %g L bottle.
""" % (grams_sugar, grams_sugar, solution_per_bottle, bottle_size)
)

