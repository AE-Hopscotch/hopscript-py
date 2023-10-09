from builder.base import generate_operator


# Object Traits
def trait_rotation(obj):
    return generate_operator(2000, 'Trait Rotation', 'operator', [obj])


def trait_x_position(obj):
    return generate_operator(2001, 'Trait X Position', 'operator', [obj])


def trait_y_position(obj):
    return generate_operator(2002, 'Trait Y Position', 'operator', [obj])


def trait_invisibility(obj):
    return generate_operator(2003, 'Trait Invisibility', 'operator', [obj])


def trait_size(obj):
    return generate_operator(2004, 'Trait Size', 'operator', [obj])


def trait_speed(obj):
    return generate_operator(2005, 'Trait Speed', 'operator', [obj])


def trait_clone_index(obj):
    return generate_operator(2006, 'Trait Clone Index', 'operator', [obj])


def trait_total_clones(obj):
    return generate_operator(2007, 'Trait Total Clones', 'operator', [obj])


def trait_width(obj):
    return generate_operator(2008, 'Trait Width', 'operator', [obj])


def trait_height(obj):
    return generate_operator(2009, 'Trait Height', 'operator', [obj])


def trait_z_index(obj):
    return generate_operator(2010, 'Trait Z Index', 'operator', [obj])


def trait_origin_x(obj):
    return generate_operator(2011, 'Trait Origin X', 'operator', [obj])


def trait_origin_y(obj):
    return generate_operator(2012, 'Trait Origin Y', 'operator', [obj])


def trait_center_x(obj):
    return generate_operator(2013, 'Trait Center X', 'operator', [obj])


def trait_center_y(obj):
    return generate_operator(2014, 'Trait Center Y', 'operator', [obj])


def trait_text(obj):
    return generate_operator(2015, 'Trait Text', 'operator', [obj])


def trait_tempo(obj):
    return generate_operator(2016, 'Trait Tempo', 'operator', [obj])


def trait_instrument(obj):
    return generate_operator(2017, 'Trait Instrument', 'operator', [obj])


def trait_object_name(obj):
    return generate_operator(2018, 'Trait Object Name', 'operator', [obj])


# User Traits
def trait_username():
    return generate_operator(2500, 'Trait Username', 'operator')


def trait_time():
    return generate_operator(2501, 'Trait Time', 'operator')


def trait_year():
    return generate_operator(2502, 'Trait Year', 'operator')


def trait_month():
    return generate_operator(2503, 'Trait Month', 'operator')


def trait_day():
    return generate_operator(2504, 'Trait Day', 'operator')


def trait_hour():
    return generate_operator(2505, 'Trait Hour', 'operator')


def trait_minute():
    return generate_operator(2506, 'Trait Minute', 'operator')


def trait_second():
    return generate_operator(2507, 'Trait Second', 'operator')


# Stage Traits
def stage_trait_width():
    return generate_operator(3000, 'Stage Trait Width', 'operator')


def stage_trait_height():
    return generate_operator(3001, 'Stage Trait Height', 'operator')


def stage_trait_tilt_up():
    return generate_operator(3002, 'Stage Trait Tilt Up', 'operator')


def stage_trait_tilt_down():
    return generate_operator(3003, 'Stage Trait Tilt Down', 'operator')


def stage_trait_tilt_left():
    return generate_operator(3004, 'Stage Trait Tilt Left', 'operator')


def stage_trait_tilt_right():
    return generate_operator(3005, 'Stage Trait Tilt Right', 'operator')


def stage_trait_last_touch_x():
    return generate_operator(3006, 'Stage Trait Last Touch X', 'operator')


def stage_trait_last_touch_y():
    return generate_operator(3007, 'Stage Trait Last Touch Y', 'operator')


def stage_trait_total_objects():
    return generate_operator(3008, 'Stage Trait Total Objects', 'operator')


