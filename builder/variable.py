from builder.util import generate_uuid
from builder.traits import *


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


# Include traits in these containers
class ObjectVariableContainer(VariableContainer):
    @property
    def _obj_id(self): return None  # Provide something; makes it easier to override

    @property
    def rotation(self): return trait_rotation(self._type, self._obj_id)
    @property
    def x_position(self): return trait_x_position(self._type, self._obj_id)
    @property
    def y_position(self): return trait_y_position(self._type, self._obj_id)
    @property
    def invisibility(self): return trait_invisibility(self._type, self._obj_id)
    @property
    def size(self): return trait_size(self._type, self._obj_id)
    @property
    def speed(self): return trait_speed(self._type, self._obj_id)
    @property
    def clone_index(self): return trait_clone_index(self._type, self._obj_id)
    @property
    def total_clones(self): return trait_total_clones(self._type, self._obj_id)
    @property
    def width(self): return trait_width(self._type, self._obj_id)
    @property
    def height(self): return trait_height(self._type, self._obj_id)
    @property
    def z_index(self): return trait_z_index(self._type, self._obj_id)
    @property
    def origin_x(self): return trait_origin_x(self._type, self._obj_id)
    @property
    def origin_y(self): return trait_origin_y(self._type, self._obj_id)
    @property
    def center_x(self): return trait_center_x(self._type, self._obj_id)
    @property
    def center_y(self): return trait_center_y(self._type, self._obj_id)
    @property
    def text(self): return trait_text(self._type, self._obj_id)
    @property
    def tempo(self): return trait_tempo(self._type, self._obj_id)
    @property
    def instrument(self): return trait_instrument(self._type, self._obj_id)
    @property
    def name(self): return trait_object_name(self._type, self._obj_id)


class UserVariableContainer(VariableContainer):
    def __init__(self):
        super().__init__(HSVariable.USER)

    @property
    def username(self): return trait_username()
    @property
    def time(self): return trait_time()
    @property
    def year(self): return trait_year()
    @property
    def month(self): return trait_month()
    @property
    def day(self): return trait_day()
    @property
    def hour(self): return trait_hour()
    @property
    def minute(self): return trait_minute()
    @property
    def second(self): return trait_second()


original = ObjectVariableContainer(HSVariable.ORIGINAL_OBJECT)
game = VariableContainer(HSVariable.GAME)
user = UserVariableContainer()
product = VariableContainer(HSVariable.PRODUCT)
local = VariableContainer(HSVariable.LOCAL)
