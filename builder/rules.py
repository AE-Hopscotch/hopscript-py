from builder.base import generate_operator


# Rule
def rule(value):
    return generate_operator(6000, 'Rule', 'operator', [value])


# idk what to do yet
def rule_preview(value):
    return generate_operator(6001, 'Rule Preview', 'operator', [value])


def event_start():
    return generate_operator(7000, 'Game Starts', 'operator')


def event_tap(obj):
    return generate_operator(7001, 'Is Tapped', 'operator', [obj])


def event_is_touching(obj1, obj2):
    return generate_operator(7002, 'Is Touching', 'operator', [obj1, obj2])


def event_hold(obj):
    return generate_operator(7003, 'Hold', 'operator', [obj])


def event_tilt_right():
    return generate_operator(7004, 'Tilt Right', 'operator')


def event_tilt_left():
    return generate_operator(7005, 'Tilt Left', 'operator')


def event_tilt_up():
    return generate_operator(7006, 'Tilt Up', 'operator')


def event_tilt_down():
    return generate_operator(7007, 'Tilt Down', 'operator')


def event_loud_noise():
    return generate_operator(7008, 'Loud Noise', 'operator')


def event_shake():
    return generate_operator(7009, 'Shake', 'operator')


def event_bump(obj1, obj2):
    return generate_operator(7010, 'Bump', 'operator', [obj1, obj2])


def event_swipe_right(obj):
    return generate_operator(7011, 'Swipe Right', 'operator', [obj])


def event_swipe_left(obj):
    return generate_operator(7012, 'Swipe Left', 'operator', [obj])


def event_swipe_up(obj):
    return generate_operator(7013, 'Swipe Up', 'operator', [obj])


def event_swipe_down(obj):
    return generate_operator(7014, 'Swipe Down', 'operator', [obj])


def event_enter_the_world():
    return generate_operator(7015, 'Object is Cloned', 'operator')


def event_tilt_right_editor():
    return generate_operator(7016, 'Tilt Right Editor', 'operator')


def event_tilt_left_editor():
    return generate_operator(7017, 'Tilt Left Editor', 'operator')


def event_tilt_up_editor():
    return generate_operator(7018, 'Tilt Up Editor', 'operator')


def event_tilt_down_editor():
    return generate_operator(7019, 'Tilt Down Editor', 'operator')


def event_not_pressed(obj):
    return generate_operator(7020, 'Not Pressed', 'operator', [obj])


def event_game_playing():
    return generate_operator(7021, 'Game Playing', 'operator')


def event_touch_ends():
    return generate_operator(7022, 'Touch Ends', 'operator')


def event_hear_message(message):
    return generate_operator(7023, 'Hear Message', 'operator', [message])


def event_message_matches(message):
    return generate_operator(7024, 'Message Matches', 'operator', [message])


def event_is_not_touching(obj1, obj2):
    return generate_operator(7025, 'Is Not Touching', 'operator', [obj1, obj2])
