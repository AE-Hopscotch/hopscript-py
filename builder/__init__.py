from builder.stage import stage, HSObject, HSRule, self

from builder.blocks import *
from builder.operators import generate_operator, matches, NOT, square_root, sin, cos, tan, \
    asin, acos, atan, maximum, minimum, Color, char_at_index, chars_in_range, join, \
    math_round, math_floor, math_ceil

# Since our magic functions take care of floor and ceil, hoist them to global scope
# This will make it consistent with other HS operators
from math import floor, ceil

from builder.traits import *
from builder.variable import original, game, user, product, local
