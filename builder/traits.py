from builder.util import generate_uuid
from builder.operators import HSDatum


class HSTrait(HSDatum):
    instances = []
    OBJECT = 8000
    GAME = 8003
    SELF = 8004
    ORIGINAL_OBJECT = 8005
    USER = 8007

    def __init__(self, trait_type: int, name: str, *,
                 object_type: int | None = None, object_id: str | None = None):
        self._id = generate_uuid()  # each is unique
        self._type = trait_type
        self._name = name
        self._object = object_id
        self._obj_type = object_type
        if trait_type >= 2500 and (object_id or object_type):
            raise ValueError('Cannot have object associated with stage or user trait')
        elif trait_type < 2500:
            # Must have object type, object_id presence must match "object_type is object-ref"
            if not object_type or (object_type == 8000) != (object_id is not None):
                raise ValueError('Object type missing from object trait')

        self._json = {'HSTraitIDKey': self._id, 'HSTraitTypeKey': trait_type, 'description': name}
        if trait_type >= 2500:
            return

        self._json['HSTraitObjectParameterTypeKey'] = object_type
        if object_type == 8000:
            self._json['HSTraitObjectIDKey'] = object_id

        if object_type == 8005 or object_type == 8000:
            # Each instance is unique per trait
            HSTrait.instances.append(self._json)

    def json(self) -> dict:
        return self._json




# Object Traits
def trait_rotation(obj_type: int, obj_id: str | None = None):
    return HSTrait(2000, 'Rotation', object_type = obj_type, object_id = obj_id)


def trait_x_position(obj_type: int, obj_id: str | None = None):
    return HSTrait(2001, 'X Position', object_type = obj_type, object_id = obj_id)


def trait_y_position(obj_type: int, obj_id: str | None = None):
    return HSTrait(2002, 'Y Position', object_type = obj_type, object_id = obj_id)


def trait_invisibility(obj_type: int, obj_id: str | None = None):
    return HSTrait(2003, 'Invisibility', object_type = obj_type, object_id = obj_id)


def trait_size(obj_type: int, obj_id: str | None = None):
    return HSTrait(2004, 'Size', object_type = obj_type, object_id = obj_id)


def trait_speed(obj_type: int, obj_id: str | None = None):
    return HSTrait(2005, 'Speed', object_type = obj_type, object_id = obj_id)


def trait_clone_index(obj_type: int, obj_id: str | None = None):
    return HSTrait(2006, 'Clone Index', object_type = obj_type, object_id = obj_id)


def trait_total_clones(obj_type: int, obj_id: str | None = None):
    return HSTrait(2007, 'Total Clones', object_type = obj_type, object_id = obj_id)


def trait_width(obj_type: int, obj_id: str | None = None):
    return HSTrait(2008, 'Width', object_type = obj_type, object_id = obj_id)


def trait_height(obj_type: int, obj_id: str | None = None):
    return HSTrait(2009, 'Height', object_type = obj_type, object_id = obj_id)


def trait_z_index(obj_type: int, obj_id: str | None = None):
    return HSTrait(2010, 'Z Index', object_type = obj_type, object_id = obj_id)


def trait_origin_x(obj_type: int, obj_id: str | None = None):
    return HSTrait(2011, 'Origin X', object_type = obj_type, object_id = obj_id)


def trait_origin_y(obj_type: int, obj_id: str | None = None):
    return HSTrait(2012, 'Origin Y', object_type = obj_type, object_id = obj_id)


def trait_center_x(obj_type: int, obj_id: str | None = None):
    return HSTrait(2013, 'Center X', object_type = obj_type, object_id = obj_id)


def trait_center_y(obj_type: int, obj_id: str | None = None):
    return HSTrait(2014, 'Center Y', object_type = obj_type, object_id = obj_id)


def trait_text(obj_type: int, obj_id: str | None = None):
    return HSTrait(2015, 'Text', object_type = obj_type, object_id = obj_id)


def trait_tempo(obj_type: int, obj_id: str | None = None):
    return HSTrait(2016, 'Tempo', object_type = obj_type, object_id = obj_id)


def trait_instrument(obj_type: int, obj_id: str | None = None):
    return HSTrait(2017, 'Instrument', object_type = obj_type, object_id = obj_id)


def trait_object_name(obj_type: int, obj_id: str | None = None):
    return HSTrait(2018, 'Name', object_type = obj_type, object_id = obj_id)


# User Traits
def trait_username():
    return HSTrait(2500, 'Username')


def trait_time():
    return HSTrait(2501, 'Time')


def trait_year():
    return HSTrait(2502, 'Year')


def trait_month():
    return HSTrait(2503, 'Month')


def trait_day():
    return HSTrait(2504, 'Day')


def trait_hour():
    return HSTrait(2505, 'Hour')


def trait_minute():
    return HSTrait(2506, 'Minute')


def trait_second():
    return HSTrait(2507, 'Second')


# Stage Traits
def stage_trait_width():
    return HSTrait(3000, 'Width')


def stage_trait_height():
    return HSTrait(3001, 'Height')


def stage_trait_tilt_up():
    return HSTrait(3002, 'Tilt Up')


def stage_trait_tilt_down():
    return HSTrait(3003, 'Tilt Down')


def stage_trait_tilt_left():
    return HSTrait(3004, 'Tilt Left')


def stage_trait_tilt_right():
    return HSTrait(3005, 'Tilt Right')


def stage_trait_last_touch_x():
    return HSTrait(3006, 'Last Touch X')


def stage_trait_last_touch_y():
    return HSTrait(3007, 'Last Touch Y')


def stage_trait_total_objects():
    return HSTrait(3008, 'Total Objects')


