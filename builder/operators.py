from builder.base import generate_operator

def _random():
    return generate_operator(233, 'Random', 'operator')


def _x_pos():
    return generate_operator(234, 'X Pos', 'operator')


def _y_pos():
    return generate_operator(235, 'Y Pos', 'operator')


def _random110():
    return generate_operator(236, 'Random110', 'operator')


def _random1100():
    return generate_operator(237, 'Random1100', 'operator')


def _random11000():
    return generate_operator(238, 'Random11000', 'operator')


def _variable():
    return generate_operator(239, 'Variable', 'operator')


# Conditional Operators
def condition_equals(val1, val2):
    return generate_operator(1000, '=', 'conditionalOperator', [val1, val2])


def condition_not_equals(val1, val2):
    return generate_operator(1001, '≠', 'conditionalOperator', [val1, val2])


def condition_less_than(val1, val2):
    return generate_operator(1002, '<', 'conditionalOperator', [val1, val2])


def condition_greater_than(val1, val2):
    return generate_operator(1003, '>', 'conditionalOperator', [val1, val2])


def condition_and(cond1, cond2):
    return generate_operator(1004, 'and', 'conditionalOperator', [cond1, cond2])


def condition_or(cond1, cond2):
    return generate_operator(1005, 'or', 'conditionalOperator', [cond1, cond2])


def condition_greater_than_or_equal_to(val1, val2):
    return generate_operator(1006, '>=', 'conditionalOperator', [val1, val2])


def condition_less_than_or_equal_to(val1, val2):
    return generate_operator(1007, '<=', 'conditionalOperator', [val1, val2])


def condition_matches(text, expression):
    return generate_operator(1008, 'matches', 'conditionalOperator', [text, expression])


def condition_not(condition):
    return generate_operator(1009, 'not', 'conditionalOperator', [condition])


def condition_is_flipped():
    return generate_operator(1010, 'flipped', 'conditionalOperator')


# Math Operators
def math_add(val1, val2):
    return generate_operator(4000, 'Math Operator Add', 'operator', [val1, val2])


def math_subtract(val1, val2):
    return generate_operator(4001, 'Math Operator Subtract', 'operator', [val1, val2])


def math_multiply(val1, val2):
    return generate_operator(4002, 'Math Operator Multiply', 'operator', [val1, val2])


def math_divide(val1, val2):
    return generate_operator(4003, 'Math Operator Divide', 'operator', [val1, val2])


def math_random(low, high):
    return generate_operator(4004, 'Math Operator Random', 'operator', [low, high])


def math_power(val1, val2):
    return generate_operator(4005, 'Math Operator Power', 'operator', [val1, val2])


def math_square_root(value):
    return generate_operator(4006, 'Math Operator Square Root', 'operator', [value])


def math_sine(value):
    return generate_operator(4007, 'Math Operator Sine', 'operator', [value])


def math_cosine(value):
    return generate_operator(4008, 'Math Operator Cosine', 'operator', [value])


def math_round(value):
    return generate_operator(4009, 'Math Operator Round', 'operator', [value])


def math_abs(value):
    return generate_operator(4010, 'Math Operator Abs', 'operator', [value])


def math_modulo(val1, val2):
    return generate_operator(4011, 'Math Operator Modulo', 'operator', [val1, val2])


def math_tangent(value):
    return generate_operator(4012, 'Math Operator Tangent', 'operator', [value])


def math_inverse_sine(value):
    return generate_operator(4013, 'Math Operator Inverse Sine', 'operator', [value])


def math_inverse_cosine(value):
    return generate_operator(4014, 'Math Operator Inverse Cosine', 'operator', [value])


def math_inverse_tangent(value):
    return generate_operator(4015, 'Math Operator Inverse Tangent', 'operator', [value])


def math_maximum(val1, val2):
    return generate_operator(4016, 'Math Operator Maximum', 'operator', [val1, val2])


def math_minimum(val1, val2):
    return generate_operator(4017, 'Math Operator Minimum', 'operator', [val1, val2])


def math_floor(value):
    return generate_operator(4018, 'Math Operator Floor', 'operator', [value])


def math_ceiling(value):
    return generate_operator(4019, 'Math Operator Ceiling', 'operator', [value])


# Color Operators
def color_operator_random(value):
    return generate_operator(5000, 'Color Operator Random', 'operator', [value])


def color_operator_rgb(value):
    return generate_operator(5001, 'Color Operator RGB', 'operator', [value])


def color_operator_hsb(value):
    return generate_operator(5002, 'Color Operator HSB', 'operator', [value])


def hs_object(value):
    return generate_operator(8000, 'Object', 'operator', [value])


def any_object(value):
    return generate_operator(8001, 'Any Object', 'operator', [value])


def screen_edge(value):
    return generate_operator(8002, 'Screen Edge', 'operator', [value])


def game(value):
    return generate_operator(8003, 'Game', 'operator', [value])


def self(value):
    return generate_operator(8004, 'Self', 'operator', [value])


def original_object(value):
    return generate_operator(8005, 'Original Object', 'operator', [value])


def local(value):
    return generate_operator(8006, 'Local', 'operator', [value])


def user(value):
    return generate_operator(8007, 'User', 'operator', [value])


def product(value):
    return generate_operator(8008, 'Product', 'operator', [value])


def scoped(value):
    return generate_operator(8009, 'Scoped', 'operator', [value])


def text_operator_char_at_index(value):
    return generate_operator(9000, 'Text Operator Char At Index', 'operator', [value])


def text_operator_chars_in_range(value):
    return generate_operator(9001, 'Text Operator Chars In Range', 'operator', [value])


def text_operator_length(value):
    return generate_operator(9002, 'Text Operator Length', 'operator', [value])


def text_operator_join(value):
    return generate_operator(9003, 'Text Operator Join', 'operator', [value])


def scene_reference_block(value):
    return generate_operator(10000, 'Scene Reference Block', 'operator', [value])


def previous_scene_parameter(value):
    return generate_operator(10001, 'Previous Scene Parameter', 'operator', [value])


def next_scene_parameter(value):
    return generate_operator(10002, 'Next Scene Parameter', 'operator', [value])

