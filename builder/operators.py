import abc
import json


class HSDatum(abc.ABC):
    """A data-holding object in Hopscotch code"""
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    # Conditional operators
    def __eq__(self, other) -> 'Operator': return condition_equals(self, other)
    def __ne__(self, other) -> 'Operator': return condition_not_equals(self, other)
    def __lt__(self, other) -> 'Operator': return condition_less_than(self, other)
    def __gt__(self, other) -> 'Operator': return condition_greater_than(self, other)
    def __le__(self, other) -> 'Operator': return condition_less_than_or_equal_to(self, other)
    def __ge__(self, other) -> 'Operator': return condition_greater_than_or_equal_to(self, other)

    def __and__(self, other) -> 'Operator':
        """Defines behavior for operand bitwise AND (i.e. Datum & 1)"""
        return condition_and(self, other)
    def __rand__(self, other) -> 'Operator':
        """Defines behavior for right-hand side operand bitwise AND (i.e. 1 & Datum)"""
        return condition_and(other, self)
    def __or__(self, other) -> 'Operator':
        """Defines behavior for operand bitwise OR (i.e. Datum & 1)"""
        return condition_or(self, other)
    def __ror__(self, other) -> 'Operator':
        """Defines behavior for right-hand side operand bitwise OR (i.e. 1 & Datum)"""
        return condition_or(other, self)

    # All math operators except square root, sine, cosine, tangent, inverse trig, comparisons
    def __add__(self, other) -> 'Operator': return math_add(self, other)
    def __radd__(self, other) -> 'Operator': return math_add(other, self)
    def __sub__(self, other) -> 'Operator': return math_subtract(self, other)
    def __rsub__(self, other) -> 'Operator': return math_subtract(other, self)
    def __mul__(self, other) -> 'Operator': return math_multiply(self, other)
    def __rmul__(self, other) -> 'Operator': return math_multiply(other, self)
    def __truediv__(self, other) -> 'Operator': return math_divide(self, other)
    def __rtruediv__(self, other) -> 'Operator': return math_divide(other, self)
    def __pow__(self, power, modulo = None) -> 'Operator': return math_power(self, power)
    def __rpow__(self, other) -> 'Operator': return math_power(other, self)
    def __round__(self, n = None) -> 'Operator': return math_round(self)
    def __floor__(self) -> 'Operator': return math_floor(self)
    def __ceil__(self) -> 'Operator': return math_ceil(self)
    def __abs__(self) -> 'Operator': return math_abs(self)
    def __mod__(self, other) -> 'Operator': return math_modulo(self, other)
    def __rmod__(self, other) -> 'Operator': return math_modulo(other, self)

    # Text operators
    def __getitem__(self, item):
        if type(item) == slice:
            if item.step is not None: raise ValueError('Cannot specify step in Hopscotch')
            return chars_in_range(self, item.start, item.stop)

        return char_at_index(self, item)

    @abc.abstractmethod
    def json(self):
        raise NotImplementedError



class Parameter:
    # 57 = Multipurpose Number Default
    def __init__(self, value: str = '', ptype: int = 57, *, default: str = '',
                 key: str = '', datum = None):
        if type(value) != str: raise BadParameterDataError('Invalid Parameter Value')
        if type(ptype) != int: raise BadParameterDataError('Invalid Parameter Type')
        if type(default) != str: raise BadParameterDataError('Invalid Default Value')
        if type(key) != str: raise BadParameterDataError('Invalid Parameter Key')

        self._default = default
        self._value = value
        self._key = key
        self._type = ptype
        self._datum = datum

    @classmethod
    def from_raw(cls, data):
        """Creates a parameter given some data"""
        if type(data) == Parameter:
            return data

        if type(data) in (int, str, float):
            return Parameter.from_primitive(data)

        if type(data).__name__ in ('Operator', 'HSVariable', 'HSTrait'):
            return Parameter.from_operator(data)

        if type(data).__name__ in ('HSObjectRef', 'HSSelfObjectRef'):
            return Parameter.from_primitive('test')

        if type(data) == DatumResolvable:
            return Parameter.from_raw(data.json()) if data.ready else data

        print(data)
        raise BadParameterDataError('Invalid Parameter Data')

    @classmethod
    def from_primitive(cls, value: int | float | str):
        return cls(str(value))

    @classmethod
    def from_operator(cls, operator):
        return cls(datum = operator)

    def json(self):
        """Converts the parameter to a JSON value"""
        content = {
            "defaultValue": self._default,
            "value": self._value,
            "key": self._key,
            "type": self._type
        }
        if type(self._datum) == DatumResolvable:
            self._datum = self._datum.json()  # needs to resolve twice
        if self._datum:
            content['datum'] = self._datum.json()
        return content


