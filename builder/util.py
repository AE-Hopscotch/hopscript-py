from uuid import uuid4

def generate_uuid() -> str:
    return str(uuid4()).upper()


class BadParameterDataError(ValueError):
    pass


class BadObjectDataError(ValueError):
    pass


class Parameter:
    # 57 = Multipurpose Number Default
    def __init__(self, value: str = '', ptype: int = 57, *, default: str = '',
                 key: str = '', datum: 'Operator' = None):
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

        if type(data).__name__ == 'HSObjectRef':
            return Parameter.from_primitive('test')

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
        if self._datum: content['datum'] = self._datum.json()
        return content



class Operator:
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


def generate_operator(block_id: int, name: str, cls: str, parameters: list[any] = None):
    return Operator(block_id, name, cls, [Parameter.from_raw(raw) for raw in parameters or []])


class HSDatum:
    """A data-holding object in Hopscotch code"""
