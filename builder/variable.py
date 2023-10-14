from builder.util import generate_uuid


class HSVariable:
    instances = {}
    OBJECT = 8000
    GAME = 8003
    SELF = 8004
    ORIGINAL_OBJECT = 8005
    USER = 8007
    PRODUCT = 8008
    LOCAL = 8009  # "scoped" in the player

    def __init__(self, var_type: int, name: str, *, object_id: str | None = None):
        self._type = var_type
        self._name = name
        var_format = 8000 if var_type == 8004 or var_type == 8005 else var_type
        self._id = HSVariable.instances.get((var_format, name), generate_uuid())
        self._object = object_id
        if var_type != HSVariable.LOCAL and name not in HSVariable.instances:
            HSVariable.instances[(var_format, name)] = self._id

    def json(self) -> dict:
        if self._type == HSVariable.LOCAL:
            return {"type": HSVariable.LOCAL, "description": "Local Variable", "name": self._name}
        variable_data = {"variable": self._id, "type": self._type, "description": "Variable"}
        if self._type == HSVariable.OBJECT:
            variable_data['object'] = self._object
        return variable_data


class VariableContainer:
    def __init__(self, var_type: int):
        self._type = var_type

    def __getattr__(self, item) -> HSVariable:
        return HSVariable(self._type, item)


original = VariableContainer(HSVariable.ORIGINAL_OBJECT)
game = VariableContainer(HSVariable.GAME)
user = VariableContainer(HSVariable.USER)
product = VariableContainer(HSVariable.PRODUCT)
local = VariableContainer(HSVariable.LOCAL)