class DatumResolvable(HSDatum):
    def __init__(self, stage, resolver: callable, *args):
        self._resolver = resolver
        self._args = args
        self._stage = stage

    def json(self) -> dict:
        return self._resolver(*self._args)

    @property
    def ready(self):
        return self._stage.objects_loaded


class StringResolvable:
    def __init__(self, stage, resolver: callable, *args):
        self._resolver = resolver
        self._args = args
        self._stage = stage

    def json(self):
        return self._resolver(*self._args)


class Operator(HSDatum):
    def __init__(self, block_id: int, name: str, cls: str = 'operator',
                 params: list[Parameter] | None = None):
        self._cls = cls
        self._params = params
        self._desc = name
        self._type = block_id

    def json(self):
        operator = {"block_class": self._cls, "type": self._type, "description": self._desc}
        if self._params: operator['params'] = [p.json() for p in self._params]
        return operator


class Color(Operator):
    def __init__(self):
        super().__init__(0, 'color')
        raise TypeError('Must call a specific color operator')

    @classmethod
    def random(cls) -> Operator:
        return color_operator_random()

    @classmethod
    def HSB(cls, hue, saturation, brightness) -> Operator:
        return color_operator_hsb(hue, saturation, brightness)


def generate_operator(block_id: int, name: str, cls: str, parameters: list[any] = None):
    return Operator(block_id, name, cls, [Parameter.from_raw(raw) for raw in parameters or []])


class BadParameterDataError(ValueError):
    pass


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


# Renamed operators will be made directly accessible
def matches(text, expression):
    return generate_operator(1008, 'matches', 'conditionalOperator', [text, expression])


def NOT(condition):
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


def square_root(value):
    return generate_operator(4006, 'Math Operator Square Root', 'operator', [value])


def sin(value):
    return generate_operator(4007, 'Math Operator Sine', 'operator', [value])


def cos(value):
    return generate_operator(4008, 'Math Operator Cosine', 'operator', [value])


def math_round(value):
    return generate_operator(4009, 'Math Operator Round', 'operator', [value])


def math_abs(value):
    return generate_operator(4010, 'Math Operator Abs', 'operator', [value])


def math_modulo(val1, val2):
    return generate_operator(4011, 'Math Operator Modulo', 'operator', [val1, val2])


def tan(value):
    return generate_operator(4012, 'Math Operator Tangent', 'operator', [value])


def asin(value):
    return generate_operator(4013, 'Math Operator Inverse Sine', 'operator', [value])


def acos(value):
    return generate_operator(4014, 'Math Operator Inverse Cosine', 'operator', [value])


def atan(value):
    return generate_operator(4015, 'Math Operator Inverse Tangent', 'operator', [value])


def maximum(val1, val2):
    return generate_operator(4016, 'Math Operator Maximum', 'operator', [val1, val2])


def minimum(val1, val2):
    return generate_operator(4017, 'Math Operator Minimum', 'operator', [val1, val2])


def math_floor(value):
    return generate_operator(4018, 'Math Operator Floor', 'operator', [value])


def math_ceil(value):
    return generate_operator(4019, 'Math Operator Ceiling', 'operator', [value])


# Color Operators
def color_operator_random():
    return generate_operator(5000, 'Color Operator Random', 'operator')


def color_operator_rgb(red, green, blue):
    return generate_operator(5001, 'Color Operator RGB', 'operator', [red, green, blue])


def color_operator_hsb(hue, sat, brightness):
    return generate_operator(5002, 'Color Operator HSB', 'operator', [hue, sat, brightness])


def char_at_index(text, index):
    return generate_operator(9000, 'Text Operator Char At Index', 'operator', [text, index])


def chars_in_range(text, start, end):
    return generate_operator(9001, 'Text Operator Chars In Range', 'operator', [text, start, end])


def length(text):
    return generate_operator(9002, 'Text Operator Length', 'operator', [text])


def join(text1, text2):
    return generate_operator(9003, 'Text Operator Join', 'operator', [text1, text2])


def scene_reference_block():
    return generate_operator(10000, 'Scene Reference Block', 'operator')


def previous_scene_parameter():
    return generate_operator(10001, 'Previous Scene', 'operator')


def next_scene_parameter():
    return generate_operator(10002, 'Next Scene', 'operator')


